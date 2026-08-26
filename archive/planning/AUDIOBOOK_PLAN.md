# Audiobook Production Plan

## Overview

Produce a professional audiobook of *The Manual of Harmonious Rationality* (~205,000 words, 48 chapters + front/back matter) using **Kokoro TTS**, an open-source 82M-parameter text-to-speech engine.

**Expected output:** ~51 MP3 files, ~22-23 hours total audio, ~1.9 GB at 192kbps  
**Generation time:** ~15-20 minutes on modern hardware  
**Voice:** `am_michael` (American male, clear and measured) at speed 0.92  

---

## Dependencies

### System (via Homebrew)
```bash
brew install espeak-ng ffmpeg
```
- `espeak-ng` — phoneme generation backend for Kokoro
- `ffmpeg` — audio format conversion (WAV to MP3)

### Python (via pip)
```bash
pip3 install kokoro soundfile numpy pydub mutagen
```
- `kokoro` — the TTS engine (auto-downloads ~80MB voice model on first use)
- `soundfile` — WAV file I/O
- `numpy` — audio array manipulation
- `pydub` — MP3 conversion
- `mutagen` — ID3 tag writing

---

## Script: `generate_audiobook.py`

A single Python file at the project root with these components:

### 1. Configuration Block

| Setting | Value | Rationale |
|---------|-------|-----------|
| Voice | `am_michael` | Clear American male with gravitas for philosophy |
| Speed | 0.92 | ~150 wpm; slightly slower than default for dense argument |
| Sample rate | 24,000 Hz | Kokoro native rate |
| MP3 bitrate | 192 kbps | High quality for speech clarity |
| Output dir | `Audiobook/mp3/` and `Audiobook/wav/` | Keeps audio separate from book source |

**Pause durations (silence inserted between segments):**

| Context | Duration | Why |
|---------|----------|-----|
| After book section announcement | 3.0s | "Book One. Foundations." needs breathing room |
| After chapter title announcement | 2.0s | Let the title land before content begins |
| At `---` horizontal rules | 1.5s | Major section transitions |
| Before/after `##` headers | 1.0s | Section changes |
| Before/after `###` headers | 0.7s | Subsection changes |
| Before/after blockquotes | 0.8s | Set off quoted material |
| Between paragraphs | 0.4s | Natural breath pause |
| Between list items | 0.3s | Keep lists flowing but distinct |
| End of chapter | 3.0s | Clean ending before next track |

**Chapter ordering:** Mirrors `BOOK_ORDER` from `build_book.py` exactly (lines 12-94).

### 2. Text Preprocessing

This is the most critical component. Raw markdown must become clean, natural speech text.

#### What Gets Stripped
- `#`, `##`, `###` header markers (text kept as section announcements)
- `**bold**` and `*italic*` markers
- `---` horizontal rules (replaced with silence)
- `> ` blockquote line prefixes
- Backtick code markers
- `|` table formatting

#### What Gets Transformed

| Pattern | Example | Becomes |
|---------|---------|---------|
| Chapter numbers | `Chapter 1:` | `Chapter One:` |
| Inline book citations | `(*A Treatise of Human Nature*, III.1.1)` | `(A Treatise of Human Nature, Book 3, Part 1, Section 1)` |
| Section symbols | `§125` | `section 125` |
| Akademie citations | `AK 4:402` | `Akademie edition, volume 4, page 402` |
| Year citations | `*A Theory of Justice* (1971)` | `A Theory of Justice, 1971` |
| Internal chapter refs | `(CH-05)` | `(Chapter 5)` |
| Position codes | `POS-M01` | `Position M-1` |
| Author placeholder | `[Author Name]` | Configured author name |
| Non-ASCII diacriticals | `karuṇā`, `mettā` | `karuna`, `metta` (stripped diacriticals) |
| CJK characters | `仁` | `ren` (with context from surrounding text) |

#### Blockquote Handling

Two patterns in the book:

**Epigraph (chapter-opening quote):**
```markdown
> *"The suffering of a conscious being matters."*
> --- The Axiom
```
Spoken as: [0.8s pause] "The suffering of a conscious being matters." [0.3s] "The Axiom." [0.8s pause]

**Inline quotation:**
```markdown
> *"Individual rationality leads to a worse outcome..."*
> --- Robert Axelrod, *The Evolution of Cooperation*
```
Spoken as: [0.8s pause] "Individual rationality leads to a worse outcome..." [0.3s] "Robert Axelrod, The Evolution of Cooperation." [0.8s pause]

No audible "quote/unquote" — the pauses and TTS prosody shift handle it naturally, matching professional audiobook conventions.

#### Table Handling

Tables in CH-46 and BACK_MATTER get special treatment:
- **CH-46 comparison table:** Converted to prose ("For Divine Command Theory, the core disagreement is...")
- **BACK_MATTER reference tables:** Skipped with note: "The Position Index, Glossary, and Thinkers Index are available in the printed edition."

#### Processing Order

Transformations run in this sequence to avoid conflicts:
1. Extract H1 as chapter title (remove from body)
2. Identify segment boundaries (rules, headers, blockquotes, paragraphs)
3. For each segment: strip blockquote markers → strip emphasis markers → transform citations → normalize Unicode → clean whitespace
4. Return ordered list of typed `TextSegment` objects

### 3. Audio Generation

**Architecture:** Segment-based generation, not one-giant-string.

```
TextSegment(type="book_announcement", text="Book One. Foundations. What Is Real?")
TextSegment(type="pause", duration=3.0)
TextSegment(type="chapter_title", text="Chapter One. The Third Way.")
TextSegment(type="pause", duration=2.0)
TextSegment(type="paragraph", text="We are heirs to a catastrophe...")
TextSegment(type="pause", duration=0.4)
TextSegment(type="section_header", text="The Ruins")
TextSegment(type="pause", duration=1.0)
...
```

Each text segment is fed to Kokoro's `KPipeline`, which returns audio at 24kHz. Silence segments are generated as zero-arrays. All segments for a chapter are concatenated into one audio file.

**Book announcements** are prepended to the first chapter of each Book section (not separate tracks). This matches professional audiobook conventions.

### 4. Output & Metadata

**File naming:** `00_TITLE_PAGE.mp3`, `01_PREFACE.mp3`, `02_CH-01.mp3`, ... `50_CH-48.mp3`, `51_BACK_MATTER.mp3`

**ID3 tags on every file:**
- Title: chapter title (e.g., "Chapter 1: The Third Way")
- Album: "The Manual of Harmonious Rationality"
- Artist / Album Artist: author name
- Track number: sequential
- Genre: "Philosophy"
- Year: 2026

### 5. Progress Tracking & Resume

A `progress.json` file in the output directory tracks:
- Which chapters are completed
- Which chapter is currently in progress
- Duration of each completed chapter

The `--resume` flag skips completed chapters, allowing the script to be stopped and restarted without losing work.

### 6. Manifest

After generation, a `manifest.json` is created with:
- Total duration and formatted time
- Voice and speed settings used
- Per-track metadata (title, file path, duration, word count)

### 7. Full Audiobook Combination

Optional `--combine` flag concatenates all chapter MP3s into a single `full_audiobook.mp3` with silence between chapters.

---

## CLI Interface

```
python generate_audiobook.py                    # Generate all chapters
python generate_audiobook.py --resume           # Resume from last checkpoint
python generate_audiobook.py --chapter CH-01    # Generate single chapter
python generate_audiobook.py --combine          # Combine existing chapters into one file
python generate_audiobook.py --voice af_heart   # Use different voice
python generate_audiobook.py --speed 1.0        # Override speed
python generate_audiobook.py --preview CH-01    # Show preprocessed text (no audio)
```

---

## Voice Options

| Voice | Description | Notes |
|-------|-------------|-------|
| `am_michael` | American male | **Recommended.** Clear, measured, authoritative. |
| `af_heart` | American female | Natural, warm. Good alternative. |
| `bf_emma` | British female | Some associate British accent with philosophical authority. |
| `am_adam` | American male (alt) | Another male option if Michael doesn't suit. |

The voice can be changed at any time and individual chapters regenerated.

---

## Edge Cases Handled

1. **CH-24 is 11,700 words** (3x average) — generator processes incrementally, no memory issues
2. **BACK_MATTER tables** — detected and handled specially (skip or convert to prose)
3. **TITLE_PAGE `[Author Name]`** — replaced from config
4. **Sanskrit/Pali/Chinese terms** (CH-45, CH-11) — diacriticals stripped, CJK replaced with romanization
5. **Nested emphasis** (`*"text"*`, `**bold *italic***`) — stripped in correct order
6. **Multi-line blockquotes** — `>` markers joined into single text block
7. **Numbered/bullet lists** — read naturally with pauses between items

---

## Estimated Output

| Metric | Value |
|--------|-------|
| Total chapters | 51 files (48 chapters + title + preface + back matter) |
| Total words | ~205,000 |
| Total audio | ~22-23 hours |
| Total file size | ~1.9 GB (MP3 192kbps) |
| Average chapter | ~27 minutes |
| Longest chapter | CH-24 (~78 minutes) |
| Shortest chapter | CH-47 (~17 minutes) |
| Generation time | ~15-20 minutes |
