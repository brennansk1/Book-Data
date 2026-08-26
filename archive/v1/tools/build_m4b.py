#!/usr/bin/env python3
"""
Build a professional M4B audiobook from per-chapter MP3s.

Output: single M4B file (AAC in MP4 container) with:
  - Chapter markers (navigable in Apple Books, Audible, Plex, etc.)
  - Full metadata (title, author/narrator, genre, year, description)
  - Audiobook-standard AAC encoding (64 kbps mono, 44.1 kHz)

Also builds a fallback full_audiobook.mp3 via concat (no re-encode) for players
that don't support M4B.
"""

import json
import os
import re
import subprocess
import sys

PROJECT_DIR = "/Users/brennankelley/Desktop/Projects/Book-Data-main"
AUDIOBOOK_DIR = os.path.join(PROJECT_DIR, "Audiobook")
MP3_DIR = os.path.join(AUDIOBOOK_DIR, "mp3")
CHAPTERS_DIR = os.path.join(PROJECT_DIR, "Book", "Chapters")

BOOK_TITLE = "The Manual of Harmonious Rationality"
BOOK_AUTHOR = "Brennan Kelley"
BOOK_NARRATOR = "Kokoro TTS (am_michael)"
BOOK_YEAR = "2026"
BOOK_GENRE = "Audiobook"
BOOK_DESCRIPTION = (
    "A rigorous moral system spanning foundations, personal ethics, political "
    "philosophy, economics, and a defense against rival systems. Built to defeat "
    "rival frameworks in head-to-head debate and to be fully lived by a real person."
)

# Chapter title overrides / friendly names derived from filename.
BOOK_PART_BOUNDARIES = {
    # First track of each Book — inserts a Book announcement before the chapter title.
    "02_CH-01.mp3": "Book One. Foundations. What Is Real?",
    "07_CH-06.mp3": "Book Two. The Enemy. Why Suffering Persists.",
    "10_CH-09.mp3": "Book Three. The Moral Architecture. How to Decide.",
    "14_CH-13.mp3": "Book Four. Personal Ethics. Living the System.",
    "18_CH-17.mp3": "Book Five. Political Philosophy. Engineering the State.",
    "27_CH-26.mp3": "Book Six. Economic Philosophy. The Machinery of Prosperity.",
    "33_CH-32.mp3": "Book Seven. The Frontier. Problems at the Edge.",
    "38_CH-37.mp3": "Book Eight. Defense. Defeating Rival Systems.",
    "48_CH-47.mp3": "Book Nine. Synthesis.",
}


def ffprobe_duration(path: str) -> float:
    """Exact duration in seconds via ffprobe."""
    out = subprocess.check_output([
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        path,
    ]).decode().strip()
    return float(out)


def read_chapter_title(mp3_name: str) -> str:
    """Derive a human-friendly chapter title from the source markdown H1."""
    # mp3 name format: "NN_ID.mp3" where ID is e.g. CH-01, PREFACE, TITLE_PAGE, BACK_MATTER
    m = re.match(r"^\d+_(.+)\.mp3$", mp3_name)
    if not m:
        return mp3_name
    chapter_id = m.group(1)

    md_path = os.path.join(CHAPTERS_DIR, f"{chapter_id}.md")
    if os.path.exists(md_path):
        with open(md_path) as f:
            for line in f:
                if line.startswith("# "):
                    return line[2:].strip()
    # Fallbacks
    return chapter_id.replace("_", " ").title()


def escape_meta(s: str) -> str:
    """Escape = ; # \\ and newlines for FFMETADATA1."""
    return (
        s.replace("\\", "\\\\")
         .replace("=", "\\=")
         .replace(";", "\\;")
         .replace("#", "\\#")
         .replace("\n", "\\\n")
    )


def build():
    files = sorted(f for f in os.listdir(MP3_DIR) if f.endswith(".mp3"))
    if not files:
        print("No MP3 files found.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(files)} tracks. Probing durations...")

    # Probe all durations and accumulate chapter offsets (in milliseconds for FFMETADATA).
    chapters = []
    cum_ms = 0
    for f in files:
        path = os.path.join(MP3_DIR, f)
        dur_s = ffprobe_duration(path)
        dur_ms = int(round(dur_s * 1000))
        title = read_chapter_title(f)

        # Book part announcement — prepend to title so the chapter marker is descriptive.
        if f in BOOK_PART_BOUNDARIES:
            title = f"{BOOK_PART_BOUNDARIES[f]} — {title}"

        chapters.append({
            "file": f,
            "title": title,
            "start_ms": cum_ms,
            "end_ms": cum_ms + dur_ms,
            "duration_s": dur_s,
        })
        cum_ms += dur_ms

    total_s = cum_ms / 1000.0
    h, rem = divmod(int(total_s), 3600)
    m_, s_ = divmod(rem, 60)
    print(f"Total runtime: {h}:{m_:02d}:{s_:02d}  ({len(chapters)} chapters)")

    # Write ffmpeg concat list
    concat_list = os.path.join(AUDIOBOOK_DIR, "_concat.txt")
    with open(concat_list, "w") as fh:
        for c in chapters:
            path = os.path.join(MP3_DIR, c["file"]).replace("'", r"'\''")
            fh.write(f"file '{path}'\n")

    # Write FFMETADATA with chapter markers + global tags
    meta_path = os.path.join(AUDIOBOOK_DIR, "_chapters.ffmetadata")
    with open(meta_path, "w") as fh:
        fh.write(";FFMETADATA1\n")
        fh.write(f"title={escape_meta(BOOK_TITLE)}\n")
        fh.write(f"artist={escape_meta(BOOK_AUTHOR)}\n")
        fh.write(f"album_artist={escape_meta(BOOK_AUTHOR)}\n")
        fh.write(f"album={escape_meta(BOOK_TITLE)}\n")
        fh.write(f"composer={escape_meta(BOOK_NARRATOR)}\n")
        fh.write(f"date={BOOK_YEAR}\n")
        fh.write(f"genre={escape_meta(BOOK_GENRE)}\n")
        fh.write(f"description={escape_meta(BOOK_DESCRIPTION)}\n")
        fh.write(f"comment={escape_meta(BOOK_DESCRIPTION)}\n")
        fh.write("media_type=2\n")  # 2 = Audiobook in iTunes/Apple
        fh.write("\n")
        for c in chapters:
            fh.write("[CHAPTER]\n")
            fh.write("TIMEBASE=1/1000\n")
            fh.write(f"START={c['start_ms']}\n")
            fh.write(f"END={c['end_ms']}\n")
            fh.write(f"title={escape_meta(c['title'])}\n")

    # ----------------------------------------------------------------
    # Build M4B (AAC, 64 kbps mono, 44.1 kHz) — the audiobook standard
    # ----------------------------------------------------------------
    m4b_path = os.path.join(AUDIOBOOK_DIR, "The_Manual_of_Harmonious_Rationality.m4b")
    print(f"\nEncoding M4B → {m4b_path}")
    print("  (this will take a while — encoding ~28 hours of audio to AAC)")

    cmd = [
        "ffmpeg", "-y",
        "-hide_banner", "-loglevel", "warning", "-stats",
        "-f", "concat", "-safe", "0", "-i", concat_list,
        "-i", meta_path,
        "-map_metadata", "1",
        "-map_chapters", "1",
        "-vn",
        "-ac", "1",           # mono
        "-ar", "44100",       # 44.1 kHz
        "-c:a", "aac",
        "-b:a", "64k",        # audiobook-standard bitrate
        "-movflags", "+faststart",
        "-f", "mp4",
        m4b_path,
    ]
    subprocess.run(cmd, check=True)

    size_mb = os.path.getsize(m4b_path) / (1024 * 1024)
    print(f"  M4B: {size_mb:.0f} MB")

    # ----------------------------------------------------------------
    # Build fallback single MP3 via concat (no re-encode, fast)
    # ----------------------------------------------------------------
    mp3_path = os.path.join(AUDIOBOOK_DIR, "The_Manual_of_Harmonious_Rationality.mp3")
    print(f"\nCopying concatenated MP3 → {mp3_path}")
    cmd = [
        "ffmpeg", "-y",
        "-hide_banner", "-loglevel", "warning",
        "-f", "concat", "-safe", "0", "-i", concat_list,
        "-i", meta_path,
        "-map_metadata", "1",
        "-map", "0:a",
        "-c:a", "copy",
        "-id3v2_version", "3",
        mp3_path,
    ]
    subprocess.run(cmd, check=True)
    size_mb = os.path.getsize(mp3_path) / (1024 * 1024)
    print(f"  MP3: {size_mb:.0f} MB")

    # Write a chapter TOC for reference
    toc_path = os.path.join(AUDIOBOOK_DIR, "CHAPTERS.txt")
    with open(toc_path, "w") as fh:
        fh.write(f"{BOOK_TITLE}\n")
        fh.write(f"by {BOOK_AUTHOR}\n")
        fh.write(f"Runtime: {h}:{m_:02d}:{s_:02d}\n")
        fh.write(f"Tracks: {len(chapters)}\n\n")
        for i, c in enumerate(chapters, 1):
            ts_s = c["start_ms"] // 1000
            hh, rr = divmod(ts_s, 3600)
            mm, ss = divmod(rr, 60)
            fh.write(f"{i:02d}. [{hh:02d}:{mm:02d}:{ss:02d}] {c['title']}\n")
    print(f"  TOC: {toc_path}")

    # Clean up intermediate files
    os.remove(concat_list)
    os.remove(meta_path)

    print("\nDone.")


if __name__ == "__main__":
    build()
