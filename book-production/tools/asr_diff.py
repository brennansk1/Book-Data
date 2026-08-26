#!/usr/bin/env python3
"""
ASR-diff QC harness for the audio pipeline (AUDIO_SPEC.md §10).

"Nine and a half hours of audio is roughly fifteen hours of human QC with
rewinds, and autoregressive TTS drops and hallucinates words at a low but
nonzero rate that a tired listener will miss. Run Whisper over every
rendered segment and diff the transcript against the source text. Flag any
mismatch above a small edit-distance threshold for human review."

This is the highest-value engineering step in the project and is built
before a single chapter is rendered.

Contract:
    Input:  a directory of rendered segment WAVs + the segment manifest JSON
            that render.py writes (segment-id -> source text / render text /
            wav path). See render.py's --help for the manifest schema.
    Output: a JSON report + a human-readable report, both listing every
            segment with its word-edit-distance and WER against the text
            that was actually fed to the model (render_text by default --
            see --compare-field), and flagging anything above threshold.
    Exit:   0 if nothing is flagged, 1 if anything is flagged or a hard
            error occurred (missing file, transcription failure, etc).

Usage:
    # Pure logic self-test -- no audio, no ML deps, safe to run anywhere:
    python3 asr_diff.py --self-test

    # Real QC pass over a rendered chapter:
    python3 asr_diff.py \\
        --manifest audio/renders/ch-10/manifest.json \\
        --renders-dir audio/renders/ch-10 \\
        --model-size small \\
        --out-json reviews/ch-10/asr_diff.json \\
        --out-txt reviews/ch-10/asr_diff.txt

Whisper backend: tries faster-whisper first, then openai-whisper, whichever
import succeeds (--engine to force one). Both are optional dependencies --
this module has zero third-party imports until a real transcription run
starts, so `--help` and `--self-test` work in a bare Python 3 environment.
"""

import argparse
import json
import os
import re
import sys
import time

# ---------------------------------------------------------------------------
# Number-to-words (small, built-in -- no dependency on num2words et al.)
# ---------------------------------------------------------------------------

_ONES = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",
]
_TENS = [
    "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
    "eighty", "ninety",
]
_SCALES = [(1_000_000_000, "billion"), (1_000_000, "million"), (1_000, "thousand")]


def _two_digit_words(n):
    if n < 20:
        return _ONES[n]
    tens, ones = divmod(n, 10)
    word = _TENS[tens]
    if ones:
        word += f" {_ONES[ones]}"
    return word


def _three_digit_words(n):
    parts = []
    hundreds, rem = divmod(n, 100)
    if hundreds:
        parts.append(f"{_ONES[hundreds]} hundred")
    if rem:
        parts.append(_two_digit_words(rem))
    return " ".join(parts) if parts else "zero"


def cardinal_words(n):
    """Spell out an integer: 1971 -> 'one thousand nine hundred seventy one'."""
    if n == 0:
        return "zero"
    if n < 0:
        return "negative " + cardinal_words(-n)
    parts = []
    remaining = n
    for scale_val, name in _SCALES:
        if remaining >= scale_val:
            count, remaining = divmod(remaining, scale_val)
            parts.append(f"{_three_digit_words(count)} {name}")
    if remaining or not parts:
        parts.append(_three_digit_words(remaining))
    return " ".join(parts)


def year_pair_words(n):
    """Spell out a 4-digit number the way a reader speaks a year.

    1971 -> 'nineteen seventy one', 2005 -> 'twenty oh five',
    1900 -> 'nineteen hundred'. This mirrors the audio-script convention
    (AUDIO_SPEC §8: 'Nineteen seventy-one,' not '1971') so that a Whisper
    hypothesis which fell back to digits still normalizes to match the
    reference, which was written as spelled-out words in the first place.
    """
    if not (1000 <= n <= 9999):
        return cardinal_words(n)
    first, second = divmod(n, 100)
    if second == 0:
        return f"{_three_digit_words(first)} hundred"
    first_word = _three_digit_words(first)
    if second < 10:
        second_word = f"oh {_ONES[second]}"
    else:
        second_word = _two_digit_words(second)
    return f"{first_word} {second_word}"


_DIGIT_RUN_RE = re.compile(r"\d+")


def digits_to_words(text):
    """Replace every run of digits in text with its spelled-out form.

    4-digit runs use the year-pair reading (the common case in this
    manuscript); everything else uses plain cardinal reading.
    """
    def repl(m):
        raw = m.group(0)
        n = int(raw)
        if len(raw) == 4:
            return year_pair_words(n)
        return cardinal_words(n)

    return _DIGIT_RUN_RE.sub(repl, text)


# ---------------------------------------------------------------------------
# Text normalization + word-level edit distance
# ---------------------------------------------------------------------------

_PUNCT_RE = re.compile(r"[^a-z0-9\s]")
_WS_RE = re.compile(r"\s+")


def normalize(text):
    """Lowercase, spell out numbers, strip punctuation, collapse whitespace."""
    text = digits_to_words(text)
    text = text.lower()
    text = _PUNCT_RE.sub(" ", text)
    text = _WS_RE.sub(" ", text).strip()
    return text


def word_edit_distance(ref_words, hyp_words):
    """Levenshtein distance over word sequences (insert/delete/substitute, cost 1)."""
    n, m = len(ref_words), len(hyp_words)
    if n == 0:
        return m
    if m == 0:
        return n
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        curr = [i] + [0] * m
        ri = ref_words[i - 1]
        for j in range(1, m + 1):
            cost = 0 if ri == hyp_words[j - 1] else 1
            curr[j] = min(
                prev[j] + 1,       # deletion
                curr[j - 1] + 1,   # insertion
                prev[j - 1] + cost,  # substitution / match
            )
        prev = curr
    return prev[m]


def diff_segment(ref_text, hyp_text):
    """Normalize both sides and return (distance, wer, ref_words, hyp_words)."""
    ref_norm = normalize(ref_text)
    hyp_norm = normalize(hyp_text)
    ref_words = ref_norm.split()
    hyp_words = hyp_norm.split()
    distance = word_edit_distance(ref_words, hyp_words)
    wer = distance / max(1, len(ref_words))
    return distance, wer, ref_words, hyp_words


def is_flagged(distance, wer, word_edit_threshold, wer_threshold):
    return distance > word_edit_threshold or wer > wer_threshold


# ---------------------------------------------------------------------------
# Whisper backends (lazy -- only touched outside --self-test)
# ---------------------------------------------------------------------------

def load_whisper_engine(model_size, engine_pref="auto"):
    """Return (transcribe_fn(wav_path) -> str, engine_name).

    Tries faster-whisper first (lighter, faster on CPU), then openai-whisper,
    whichever import succeeds -- unless a specific engine is forced.
    """
    errors = []

    if engine_pref in ("auto", "faster-whisper"):
        try:
            from faster_whisper import WhisperModel  # noqa: F401 (lazy)
            model = WhisperModel(model_size)

            def transcribe(path):
                segments, _info = model.transcribe(path)
                return " ".join(seg.text for seg in segments).strip()

            return transcribe, "faster-whisper"
        except ImportError as e:
            errors.append(f"faster-whisper: {e}")
            if engine_pref == "faster-whisper":
                raise RuntimeError(
                    "faster-whisper requested but not importable: "
                    "pip install faster-whisper"
                ) from e

    if engine_pref in ("auto", "whisper"):
        try:
            import whisper  # noqa: F401 (lazy)
            model = whisper.load_model(model_size)

            def transcribe(path):
                result = model.transcribe(path)
                return result["text"].strip()

            return transcribe, "whisper"
        except ImportError as e:
            errors.append(f"openai-whisper: {e}")
            if engine_pref == "whisper":
                raise RuntimeError(
                    "openai-whisper requested but not importable: "
                    "pip install openai-whisper"
                ) from e

    raise RuntimeError(
        "No Whisper backend available. Install one of:\n"
        "  pip install faster-whisper\n"
        "  pip install openai-whisper\n"
        "Import errors:\n  " + "\n  ".join(errors)
    )


# ---------------------------------------------------------------------------
# Manifest loading
# ---------------------------------------------------------------------------

def load_manifest(manifest_path):
    with open(manifest_path, encoding="utf-8") as f:
        data = json.load(f)
    segments = data["segments"] if isinstance(data, dict) else data
    return data if isinstance(data, dict) else {"segments": segments}, segments


def resolve_wav_path(segment, manifest_path, renders_dir):
    if renders_dir:
        return os.path.join(renders_dir, os.path.basename(segment["wav_path"]))
    wav_path = segment["wav_path"]
    if os.path.isabs(wav_path):
        return wav_path
    return os.path.join(os.path.dirname(os.path.abspath(manifest_path)), wav_path)


# ---------------------------------------------------------------------------
# Main QC pass
# ---------------------------------------------------------------------------

def run_qc(args):
    manifest_data, segments = load_manifest(args.manifest)
    transcribe, engine_name = load_whisper_engine(args.model_size, args.engine)

    print(f"  Engine: {engine_name} | model size: {args.model_size}")
    print(f"  Segments: {len(segments)}")
    print(f"  Compare field: {args.compare_field}")
    print(f"  Thresholds: >{args.word_edit_threshold} word edit(s) OR "
          f">{args.wer_threshold * 100:.1f}% WER\n")

    results = []
    flagged_count = 0
    error_count = 0

    for i, seg in enumerate(segments):
        seg_id = seg.get("segment_id", f"seg-{i:04d}")
        ref_text = seg.get(args.compare_field, "")
        wav_path = resolve_wav_path(seg, args.manifest, args.renders_dir)

        if not os.path.exists(wav_path):
            print(f"  [{i:04d}] {seg_id}: ERROR wav not found: {wav_path}")
            results.append({
                "segment_id": seg_id, "error": f"wav not found: {wav_path}",
                "flagged": True,
            })
            error_count += 1
            continue

        try:
            hyp_text = transcribe(wav_path)
        except Exception as e:  # noqa: BLE001 -- surface any backend failure
            print(f"  [{i:04d}] {seg_id}: ERROR transcription failed: {e}")
            results.append({
                "segment_id": seg_id, "error": f"transcription failed: {e}",
                "flagged": True,
            })
            error_count += 1
            continue

        distance, wer, ref_words, hyp_words = diff_segment(ref_text, hyp_text)
        flagged = is_flagged(distance, wer, args.word_edit_threshold, args.wer_threshold)
        if flagged:
            flagged_count += 1

        status = "FLAG" if flagged else "ok"
        print(f"  [{i:04d}] {seg_id}: dist={distance} wer={wer * 100:.1f}% [{status}]")

        results.append({
            "segment_id": seg_id,
            "wav_path": wav_path,
            "voice": seg.get("voice"),
            "compare_field": args.compare_field,
            "reference_text": ref_text,
            "hypothesis_text": hyp_text,
            "reference_words": len(ref_words),
            "hypothesis_words": len(hyp_words),
            "edit_distance": distance,
            "wer": round(wer, 4),
            "flagged": flagged,
        })

    report = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "manifest": os.path.abspath(args.manifest),
        "engine": engine_name,
        "model_size": args.model_size,
        "compare_field": args.compare_field,
        "thresholds": {
            "word_edit_threshold": args.word_edit_threshold,
            "wer_threshold": args.wer_threshold,
        },
        "summary": {
            "total_segments": len(segments),
            "flagged": flagged_count,
            "errors": error_count,
        },
        "segments": results,
    }

    if args.out_json:
        os.makedirs(os.path.dirname(os.path.abspath(args.out_json)) or ".", exist_ok=True)
        with open(args.out_json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"\n  JSON report: {args.out_json}")

    txt_lines = [
        f"ASR diff report -- {report['generated_at']}",
        f"manifest: {report['manifest']}",
        f"engine: {engine_name} ({args.model_size})",
        f"thresholds: >{args.word_edit_threshold} word edit(s) OR "
        f">{args.wer_threshold * 100:.1f}% WER",
        "",
        f"{report['summary']['total_segments']} segments, "
        f"{flagged_count} flagged, {error_count} errors",
        "",
    ]
    for r in results:
        if not r.get("flagged"):
            continue
        if "error" in r:
            txt_lines.append(f"[{r['segment_id']}] ERROR: {r['error']}")
            continue
        txt_lines.append(
            f"[{r['segment_id']}] dist={r['edit_distance']} wer={r['wer'] * 100:.1f}%"
        )
        txt_lines.append(f"  ref: {r['reference_text']}")
        txt_lines.append(f"  hyp: {r['hypothesis_text']}")
        txt_lines.append("")

    txt_report = "\n".join(txt_lines)
    if args.out_txt:
        os.makedirs(os.path.dirname(os.path.abspath(args.out_txt)) or ".", exist_ok=True)
        with open(args.out_txt, "w", encoding="utf-8") as f:
            f.write(txt_report)
        print(f"  Text report: {args.out_txt}")

    print(f"\n  {flagged_count} flagged, {error_count} error(s) "
          f"out of {len(segments)} segments")

    return 1 if (flagged_count or error_count) else 0


# ---------------------------------------------------------------------------
# Self-test (no audio, no ML deps)
# ---------------------------------------------------------------------------

def run_self_test():
    failures = []

    def check(name, condition):
        status = "PASS" if condition else "FAIL"
        print(f"  [{status}] {name}")
        if not condition:
            failures.append(name)

    # Number conversion
    check("cardinal_words(0) == 'zero'", cardinal_words(0) == "zero")
    check("cardinal_words(15) == 'fifteen'", cardinal_words(15) == "fifteen")
    check("cardinal_words(42) == 'forty two'", cardinal_words(42) == "forty two")
    check("cardinal_words(100) == 'one hundred'", cardinal_words(100) == "one hundred")
    check("year_pair_words(1971) == 'nineteen seventy one'",
          year_pair_words(1971) == "nineteen seventy one")
    check("year_pair_words(2005) == 'twenty oh five'",
          year_pair_words(2005) == "twenty oh five")
    check("year_pair_words(1900) == 'nineteen hundred'",
          year_pair_words(1900) == "nineteen hundred")

    # Normalization
    check("normalize strips punctuation and case",
          normalize("Ostrom's Third Principle!") == "ostrom s third principle")
    check("normalize spells out digits",
          normalize("in 1971,") == normalize("in nineteen seventy-one"))

    # Exact match -> zero distance
    d, wer, ref_w, hyp_w = diff_segment(
        "Elinor Ostrom walked the Valencia huerta in nineteen seventy-one.",
        "elinor ostrom walked the valencia huerta in nineteen seventy one",
    )
    check("exact match (mod. case/punct) -> distance 0", d == 0)
    check("exact match -> wer 0.0", wer == 0.0)

    # A digit-vs-spelled year should still match after normalization
    d, wer, _, _ = diff_segment(
        "The court has met since 1239.",
        "the court has met since twelve thirty nine",
    )
    check("digit year normalizes to match spelled year", d == 0)

    # One dropped word on a short segment: distance 1 is at the edit
    # threshold (not flagged by that metric alone) but 1/16 words = 6.25%
    # WER trips the 5% WER threshold -- exactly the point of having both
    # metrics on short TTS segments.
    ref = ("The obvious objection to a rule is that rules are stupid "
           "they do not know what is happening")
    hyp = ("the obvious objection to a rule is that rules are stupid "
           "they do know what is happening")  # "not" dropped
    d, wer, _, _ = diff_segment(ref, hyp)
    check("one dropped word on a short segment -> distance 1", d == 1)
    check("one dropped word on a short segment -> flagged via WER",
          is_flagged(d, wer, word_edit_threshold=1, wer_threshold=0.05))

    # The same single dropped word on a longer reference stays under both
    # thresholds and should NOT be flagged.
    long_ref = (
        "The obvious objection to a rule is that rules are stupid they do "
        "not know what is happening in the specific case in front of you "
        "right now and that is exactly the point a rule is defending"
    )
    long_hyp = long_ref.replace("do not know", "do know")  # "not" dropped
    d, wer, _, _ = diff_segment(long_ref, long_hyp)
    check("one dropped word on a long segment -> distance 1", d == 1)
    check("one dropped word on a long segment -> not flagged at default thresholds",
          not is_flagged(d, wer, word_edit_threshold=1, wer_threshold=0.05))

    # Two errors (a hallucinated word + a dropped word) on a short segment
    # -- should flag both by distance and by WER
    ref2 = "Everyone hates this."
    hyp2 = "Everyone really hates."  # inserted "really", dropped "this"
    d2, wer2, _, _ = diff_segment(ref2, hyp2)
    check("hallucination + drop -> distance >= 2", d2 >= 2)
    check("hallucination + drop -> flagged", is_flagged(d2, wer2, 1, 0.05))

    # word_edit_distance basic properties
    check("word_edit_distance identical lists -> 0",
          word_edit_distance(["a", "b", "c"], ["a", "b", "c"]) == 0)
    check("word_edit_distance empty ref -> len(hyp)",
          word_edit_distance([], ["a", "b"]) == 2)
    check("word_edit_distance empty hyp -> len(ref)",
          word_edit_distance(["a", "b"], []) == 2)

    print(f"\n  {len(failures)} failure(s) out of self-test")
    return 1 if failures else 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(
        description="ASR-diff QC harness: transcribe rendered TTS segments "
                     "with Whisper and diff against the source text "
                     "(AUDIO_SPEC.md §10).",
    )
    p.add_argument("--manifest", type=str,
                    help="Segment manifest JSON written by render.py")
    p.add_argument("--renders-dir", type=str, default=None,
                    help="Directory of rendered segment WAVs. If omitted, "
                         "wav_path from the manifest is used directly "
                         "(resolved relative to the manifest's directory).")
    p.add_argument("--model-size", type=str, default="small",
                    help="Whisper model size (tiny/base/small/medium/large*, "
                         "default: small)")
    p.add_argument("--engine", type=str, default="auto",
                    choices=["auto", "whisper", "faster-whisper"],
                    help="Force a specific Whisper backend (default: auto, "
                         "tries faster-whisper then openai-whisper)")
    p.add_argument("--compare-field", type=str, default="render_text",
                    choices=["render_text", "source_text"],
                    help="Which manifest field to diff the transcript "
                         "against. render_text (default) is what was "
                         "actually fed to the model, post-lexicon "
                         "substitution -- the correct QC target. "
                         "source_text is the pre-substitution print text.")
    p.add_argument("--word-edit-threshold", type=int, default=1,
                    help="Flag if word edit distance exceeds this (default: "
                         "1, i.e. flag on 2+ word edits)")
    p.add_argument("--wer-threshold", type=float, default=0.05,
                    help="Flag if WER exceeds this fraction (default: 0.05 "
                         "= 5%%)")
    p.add_argument("--out-json", type=str, default=None,
                    help="Write the full JSON report here")
    p.add_argument("--out-txt", type=str, default=None,
                    help="Write the human-readable report here")
    p.add_argument("--self-test", action="store_true",
                    help="Run the built-in normalization/edit-distance "
                         "self-test on synthetic strings and exit. No "
                         "audio or ML dependencies required.")
    return p


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.self_test:
        sys.exit(run_self_test())

    if not args.manifest:
        parser.error("--manifest is required (unless --self-test)")

    sys.exit(run_qc(args))


if __name__ == "__main__":
    main()
