#!/usr/bin/env python3
"""
Render an audio-script chapter (audio/script/ch-NN.md) to segment WAVs via
MisoTTS (AUDIO_SPEC.md §5-§7).

Audio-script markdown conventions (resolved from AUDIO_SPEC, documented here
since the spec doesn't pin down a literal schema):

    ---                     (optional YAML-ish frontmatter, key: value lines)
    voice-default: narration
    ---
    # Chapter Ten. Three Gates.        <- H1, becomes the chapter-title block

    A regular paragraph renders in the file's default voice (narration,
    unless overridden by voice-default: part-opening for a part-title or
    prologue file).

    > A blockquote renders in the quotation anchor voice. Every block quote
    > from Chesterton, Rawls, Ostrom goes here.
    > -- Attribution line (starts with "-- " or an em dash)

    ::: part-opening
    A fenced div overrides the voice for just this block (narration,
    quotation, or part-opening) regardless of the file default.
    :::

    A standalone line of three or more hyphens is a section break:

    ---

Chunking rule (AUDIO_SPEC §7): split each block on sentence boundaries, then
merge adjacent sentences up to ~200 characters, never merging across a
paragraph break -- so paragraphs are chunked independently by construction.

Rendering context (AUDIO_SPEC §7): every generate() call receives the fixed
anchor segment for that block's voice, plus a rolling window of the last 2-3
segments generated *in that same voice*. Each voice's rolling window is
independent (mixing quotation-voice audio into the narration anchor's
context would degrade narration continuity) and all windows reset when a
new chapter starts, which is exactly what invoking render.py once per
chapter file already gives you.

Usage:
    # See the chunk plan without loading anything (no torch/Miso needed):
    python3 render.py audio/script/ch-10.md --dry-run

    # Real render on a rented CUDA box:
    python3 render.py audio/script/ch-10.md \\
        --device cuda \\
        --anchors-config audio/anchors.json \\
        --lexicon audio/lexicon.tsv \\
        --out-dir audio/renders/ch-10

    # Resume an interrupted render (skips already-rendered segments whose
    # render text hasn't changed, but still seeds the rolling context from
    # their audio on disk so continuity is preserved across the resume):
    python3 render.py audio/script/ch-10.md --device cuda --resume \\
        --anchors-config audio/anchors.json --out-dir audio/renders/ch-10

anchors.json schema:
    {
      "narration":    {"wav": "voice/seed/author/narration.wav",  "text": "..."},
      "quotation":    {"wav": "voice/seed/author/quotation.wav",  "text": "..."},
      "part-opening": {"wav": "voice/seed/author/part-opening.wav", "text": "..."}
    }
Only the voices actually used in the chapter need an entry.

Output: one WAV per segment, plus manifest.json (segment-id, source text,
render text, voice, boundary_after, timing) -- the exact contract asr_diff.py
and assemble.py both consume.
"""

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass, field
from typing import List, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VOICES = ("narration", "quotation", "part-opening")
DEFAULT_SPEAKER_IDS = {"narration": 0, "quotation": 1, "part-opening": 2}
DEFAULT_MAX_CHARS = 200
DEFAULT_CONTEXT_SEGMENTS = 3
MISO_REPO_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "MisoTTS",
)
MISO_MODEL_REPO_ID = "MisoLabs/MisoTTS"
MISO_MS_PER_CHAR = 90
MISO_MS_HEADROOM = 2000
MISO_MAX_AUDIO_MS = 30_000
MISO_TEMPERATURE = 0.9
MISO_TOPK = 50

# Boundary -> which assemble.py silence bucket applies after this chunk.
# (assemble.py owns the actual millisecond values; this is just the label.)
BOUNDARY_SENTENCE = "sentence"
BOUNDARY_PARAGRAPH = "paragraph"
BOUNDARY_SECTION = "section"
BOUNDARY_CHAPTER_END = "chapter_end"


# ---------------------------------------------------------------------------
# Parsing: audio-script markdown -> Blocks -> Chunks
# ---------------------------------------------------------------------------

@dataclass
class Block:
    block_type: str      # chapter_title | paragraph | header | blockquote | attribution
    voice: str
    text: str
    section_index: int
    is_last_in_section: bool = False
    is_last_overall: bool = False


@dataclass
class Chunk:
    index: int
    block_type: str
    voice: str
    source_text: str
    boundary_after: str


_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'“‘(])")
_FENCE_START_RE = re.compile(r"^:::\s*(\S+)\s*$")
_FENCE_END_RE = re.compile(r"^:::\s*$")


def strip_frontmatter(raw):
    m = _FRONTMATTER_RE.match(raw)
    if not m:
        return {}, raw
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, raw[m.end():]


def clean_text(text):
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\s)\*([^*\n]+?)\*(?!\s*$)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_title(body):
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            rest = "\n".join(lines[i + 1:])
            return title, rest
        if line.strip():
            break  # first non-blank line isn't an H1 -- no title block
    return None, body


def parse_blockquote(para):
    lines = [ln.strip() for ln in para.split("\n")]
    quote_lines, attribution = [], ""
    for ln in lines:
        content = None
        if ln.startswith("> "):
            content = ln[2:].strip()
        elif ln.startswith(">"):
            content = ln[1:].strip()
        if content is None:
            continue
        if content.startswith("-- ") or content.startswith("—"):
            attribution = content.lstrip("-— ").strip()
        else:
            quote_lines.append(content)
    return clean_text(" ".join(quote_lines)), clean_text(attribution) if attribution else ""


def parse_blocks(body, default_voice):
    """Split the (post-frontmatter, post-title) body into ordered Blocks."""
    sections = re.split(r"\n---+\n", body)
    blocks = []

    for section_idx, section in enumerate(sections):
        section = section.strip()
        if not section:
            continue
        paragraphs = [p for p in re.split(r"\n\s*\n", section) if p.strip()]
        section_blocks = []

        i = 0
        while i < len(paragraphs):
            para = paragraphs[i].strip()

            fence_m = _FENCE_START_RE.match(para.split("\n", 1)[0])
            if fence_m:
                label = fence_m.group(1)
                voice = label if label in VOICES else default_voice
                # Collect until a closing ::: fence, possibly across
                # multiple "paragraphs" (blank-line-separated chunks).
                inner_lines = para.split("\n")[1:]
                collected = list(inner_lines)
                j = i
                closed = any(_FENCE_END_RE.match(ln) for ln in inner_lines)
                while not closed and j + 1 < len(paragraphs):
                    j += 1
                    more_lines = paragraphs[j].split("\n")
                    collected.extend(more_lines)
                    closed = any(_FENCE_END_RE.match(ln) for ln in more_lines)
                text_lines = [ln for ln in collected if not _FENCE_END_RE.match(ln)]
                text = clean_text("\n".join(text_lines))
                if text:
                    section_blocks.append(Block("paragraph", voice, text, section_idx))
                i = j + 1
                continue

            if para.startswith(">"):
                quote_text, attribution = parse_blockquote(para)
                if quote_text:
                    section_blocks.append(Block("blockquote", "quotation", quote_text, section_idx))
                if attribution:
                    section_blocks.append(Block("attribution", "quotation", attribution, section_idx))
                i += 1
                continue

            if para.startswith("## ") or para.startswith("### "):
                header_text = clean_text(re.sub(r"^#+\s+", "", para))
                if header_text:
                    section_blocks.append(Block("header", default_voice, header_text, section_idx))
                i += 1
                continue

            if re.match(r"^\|", para):
                # Table -- not audio-representable; skip with a spoken note.
                section_blocks.append(Block(
                    "paragraph", default_voice,
                    "The following table is available in the printed edition.",
                    section_idx,
                ))
                i += 1
                continue

            text = clean_text(para)
            if text:
                section_blocks.append(Block("paragraph", default_voice, text, section_idx))
            i += 1

        if section_blocks:
            section_blocks[-1].is_last_in_section = True
            blocks.extend(section_blocks)

    if blocks:
        blocks[-1].is_last_overall = True
    return blocks


def chunk_block_text(text, max_chars):
    """Sentence-split then merge up to max_chars. Never crosses a Block
    boundary (each Block is chunked independently) -- this is what keeps
    paragraph breaks as seams, per AUDIO_SPEC §7."""
    sentences = [s.strip() for s in _SENTENCE_SPLIT_RE.split(text) if s.strip()]
    if not sentences:
        return [text] if text else []

    chunks, current = [], ""
    for sentence in sentences:
        candidate = f"{current} {sentence}".strip() if current else sentence
        if not current or len(candidate) <= max_chars:
            current = candidate
        else:
            chunks.append(current)
            current = sentence
    if current:
        chunks.append(current)

    final = []
    for c in chunks:
        if len(c) <= max_chars * 1.5:
            final.append(c)
        else:
            final.extend(_hard_split(c, max_chars))
    return final


def _hard_split(text, max_chars):
    words = text.split(" ")
    chunks, current = [], ""
    for word in words:
        candidate = f"{current} {word}".strip() if current else word
        if not current or len(candidate) <= max_chars:
            current = candidate
        else:
            chunks.append(current)
            current = word
    if current:
        chunks.append(current)
    return chunks


def build_chunk_plan(script_path, max_chars=DEFAULT_MAX_CHARS):
    """Parse an audio-script file into an ordered list of Chunks.

    Returns (chapter_id, meta, chunks).
    """
    with open(script_path, encoding="utf-8") as f:
        raw = f.read()

    meta, body = strip_frontmatter(raw)
    default_voice = meta.get("voice-default", "narration")
    if default_voice not in VOICES:
        default_voice = "narration"

    title, rest = extract_title(body)
    blocks = []
    if title:
        blocks.append(Block("chapter_title", default_voice, clean_text(title), -1,
                             is_last_in_section=True))

    body_blocks = parse_blocks(rest, default_voice)
    blocks.extend(body_blocks)
    if blocks:
        blocks[-1].is_last_overall = True

    chapter_id = os.path.splitext(os.path.basename(script_path))[0]

    chunks = []
    idx = 0
    for block in blocks:
        pieces = chunk_block_text(block.text, max_chars)
        if not pieces:
            continue
        for k, piece in enumerate(pieces):
            is_last_piece = (k == len(pieces) - 1)
            if not is_last_piece:
                boundary = BOUNDARY_SENTENCE
            elif block.is_last_overall:
                boundary = BOUNDARY_CHAPTER_END
            elif block.is_last_in_section:
                boundary = BOUNDARY_SECTION
            elif block.block_type == "chapter_title":
                boundary = BOUNDARY_SECTION
            else:
                boundary = BOUNDARY_PARAGRAPH
            chunks.append(Chunk(idx, block.block_type, block.voice, piece, boundary))
            idx += 1

    return chapter_id, meta, chunks


# ---------------------------------------------------------------------------
# Lexicon (print form -> render form substitution, render text only)
# ---------------------------------------------------------------------------

def load_lexicon(path):
    """TSV: print_form \\t render_form \\t status. Header row required."""
    rows = []
    if not path or not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f if ln.strip()]
    if not lines:
        return rows
    for line in lines[1:]:  # skip header
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        print_form, render_form = parts[0], parts[1]
        if print_form and render_form and print_form != render_form:
            rows.append((print_form, render_form))
    rows.sort(key=lambda r: len(r[0]), reverse=True)
    return rows


def apply_lexicon(text, lexicon_rows):
    for print_form, render_form in lexicon_rows:
        pattern = re.compile(r"\b" + re.escape(print_form) + r"\b")

        def repl(m, render_form=render_form):
            matched = m.group(0)
            if matched.isupper():
                return render_form.upper()
            if matched[0].isupper():
                return render_form[0].upper() + render_form[1:]
            return render_form

        text = pattern.sub(repl, text)
    return text


# ---------------------------------------------------------------------------
# Dry run
# ---------------------------------------------------------------------------

def print_dry_run(chapter_id, meta, chunks, lexicon_rows):
    print(f"\n{'=' * 70}")
    print(f"CHUNK PLAN: {chapter_id}")
    if meta:
        print(f"frontmatter: {meta}")
    print(f"{'=' * 70}\n")

    voice_counts = {}
    total_chars = 0
    for c in chunks:
        voice_counts[c.voice] = voice_counts.get(c.voice, 0) + 1
        total_chars += len(c.source_text)
        render_text = apply_lexicon(c.source_text, lexicon_rows)
        marker = " *lexicon*" if render_text != c.source_text else ""
        preview = c.source_text if len(c.source_text) <= 90 else c.source_text[:87] + "..."
        print(f"  [{c.index:04d}] {c.block_type:<13} {c.voice:<13} "
              f"({len(c.source_text):3d} ch, after={c.boundary_after:<11}){marker}  {preview}")

    print(f"\n{'-' * 70}")
    print(f"Total chunks: {len(chunks)}")
    for voice, n in voice_counts.items():
        print(f"  {voice}: {n}")
    print(f"Total characters: {total_chars}")
    est_seconds = total_chars / 15.0  # ~15 chars/sec at audiobook pace, rough
    print(f"Rough estimated duration: ~{est_seconds / 60:.1f} min "
          f"(15 chars/sec heuristic, not a substitute for a real render)")


# ---------------------------------------------------------------------------
# Real render (torch / MisoTTS -- lazy imports only reached here)
# ---------------------------------------------------------------------------

def miso_max_audio_ms(text):
    return min(MISO_MAX_AUDIO_MS, int(len(text) * MISO_MS_PER_CHAR) + MISO_MS_HEADROOM)


def load_anchors_config(path):
    if not path:
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def content_hash(voice, render_text, speaker_id):
    h = hashlib.sha256()
    h.update(f"{voice}\x1f{speaker_id}\x1f{render_text}".encode("utf-8"))
    return h.hexdigest()[:16]


def run_render(args):
    import numpy as np
    import soundfile as sf

    chapter_id, meta, chunks = build_chunk_plan(args.script, args.max_chars)
    lexicon_rows = load_lexicon(args.lexicon)
    voices_used = sorted({c.voice for c in chunks})

    out_dir = args.out_dir or os.path.join("audio", "renders", chapter_id)
    os.makedirs(out_dir, exist_ok=True)
    manifest_path = args.manifest_out or os.path.join(out_dir, "manifest.json")
    checkpoint_path = os.path.join(out_dir, "checkpoint.json")

    checkpoint = {}
    if args.resume and os.path.exists(checkpoint_path):
        with open(checkpoint_path, encoding="utf-8") as f:
            checkpoint = json.load(f)

    # --- speaker IDs ---
    speaker_ids = dict(DEFAULT_SPEAKER_IDS)
    if args.speaker_narration is not None:
        speaker_ids["narration"] = args.speaker_narration
    if args.speaker_quotation is not None:
        speaker_ids["quotation"] = args.speaker_quotation
    if args.speaker_part_opening is not None:
        speaker_ids["part-opening"] = args.speaker_part_opening

    # --- anchors ---
    anchors_config = load_anchors_config(args.anchors_config)
    missing_anchor_voices = []
    anchor_specs = {}
    per_voice_flags = {
        "narration": (args.anchor_narration_wav, args.anchor_narration_text),
        "quotation": (args.anchor_quotation_wav, args.anchor_quotation_text),
        "part-opening": (args.anchor_part_opening_wav, args.anchor_part_opening_text),
    }
    for voice in voices_used:
        if voice in anchors_config:
            anchor_specs[voice] = (anchors_config[voice]["wav"], anchors_config[voice]["text"])
        elif per_voice_flags[voice][0] and per_voice_flags[voice][1]:
            anchor_specs[voice] = per_voice_flags[voice]
        else:
            missing_anchor_voices.append(voice)

    if missing_anchor_voices:
        print(f"ERROR: no anchor configured for voice(s): {', '.join(missing_anchor_voices)}")
        print("Provide --anchors-config audio/anchors.json, or the per-voice "
              "--anchor-<voice>-wav/--anchor-<voice>-text flags.")
        sys.exit(2)

    # --- lazy heavy imports ---
    if MISO_REPO_DIR not in sys.path:
        sys.path.insert(0, MISO_REPO_DIR)
    import torch
    from generator import Segment, load_miso_8b

    print(f"  Loading MisoTTS on {args.device} (bf16)...")
    generator = load_miso_8b(device=args.device, model_path_or_repo_id=args.miso_model,
                              dtype=torch.bfloat16)
    sample_rate = generator.sample_rate
    print(f"  Sample rate: {sample_rate} Hz")

    def load_anchor_segment(voice):
        import torchaudio
        wav_path, transcript = anchor_specs[voice]
        audio, sr = torchaudio.load(wav_path)
        if audio.ndim > 1:
            audio = audio.mean(dim=0)
        audio = torchaudio.functional.resample(audio, orig_freq=sr, new_freq=sample_rate)
        return Segment(speaker=speaker_ids[voice], text=transcript, audio=audio)

    anchor_segments = {voice: load_anchor_segment(voice) for voice in voices_used}

    from collections import deque
    context_windows = {voice: deque(maxlen=args.context_window) for voice in voices_used}

    manifest_segments = []

    def save_manifest():
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump({
                "chapter_id": chapter_id,
                "sample_rate": sample_rate,
                "engine": "miso",
                "segments": manifest_segments,
            }, f, indent=2)

    for chunk in chunks:
        seg_id = f"{chapter_id}-{chunk.index:04d}"
        render_text = apply_lexicon(chunk.source_text, lexicon_rows)
        wav_path = os.path.join(out_dir, f"{seg_id}.wav")
        speaker_id = speaker_ids[chunk.voice]
        h = content_hash(chunk.voice, render_text, speaker_id)

        cached = checkpoint.get(seg_id)
        if args.resume and cached and cached.get("hash") == h and os.path.exists(wav_path):
            audio_np, sr_on_disk = sf.read(wav_path, dtype="float32")
            audio_tensor = torch.from_numpy(audio_np)
            print(f"  [{chunk.index:04d}] {seg_id}: cached (resume)")
        else:
            max_ms = miso_max_audio_ms(render_text)
            context = [anchor_segments[chunk.voice]] + list(context_windows[chunk.voice])
            audio_tensor = generator.generate(
                text=render_text,
                speaker=speaker_id,
                context=context,
                max_audio_length_ms=max_ms,
                temperature=args.temperature,
                topk=args.topk,
            )
            audio_np = audio_tensor.detach().to(torch.float32).cpu().numpy()
            sf.write(wav_path, audio_np, sample_rate)
            checkpoint[seg_id] = {"hash": h}
            with open(checkpoint_path, "w", encoding="utf-8") as f:
                json.dump(checkpoint, f, indent=2)
            print(f"  [{chunk.index:04d}] {seg_id}: rendered "
                  f"({len(audio_np) / sample_rate:.2f}s)")

        context_windows[chunk.voice].append(
            Segment(speaker=speaker_id, text=render_text, audio=audio_tensor))

        duration_ms = int(1000 * len(audio_np) / sample_rate)
        manifest_segments.append({
            "segment_id": seg_id,
            "chapter_id": chapter_id,
            "index": chunk.index,
            "block_type": chunk.block_type,
            "voice": chunk.voice,
            "speaker_id": speaker_id,
            "source_text": chunk.source_text,
            "render_text": render_text,
            "wav_path": os.path.abspath(wav_path),
            "sample_rate": sample_rate,
            "duration_ms": duration_ms,
            "boundary_after": chunk.boundary_after,
        })
        save_manifest()

    print(f"\n  Rendered {len(manifest_segments)} segments to {out_dir}")
    print(f"  Manifest: {manifest_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(
        description="Render an audio-script chapter to segment WAVs via "
                     "MisoTTS (AUDIO_SPEC.md §5-§7).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("script", type=str, help="Path to audio/script/ch-NN.md")
    p.add_argument("--dry-run", action="store_true",
                    help="Print the chunk plan and exit. No model load, no "
                         "audio, no torch/soundfile import.")
    p.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS,
                    help=f"Chunk merge budget in characters (default: {DEFAULT_MAX_CHARS})")
    p.add_argument("--lexicon", type=str, default=os.path.join("audio", "lexicon.tsv"),
                    help="Path to lexicon.tsv (print form -> render form). "
                         "Applied to render text only.")
    p.add_argument("--out-dir", type=str, default=None,
                    help="Output dir for segment WAVs + manifest.json "
                         "(default: audio/renders/<chapter-id>/)")
    p.add_argument("--manifest-out", type=str, default=None,
                    help="Override manifest.json path (default: <out-dir>/manifest.json)")
    p.add_argument("--resume", action="store_true",
                    help="Skip segments already rendered with identical "
                         "render text (checked via checkpoint.json), but "
                         "still seed the rolling context from their audio "
                         "on disk so continuity across the resume point "
                         "is preserved.")
    p.add_argument("--device", type=str, default="cpu", choices=["cuda", "cpu"],
                    help="MisoTTS device. Production renders happen on "
                         "rented CUDA hardware (AUDIO_SPEC §11); cpu is for "
                         "local smoke-testing only. MPS is deliberately not "
                         "offered here -- it is broken upstream (float64 "
                         "ops in the watermarker/Mimi codec).")
    p.add_argument("--miso-model", type=str, default=MISO_MODEL_REPO_ID,
                    help=f"Miso model path or HF repo id (default: {MISO_MODEL_REPO_ID})")
    p.add_argument("--context-window", type=int, default=DEFAULT_CONTEXT_SEGMENTS,
                    help=f"Rolling context segments per voice (default: {DEFAULT_CONTEXT_SEGMENTS})")
    p.add_argument("--temperature", type=float, default=MISO_TEMPERATURE)
    p.add_argument("--topk", type=int, default=MISO_TOPK)

    p.add_argument("--speaker-narration", type=int, default=None,
                    help=f"Speaker id for narration voice (default: {DEFAULT_SPEAKER_IDS['narration']})")
    p.add_argument("--speaker-quotation", type=int, default=None,
                    help=f"Speaker id for quotation voice (default: {DEFAULT_SPEAKER_IDS['quotation']})")
    p.add_argument("--speaker-part-opening", type=int, default=None,
                    help=f"Speaker id for part-opening voice (default: {DEFAULT_SPEAKER_IDS['part-opening']})")

    p.add_argument("--anchors-config", type=str, default=None,
                    help="JSON file mapping voice -> {wav, text}. Takes "
                         "precedence over the per-voice flags below.")
    p.add_argument("--anchor-narration-wav", type=str, default=None)
    p.add_argument("--anchor-narration-text", type=str, default=None)
    p.add_argument("--anchor-quotation-wav", type=str, default=None)
    p.add_argument("--anchor-quotation-text", type=str, default=None)
    p.add_argument("--anchor-part-opening-wav", type=str, default=None)
    p.add_argument("--anchor-part-opening-text", type=str, default=None)

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.dry_run:
        chapter_id, meta, chunks = build_chunk_plan(args.script, args.max_chars)
        lexicon_rows = load_lexicon(args.lexicon)
        print_dry_run(chapter_id, meta, chunks, lexicon_rows)
        return

    run_render(args)


if __name__ == "__main__":
    main()
