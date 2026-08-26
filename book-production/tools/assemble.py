#!/usr/bin/env python3
"""
Assemble rendered segment WAVs into a mastered chapter file
(AUDIO_SPEC.md §7).

Takes the segment manifest that render.py writes (WAV path + boundary_after
per segment), concatenates with the silence table, adds a low-level
room-tone bed, normalizes loudness, and writes chapter masters at 44.1 kHz
plus a duration report.

Silence table (AUDIO_SPEC §7):
    sentence within paragraph   350 ms
    paragraph                  700 ms
    section break              1.2 s
    chapter end                2.5 s

Loudness: target -19 LUFS integrated (window -18 to -20), true peak
<= -3 dBTP, 44.1 kHz (ACX-style spec -- verify against your actual
distributor). If `pyloudnorm` is importable it's used directly; otherwise
this script falls back to writing an unnormalized 44.1kHz intermediate WAV
and printing (and saving, via --emit-ffmpeg-cmd) the exact two-pass ffmpeg
loudnorm command to run instead.

Usage:
    python3 assemble.py --help
    python3 assemble.py --manifest audio/renders/ch-10/manifest.json \\
        --out-dir audio/masters

Dependencies: stdlib + numpy/soundfile/pydub (all required -- these are
declared baseline deps for this tool, not lazy). pyloudnorm is optional and
imported lazily; ffmpeg is required either way (pydub shells out to it for
concatenation/resampling, and it's the documented fallback for loudness
normalization).
"""

import argparse
import json
import os
import sys
import time

import numpy as np
import soundfile as sf
from pydub import AudioSegment

# ---------------------------------------------------------------------------
# Silence table (AUDIO_SPEC §7)
# ---------------------------------------------------------------------------

SILENCE_MS = {
    "sentence": 350,
    "paragraph": 700,
    "section": 1200,
    "chapter_end": 2500,
}

DEFAULT_TARGET_LUFS = -19.0
DEFAULT_LUFS_WINDOW = (-20.0, -18.0)
DEFAULT_TRUE_PEAK_DBTP = -3.0
DEFAULT_ROOM_TONE_DBFS = -60.0
DEFAULT_SAMPLE_RATE = 44100


# ---------------------------------------------------------------------------
# Manifest loading
# ---------------------------------------------------------------------------

def load_manifest(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        chapter_id = data.get("chapter_id", os.path.splitext(os.path.basename(path))[0])
        segments = data["segments"]
    else:
        chapter_id = os.path.splitext(os.path.basename(path))[0]
        segments = data
    segments = sorted(segments, key=lambda s: s.get("index", 0))
    return chapter_id, segments


# ---------------------------------------------------------------------------
# Concatenation
# ---------------------------------------------------------------------------

def concatenate_chapter(segments, target_sample_rate):
    """Load every segment WAV, resample to target_sample_rate, concatenate
    with the silence table applied after each segment. Returns a pydub
    AudioSegment."""
    combined = AudioSegment.empty()
    combined = combined.set_frame_rate(target_sample_rate).set_channels(1)

    for seg in segments:
        wav_path = seg["wav_path"]
        if not os.path.exists(wav_path):
            raise FileNotFoundError(f"segment wav not found: {wav_path} "
                                     f"(segment {seg.get('segment_id')})")
        audio = AudioSegment.from_wav(wav_path)
        if audio.frame_rate != target_sample_rate:
            audio = audio.set_frame_rate(target_sample_rate)
        if audio.channels != 1:
            audio = audio.set_channels(1)
        combined += audio

        boundary = seg.get("boundary_after", "paragraph")
        silence_ms = SILENCE_MS.get(boundary, SILENCE_MS["paragraph"])
        combined += AudioSegment.silent(duration=silence_ms, frame_rate=target_sample_rate)

    return combined


# ---------------------------------------------------------------------------
# Room tone bed
# ---------------------------------------------------------------------------

def generate_room_tone(duration_ms, sample_rate, target_dbfs, seed=0):
    """Shaped (brown-ish) noise bed at roughly target_dbfs.

    Neural TTS output is unnaturally clean; a near-inaudible noise floor
    keeps nine-plus hours from feeling fatiguing (AUDIO_SPEC §7). White
    noise passed through a short moving-average (box) filter approximates
    a gently low-passed noise floor. Implemented as a cumulative-sum trick
    so it's fully vectorized -- a per-sample Python loop here would take
    minutes on a chapter-length (tens of millions of samples) bed.
    """
    rng = np.random.default_rng(seed)
    n_samples = int(sample_rate * duration_ms / 1000)
    white = rng.normal(0, 1, n_samples).astype(np.float64)

    window = max(1, int(sample_rate * 0.0007))  # ~0.7ms box filter, gentle HF rolloff
    padded = np.concatenate([np.zeros(window), white])
    cumsum = np.cumsum(padded)
    shaped = (cumsum[window:] - cumsum[:-window]) / window
    shaped = shaped / (np.max(np.abs(shaped)) + 1e-9)

    # Scale to target dBFS (RMS-referenced, the perceptually relevant
    # measure for a noise floor rather than its peak).
    rms = np.sqrt(np.mean(shaped ** 2)) + 1e-12
    target_rms = 10 ** (target_dbfs / 20)
    shaped = shaped * (target_rms / rms)
    return shaped.astype(np.float32)


def overlay_room_tone(combined_segment, target_dbfs, seed=0):
    sample_rate = combined_segment.frame_rate
    duration_ms = len(combined_segment)
    noise = generate_room_tone(duration_ms, sample_rate, target_dbfs, seed=seed)

    noise_i16 = np.clip(noise * 32767, -32768, 32767).astype(np.int16)
    noise_segment = AudioSegment(
        noise_i16.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1,
    )
    return combined_segment.overlay(noise_segment)


# ---------------------------------------------------------------------------
# Loudness normalization
# ---------------------------------------------------------------------------

def pydub_to_numpy(segment):
    samples = np.array(segment.get_array_of_samples()).astype(np.float32)
    samples /= float(1 << (8 * segment.sample_width - 1))
    return samples, segment.frame_rate


def numpy_to_wav(samples, sample_rate, path, subtype="PCM_16"):
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    sf.write(path, samples, sample_rate, subtype=subtype)


def estimate_true_peak_dbtp(samples, oversample=4, block_size=1_000_000):
    """Approximate true peak via linear-interpolation oversampling.

    This is a lightweight stand-in for a proper ITU-R BS.1770 true-peak
    filter (which needs a polyphase resampler). Oversampling by linear
    interpolation catches most inter-sample peaks that a bare sample-peak
    reading misses, without pulling in scipy; it is conservative but not
    exact. For a release-grade true-peak measurement, verify with a DAW or
    ffmpeg's astats/loudnorm filter before shipping.

    Processed in overlapping blocks so memory stays bounded on a
    chapter-length (tens of millions of samples) array -- oversampling the
    whole thing at once would allocate `oversample`x its size at float64.
    """
    n = len(samples)
    if n < 2:
        peak = float(np.max(np.abs(samples))) if n else 0.0
        return 20 * np.log10(max(peak, 1e-12))

    overall_peak = 0.0
    step = block_size
    for start in range(0, n, step):
        # One sample of overlap on each side so inter-sample peaks at block
        # boundaries aren't missed.
        lo = max(0, start - 1)
        hi = min(n, start + step + 1)
        block = samples[lo:hi]
        x = np.arange(len(block))
        xi = np.linspace(0, len(block) - 1, len(block) * oversample)
        upsampled = np.interp(xi, x, block)
        overall_peak = max(overall_peak, float(np.max(np.abs(upsampled))))

    return 20 * np.log10(max(overall_peak, 1e-12))


def normalize_loudness_pyloudnorm(samples, sample_rate, target_lufs, true_peak_dbtp):
    import pyloudnorm as pyln

    meter = pyln.Meter(sample_rate)
    integrated_lufs = meter.integrated_loudness(samples)
    gain_db = target_lufs - integrated_lufs
    gained = samples * (10 ** (gain_db / 20))

    peak_dbtp = estimate_true_peak_dbtp(gained)
    if peak_dbtp > true_peak_dbtp:
        reduction_db = peak_dbtp - true_peak_dbtp
        gained = gained * (10 ** (-reduction_db / 20))
        peak_dbtp = true_peak_dbtp

    final_lufs = meter.integrated_loudness(gained)
    return gained, {
        "measured_lufs_before": round(float(integrated_lufs), 2),
        "gain_applied_db": round(float(gain_db), 2),
        "measured_lufs_after": round(float(final_lufs), 2),
        "estimated_true_peak_dbtp": round(float(peak_dbtp), 2),
        "method": "pyloudnorm",
    }


def ffmpeg_loudnorm_command(in_wav, out_wav, target_lufs, true_peak_dbtp, lra=11):
    return (
        f'ffmpeg -y -i "{in_wav}" -af '
        f'loudnorm=I={target_lufs}:TP={true_peak_dbtp}:LRA={lra}:print_format=summary '
        f'-ar {DEFAULT_SAMPLE_RATE} "{out_wav}"'
    )


# ---------------------------------------------------------------------------
# Main assembly
# ---------------------------------------------------------------------------

def assemble_chapter(args):
    chapter_id, segments = load_manifest(args.manifest)
    if not segments:
        print(f"ERROR: no segments in manifest {args.manifest}")
        return 1

    print(f"  Chapter: {chapter_id}")
    print(f"  Segments: {len(segments)}")

    combined = concatenate_chapter(segments, args.sample_rate)
    print(f"  Concatenated duration: {len(combined) / 1000:.1f}s")

    if args.room_tone_dbfs is not None:
        combined = overlay_room_tone(combined, args.room_tone_dbfs, seed=args.room_tone_seed)
        print(f"  Room tone bed added at ~{args.room_tone_dbfs} dBFS")

    samples, sample_rate = pydub_to_numpy(combined)

    os.makedirs(args.out_dir, exist_ok=True)
    master_path = os.path.join(args.out_dir, f"{chapter_id}.wav")

    loudness_report = None
    try:
        import pyloudnorm  # noqa: F401
        normalized, loudness_report = normalize_loudness_pyloudnorm(
            samples, sample_rate, args.target_lufs, args.true_peak_dbtp)
        numpy_to_wav(normalized, sample_rate, master_path)
        lo, hi = args.lufs_window
        in_window = lo <= loudness_report["measured_lufs_after"] <= hi
        print(f"  Loudness (pyloudnorm): {loudness_report['measured_lufs_before']} LUFS -> "
              f"{loudness_report['measured_lufs_after']} LUFS "
              f"(window {lo}..{hi}: {'OK' if in_window else 'OUT OF WINDOW'})")
        print(f"  Estimated true peak: {loudness_report['estimated_true_peak_dbtp']} dBTP")
        print(f"  Master written: {master_path}")
    except ImportError:
        prenorm_path = os.path.join(args.out_dir, f"{chapter_id}.prenorm.wav")
        numpy_to_wav(samples, sample_rate, prenorm_path)
        cmd = ffmpeg_loudnorm_command(prenorm_path, master_path, args.target_lufs,
                                       args.true_peak_dbtp)
        print("  pyloudnorm not installed -- wrote unnormalized intermediate WAV.")
        print(f"  Intermediate: {prenorm_path}")
        print("  Run this to produce the mastered, loudness-normalized file:")
        print(f"    {cmd}")
        loudness_report = {
            "method": "ffmpeg_fallback",
            "intermediate_wav": prenorm_path,
            "ffmpeg_command": cmd,
        }

    duration_seconds = len(samples) / sample_rate
    manifest_total_ms = sum(s.get("duration_ms", 0) for s in segments)
    manifest_total_s = manifest_total_ms / 1000

    report = {
        "chapter_id": chapter_id,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "manifest": os.path.abspath(args.manifest),
        "master_wav": os.path.abspath(master_path),
        "sample_rate": sample_rate,
        "segment_count": len(segments),
        "duration_seconds": round(duration_seconds, 2),
        "duration_formatted": format_duration(duration_seconds),
        "segment_audio_seconds_from_manifest": round(manifest_total_s, 2),
        "silence_table_ms": SILENCE_MS,
        "room_tone_dbfs": args.room_tone_dbfs,
        "target_lufs": args.target_lufs,
        "lufs_window": list(args.lufs_window),
        "true_peak_dbtp_target": args.true_peak_dbtp,
        "loudness": loudness_report,
    }

    report_path = args.report_out or os.path.join(args.out_dir, f"{chapter_id}.duration_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"  Duration report: {report_path}")
    print(f"  Total duration: {report['duration_formatted']}")

    return 0


def format_duration(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(
        description="Assemble rendered segment WAVs into a mastered chapter "
                     "file with silence table, room tone, and loudness "
                     "normalization (AUDIO_SPEC.md §7).",
    )
    p.add_argument("--manifest", type=str, required=True,
                    help="Segment manifest JSON written by render.py")
    p.add_argument("--out-dir", type=str, default=os.path.join("audio", "masters"),
                    help="Output directory for the chapter master + report "
                         "(default: audio/masters)")
    p.add_argument("--report-out", type=str, default=None,
                    help="Override duration report path")
    p.add_argument("--sample-rate", type=int, default=DEFAULT_SAMPLE_RATE,
                    help=f"Master sample rate (default: {DEFAULT_SAMPLE_RATE})")
    p.add_argument("--target-lufs", type=float, default=DEFAULT_TARGET_LUFS,
                    help=f"Target integrated LUFS (default: {DEFAULT_TARGET_LUFS})")
    p.add_argument("--lufs-window", type=float, nargs=2, default=list(DEFAULT_LUFS_WINDOW),
                    metavar=("LOW", "HIGH"),
                    help=f"Acceptable integrated LUFS window (default: {DEFAULT_LUFS_WINDOW})")
    p.add_argument("--true-peak-dbtp", type=float, default=DEFAULT_TRUE_PEAK_DBTP,
                    help=f"Max true peak in dBTP (default: {DEFAULT_TRUE_PEAK_DBTP})")
    p.add_argument("--room-tone-dbfs", type=float, default=DEFAULT_ROOM_TONE_DBFS,
                    help="Room-tone bed level in dBFS, or a very negative "
                         f"number effectively disables it (default: {DEFAULT_ROOM_TONE_DBFS})")
    p.add_argument("--room-tone-seed", type=int, default=0,
                    help="RNG seed for the room-tone noise bed (default: 0, "
                         "for reproducible masters)")
    return p


def main():
    parser = build_parser()
    args = parser.parse_args()
    sys.exit(assemble_chapter(args))


if __name__ == "__main__":
    main()
