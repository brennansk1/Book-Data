#!/usr/bin/env python3
"""
Audiobook Generation Pipeline for The Manual of Harmonious Rationality

Dependencies:
    System: espeak-ng, ffmpeg
        brew install espeak-ng ffmpeg

    Python (shared, both engines):
        pip3 install soundfile numpy pydub mutagen

    Python (Kokoro engine, --engine kokoro):
        pip3 install kokoro

    Python (Miso engine, --engine miso, DEFAULT):
        Needs a Python 3.10 environment (system Python here is 3.9) and the
        MisoLabsAI/MisoTTS repo cloned to ./MisoTTS with its dependencies
        installed (torch, torchaudio, moshi, torchtune, torchao, transformers,
        tokenizers, huggingface_hub, silentcipher). See
        Revision/AUDIOBOOK_MISO_SETUP.md for the full step-by-step setup,
        performance expectations on Apple Silicon, and memory guidance.

Usage:
    python3 generate_audiobook.py                       # Generate all chapters (Miso engine)
    python3 generate_audiobook.py --engine kokoro        # Use the legacy Kokoro engine instead
    python3 generate_audiobook.py --smoke-test           # Load model, synthesize 1 sentence, exit
    python3 generate_audiobook.py --device cpu --smoke-test   # Force CPU (skip MPS) for the smoke test
    python3 generate_audiobook.py --resume               # Resume from last checkpoint
    python3 generate_audiobook.py --chapter CH-01         # Generate single chapter
    python3 generate_audiobook.py --combine              # Combine existing chapters
    python3 generate_audiobook.py --voice af_heart --engine kokoro   # Kokoro voice override
    python3 generate_audiobook.py --speed 1.0 --engine kokoro        # Kokoro speed override
    python3 generate_audiobook.py --preview CH-01        # Preview preprocessing
"""

import os
import re
import sys
import json
import argparse
import unicodedata
import time
from collections import deque
from dataclasses import dataclass, field
from typing import List, Optional

import numpy as np
import soundfile as sf
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, TRCK, TCON, TDRC

# ============================================================
# CONFIGURATION
# ============================================================

PROJECT_DIR = "/Users/brennankelley/Desktop/Projects/Book-Data-main"
CHAPTERS_DIR = os.path.join(PROJECT_DIR, "Book", "Chapters")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "Audiobook")
PROGRESS_FILE = os.path.join(OUTPUT_DIR, "progress.json")
MANIFEST_FILE = os.path.join(OUTPUT_DIR, "manifest.json")

# Engine selection
DEFAULT_ENGINE = "miso"

# Kokoro audio settings
VOICE = "am_michael"
SPEED = 0.92
SAMPLE_RATE = 24000  # Kokoro's fixed output sample rate
MP3_BITRATE = "192k"

# Miso (MisoTTS / Sesame CSM 8B) settings
MISO_REPO_DIR = os.path.join(PROJECT_DIR, "MisoTTS")
MISO_MODEL_REPO_ID = "MisoLabs/MisoTTS"
MISO_SPEAKER_ID = 0
# MisoTTS shares one 2048-token sequence budget between text and audio tokens,
# so each synthesis call must cover only a small amount of text. We split each
# paragraph into sentence groups capped at this many characters.
MISO_CHUNK_MAX_CHARS = 200
# Rolling context window: number of previously generated (text, audio) segments
# fed back into each generate() call so the voice stays consistent across a
# chapter. Reset at chapter boundaries.
MISO_CONTEXT_SEGMENTS = 3
# max_audio_length_ms heuristic: ~90ms of audio per character of input text,
# plus a fixed headroom buffer, capped at 30 seconds per chunk.
MISO_MS_PER_CHAR = 90
MISO_MS_HEADROOM = 2000
MISO_MAX_AUDIO_MS = 30_000
MISO_TEMPERATURE = 0.9
MISO_TOPK = 50
# Optional voice cloning: path to a reference WAV + the exact transcript of
# what is said in it. If set, this becomes a permanent first context segment
# on every generate() call (in addition to the rolling window above).
REFERENCE_VOICE_WAV = None
REFERENCE_VOICE_TRANSCRIPT = None

# Metadata
BOOK_TITLE = "The Manual of Harmonious Rationality"
BOOK_AUTHOR = "Brennan Kelley"
BOOK_YEAR = "2026"
BOOK_GENRE = "Philosophy"

# Pause durations (seconds)
PAUSE_BOOK_ANNOUNCEMENT = 3.0
PAUSE_CHAPTER_START = 2.0
PAUSE_SECTION_BREAK = 1.5
PAUSE_HEADER = 1.0
PAUSE_SUBHEADER = 0.7
PAUSE_BLOCKQUOTE_BEFORE = 0.8
PAUSE_BLOCKQUOTE_AFTER = 0.8
PAUSE_PARAGRAPH = 0.4
PAUSE_LIST_ITEM = 0.3
PAUSE_CHAPTER_END = 3.0

# Book structure (mirrors build_book.py)
BOOK_ORDER = [
    ("front", "TITLE_PAGE.md"),
    ("front", "PREFACE.md"),
    ("book", "Book One. Foundations. What Is Real?"),
    ("ch", "CH-01.md"), ("ch", "CH-02.md"), ("ch", "CH-03.md"),
    ("ch", "CH-04.md"), ("ch", "CH-05.md"),
    ("book", "Book Two. The Enemy. Why Suffering Persists."),
    ("ch", "CH-06.md"), ("ch", "CH-07.md"), ("ch", "CH-08.md"),
    ("book", "Book Three. The Moral Architecture. How to Decide."),
    ("ch", "CH-09.md"), ("ch", "CH-10.md"), ("ch", "CH-11.md"), ("ch", "CH-12.md"),
    ("book", "Book Four. Personal Ethics. Living the System."),
    ("ch", "CH-13.md"), ("ch", "CH-14.md"), ("ch", "CH-15.md"), ("ch", "CH-16.md"),
    ("book", "Book Five. Political Philosophy. Engineering the State."),
    ("ch", "CH-17.md"), ("ch", "CH-18.md"), ("ch", "CH-19.md"), ("ch", "CH-20.md"),
    ("ch", "CH-21.md"), ("ch", "CH-22.md"), ("ch", "CH-23.md"), ("ch", "CH-24.md"),
    ("ch", "CH-25.md"),
    ("book", "Book Six. Economic Philosophy. The Machinery of Prosperity."),
    ("ch", "CH-26.md"), ("ch", "CH-27.md"), ("ch", "CH-28.md"),
    ("ch", "CH-29.md"), ("ch", "CH-30.md"), ("ch", "CH-31.md"),
    ("book", "Book Seven. The Frontier. Problems at the Edge."),
    ("ch", "CH-32.md"), ("ch", "CH-33.md"), ("ch", "CH-34.md"),
    ("ch", "CH-35.md"), ("ch", "CH-36.md"),
    ("book", "Book Eight. Defense. Defeating Rival Systems."),
    ("ch", "CH-37.md"), ("ch", "CH-38.md"), ("ch", "CH-39.md"), ("ch", "CH-40.md"),
    ("ch", "CH-41.md"), ("ch", "CH-42.md"), ("ch", "CH-43.md"), ("ch", "CH-44.md"),
    ("ch", "CH-45.md"), ("ch", "CH-46.md"),
    ("book", "Book Nine. Synthesis."),
    ("ch", "CH-47.md"), ("ch", "CH-48.md"), ("ch", "CH-49.md"),
    ("front", "BACK_MATTER.md"),
]

# Number words for chapter announcements
NUM_WORDS = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
    11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
    15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
    19: "Nineteen", 20: "Twenty", 21: "Twenty-One", 22: "Twenty-Two",
    23: "Twenty-Three", 24: "Twenty-Four", 25: "Twenty-Five",
    26: "Twenty-Six", 27: "Twenty-Seven", 28: "Twenty-Eight",
    29: "Twenty-Nine", 30: "Thirty", 31: "Thirty-One", 32: "Thirty-Two",
    33: "Thirty-Three", 34: "Thirty-Four", 35: "Thirty-Five",
    36: "Thirty-Six", 37: "Thirty-Seven", 38: "Thirty-Eight",
    39: "Thirty-Nine", 40: "Forty", 41: "Forty-One", 42: "Forty-Two",
    43: "Forty-Three", 44: "Forty-Four", 45: "Forty-Five",
    46: "Forty-Six", 47: "Forty-Seven", 48: "Forty-Eight",
    49: "Forty-Nine",
}

# Non-ASCII replacements
UNICODE_REPLACEMENTS = {
    "仁": "ren",       # 仁
    "karuṇā": "karuna",
    "mettā": "metta",
    "pratītyasamutpāda": "pratitya samutpada",
    "telē": "tele",
    "dukkha": "dukkha",
    "eudaimonia": "eudaimonia",
}


# ============================================================
# TEXT SEGMENTS
# ============================================================

@dataclass
class TextSegment:
    seg_type: str  # "paragraph", "pause", "chapter_title", "section_header",
                   # "subheader", "blockquote", "attribution", "book_announcement"
    text: str = ""
    duration: float = 0.0


# ============================================================
# TEXT PREPROCESSING
# ============================================================

class MarkdownCleaner:
    """Transforms raw markdown into speech-ready TextSegment lists."""

    def process_file(self, filepath: str) -> List[TextSegment]:
        with open(filepath, 'r') as f:
            raw = f.read()

        segments = []
        lines = raw.split('\n')

        # Extract H1 title
        title_text = ""
        body_start = 0
        for i, line in enumerate(lines):
            if line.startswith('# '):
                title_text = line[2:].strip()
                body_start = i + 1
                break

        # Build chapter title announcement
        if title_text:
            spoken_title = self._make_spoken_title(title_text)
            segments.append(TextSegment("chapter_title", spoken_title))
            segments.append(TextSegment("pause", duration=PAUSE_CHAPTER_START))

        # Process body
        body = '\n'.join(lines[body_start:])
        segments.extend(self._process_body(body))

        # End-of-chapter silence
        segments.append(TextSegment("pause", duration=PAUSE_CHAPTER_END))

        return segments

    def _make_spoken_title(self, title: str) -> str:
        # Convert "Chapter 24: Political Policy Evaluation — How to Think..."
        # to "Chapter Twenty-Four. Political Policy Evaluation. How to Think..."
        title = title.replace(' — ', '. ').replace(' -- ', '. ')

        # Convert chapter number to words
        m = re.match(r'Chapter (\d+):\s*(.*)', title)
        if m:
            num = int(m.group(1))
            rest = m.group(2)
            word = NUM_WORDS.get(num, str(num))
            title = f"Chapter {word}. {rest}"

        return title

    def _process_body(self, body: str) -> List[TextSegment]:
        segments = []
        # Split on horizontal rules first
        sections = re.split(r'\n---+\n', body)

        for i, section in enumerate(sections):
            if i > 0:
                segments.append(TextSegment("pause", duration=PAUSE_SECTION_BREAK))

            section = section.strip()
            if not section:
                continue

            # Process paragraphs within each section
            paragraphs = re.split(r'\n\n+', section)
            for para in paragraphs:
                para = para.strip()
                if not para:
                    continue

                # Check for headers
                if para.startswith('## '):
                    header_text = para[3:].strip()
                    header_text = self._clean_text(header_text)
                    segments.append(TextSegment("pause", duration=PAUSE_HEADER))
                    segments.append(TextSegment("section_header", header_text))
                    segments.append(TextSegment("pause", duration=PAUSE_HEADER))
                elif para.startswith('### '):
                    header_text = para[4:].strip()
                    header_text = self._clean_text(header_text)
                    segments.append(TextSegment("pause", duration=PAUSE_SUBHEADER))
                    segments.append(TextSegment("subheader", header_text))
                    segments.append(TextSegment("pause", duration=PAUSE_SUBHEADER))
                elif para.startswith('> '):
                    # Blockquote
                    segments.extend(self._process_blockquote(para))
                elif re.match(r'^\|', para):
                    # Table — skip with note
                    segments.append(TextSegment("paragraph",
                        "The following table is available in the printed edition."))
                    segments.append(TextSegment("pause", duration=PAUSE_PARAGRAPH))
                else:
                    # Regular paragraph (may contain lists)
                    cleaned = self._clean_text(para)
                    if cleaned:
                        segments.append(TextSegment("paragraph", cleaned))
                        segments.append(TextSegment("pause", duration=PAUSE_PARAGRAPH))

        return segments

    def _process_blockquote(self, block: str) -> List[TextSegment]:
        segments = [TextSegment("pause", duration=PAUSE_BLOCKQUOTE_BEFORE)]

        lines = block.split('\n')
        quote_lines = []
        attribution = ""

        for line in lines:
            line = line.strip()
            if line.startswith('> '):
                content = line[2:].strip()
                # Check for attribution line
                if content.startswith('--- ') or content.startswith('— '):
                    attribution = content.lstrip('-— ').strip()
                else:
                    quote_lines.append(content)
            elif line.startswith('>'):
                content = line[1:].strip()
                if content.startswith('--- ') or content.startswith('— '):
                    attribution = content.lstrip('-— ').strip()
                else:
                    quote_lines.append(content)

        quote_text = ' '.join(quote_lines)
        quote_text = self._clean_text(quote_text)
        if quote_text:
            segments.append(TextSegment("blockquote", quote_text))

        if attribution:
            attribution = self._clean_text(attribution)
            segments.append(TextSegment("attribution", attribution))

        segments.append(TextSegment("pause", duration=PAUSE_BLOCKQUOTE_AFTER))
        return segments

    def _clean_text(self, text: str) -> str:
        # Join lines within a paragraph
        text = re.sub(r'\n', ' ', text)

        # Strip markdown emphasis (order matters: *** before ** before *)
        text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', text)
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        # Italic: be careful not to strip bullet asterisks
        text = re.sub(r'(?<!\s)\*([^*\n]+?)\*(?!\s*$)', r'\1', text)
        text = re.sub(r'\*([^*\n]+?)\*', r'\1', text)

        # Strip backtick code markers
        text = re.sub(r'`([^`]+)`', r'\1', text)

        # Transform citations
        text = self._transform_citations(text)

        # Replace [Author Name] placeholder
        text = text.replace('[Author Name]', BOOK_AUTHOR)

        # Handle non-ASCII
        text = self._handle_unicode(text)

        # Clean up numbered lists: "1. **bold text**" -> "One. bold text"
        text = re.sub(r'^(\d+)\.\s+', lambda m: f"{NUM_WORDS.get(int(m.group(1)), m.group(1))}. ", text)

        # Clean bullet lists
        text = re.sub(r'^[-*]\s+', '', text, flags=re.MULTILINE)

        # Clean up whitespace
        text = re.sub(r'\s+', ' ', text).strip()

        # Ensure em-dashes have spaces for natural TTS pacing
        text = text.replace('--', ' -- ')
        text = text.replace('—', ' -- ')
        text = re.sub(r'\s+', ' ', text)

        return text

    def _transform_citations(self, text: str) -> str:
        # Section symbols: §125 -> section 125
        text = re.sub(r'§(\d+)', r'section \1', text)

        # Akademie citations: AK 4:402 -> Akademie edition, volume 4, page 402
        text = re.sub(r'AK\s+(\d+):(\d+)',
                       r'Akademie edition, volume \1, page \2', text)

        # Internal chapter refs: (CH-05) -> (Chapter 5)
        text = re.sub(r'\(CH-(\d+)\)', lambda m: f'(Chapter {int(m.group(1))})', text)
        text = re.sub(r'CH-(\d+)', lambda m: f'Chapter {int(m.group(1))}', text)

        # Position codes: POS-M01 -> Position M-1
        text = re.sub(r'POS-([A-Z]+)(\d+)',
                       lambda m: f'Position {m.group(1)}-{int(m.group(2))}', text)

        # Book citations with Roman numeral locations
        # (*Title*, III.1.1) -> (Title, Book 3, Part 1, Section 1)
        def roman_to_int(s):
            vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
            result = 0
            for i, c in enumerate(s):
                if i + 1 < len(s) and vals.get(c, 0) < vals.get(s[i+1], 0):
                    result -= vals.get(c, 0)
                else:
                    result += vals.get(c, 0)
            return result

        def citation_repl(m):
            title = m.group(1)
            loc = m.group(2)
            parts = loc.split('.')
            if len(parts) >= 2 and re.match(r'^[IVXLC]+$', parts[0]):
                book_num = roman_to_int(parts[0])
                rest = ', '.join(f'section {p}' for p in parts[1:])
                return f'({title}, Book {book_num}, {rest})'
            return f'({title}, {loc})'

        text = re.sub(r'\(([^)]+?),\s*([IVXLC]+(?:\.\d+)+)\)', citation_repl, text)

        return text

    def _handle_unicode(self, text: str) -> str:
        # Specific replacements
        for old, new in UNICODE_REPLACEMENTS.items():
            text = text.replace(old, new)

        # Strip combining diacriticals from remaining text
        normalized = unicodedata.normalize('NFD', text)
        stripped = ''.join(c for c in normalized
                         if unicodedata.category(c) != 'Mn')
        return stripped


# ============================================================
# MISO TEXT CHUNKING
# ============================================================

_SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])\s+')


def chunk_text_for_miso(text: str, max_chars: int = MISO_CHUNK_MAX_CHARS) -> List[str]:
    """Split text into sentence-group chunks of at most ~max_chars characters.

    MisoTTS shares a single 2048-token sequence budget between the rolling
    context, the input text, and the generated audio tokens, so long
    paragraphs must be fed to generate() a few sentences at a time.
    """
    text = text.strip()
    if not text:
        return []

    sentences = [s.strip() for s in _SENTENCE_SPLIT_RE.split(text) if s.strip()]
    if not sentences:
        return [text] if len(text) <= max_chars else _hard_split(text, max_chars)

    chunks = []
    current = ""
    for sentence in sentences:
        candidate = f"{current} {sentence}".strip() if current else sentence
        if not current or len(candidate) <= max_chars:
            current = candidate
        else:
            chunks.append(current)
            current = sentence

    if current:
        chunks.append(current)

    # Guard against any single "sentence" (e.g. a run-on with no punctuation)
    # still being far too long for one generate() call.
    final_chunks = []
    for chunk in chunks:
        if len(chunk) <= max_chars * 1.5:
            final_chunks.append(chunk)
        else:
            final_chunks.extend(_hard_split(chunk, max_chars))
    return final_chunks


def _hard_split(text: str, max_chars: int) -> List[str]:
    """Fallback word-boundary split for text with no sentence punctuation."""
    words = text.split(' ')
    chunks = []
    current = ""
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


def miso_max_audio_ms(text: str) -> int:
    """Adaptive max_audio_length_ms: ~90ms/char + 2s headroom, capped at 30s."""
    return min(MISO_MAX_AUDIO_MS, int(len(text) * MISO_MS_PER_CHAR) + MISO_MS_HEADROOM)


# ============================================================
# AUDIO GENERATION -- KOKORO (fallback engine)
# ============================================================

class AudioGenerator:
    """Legacy Kokoro TTS engine. Kept as a fallback via --engine kokoro."""

    def __init__(self, voice: str, speed: float):
        print("  Initializing Kokoro TTS pipeline...")
        from kokoro import KPipeline
        self.pipeline = KPipeline(lang_code='a')
        self.voice = voice
        self.speed = speed
        self.sample_rate = SAMPLE_RATE
        print(f"  Voice: {voice}, Speed: {speed}")

    def generate_chapter_audio(self, segments: List[TextSegment]) -> np.ndarray:
        audio_parts = []
        for seg in segments:
            if seg.seg_type == "pause":
                audio_parts.append(self._silence(seg.duration))
            elif seg.text.strip():
                audio = self._synthesize(seg.text)
                if audio is not None and len(audio) > 0:
                    audio_parts.append(audio)
        if not audio_parts:
            return np.zeros(self.sample_rate, dtype=np.float32)
        return np.concatenate(audio_parts)

    def _synthesize(self, text: str) -> Optional[np.ndarray]:
        chunks = []
        try:
            for gs, ps, audio in self.pipeline(
                text, voice=self.voice, speed=self.speed
            ):
                if audio is not None:
                    chunks.append(audio)
        except Exception as e:
            print(f"    WARNING: TTS error on text segment: {e}")
            print(f"    Text: {text[:80]}...")
            return None
        if chunks:
            return np.concatenate(chunks)
        return None

    def _silence(self, seconds: float) -> np.ndarray:
        return np.zeros(int(self.sample_rate * seconds), dtype=np.float32)


# ============================================================
# AUDIO GENERATION -- MISO TTS (default engine)
# ============================================================

class MisoAudioGenerator:
    """MisoTTS (Sesame CSM-style 8B backbone + Mimi codec) TTS engine.

    Loads the MisoLabsAI/MisoTTS inference code from MISO_REPO_DIR, picks the
    best available device (cuda > mps > cpu), and loads weights in bfloat16
    (required to fit the ~16GB model in 24GB of unified memory on an M-series
    Mac). Text is chunked to respect the model's 2048-token sequence budget,
    and a rolling window of previously generated segments is fed back in as
    `context` on every call so the voice stays consistent across a chapter.
    """

    def __init__(self, device: Optional[str] = None,
                 model_path_or_repo_id: str = MISO_MODEL_REPO_ID,
                 speaker: int = MISO_SPEAKER_ID,
                 reference_voice_wav: Optional[str] = None,
                 reference_transcript: Optional[str] = None,
                 temperature: float = MISO_TEMPERATURE,
                 topk: int = MISO_TOPK):
        print("  Initializing Miso TTS (Sesame-CSM-style 8B) pipeline...")

        if MISO_REPO_DIR not in sys.path:
            sys.path.insert(0, MISO_REPO_DIR)

        try:
            import torch
        except ImportError as e:
            raise RuntimeError(
                "The 'miso' engine requires torch/torchaudio and the MisoTTS "
                "repo's dependencies to be installed. See "
                "Revision/AUDIOBOOK_MISO_SETUP.md, or use --engine kokoro."
            ) from e

        self._torch = torch
        self.speaker = speaker
        self.temperature = temperature
        self.topk = topk
        self.model_path_or_repo_id = model_path_or_repo_id

        requested_device = device or self._detect_device()
        self.device = requested_device
        self.generator = self._load_generator(requested_device)
        self.sample_rate = self.generator.sample_rate
        print(f"  Device: {self.device} | Sample rate: {self.sample_rate} Hz | "
              f"Model: {model_path_or_repo_id}")

        # Rolling context of the last N generated (text, audio) segments.
        self.context_window = deque(maxlen=MISO_CONTEXT_SEGMENTS)

        # Optional permanent voice-cloning reference segment.
        self.reference_segment = None
        if reference_voice_wav:
            if not reference_transcript:
                raise ValueError(
                    "REFERENCE_VOICE_WAV is set but no matching transcript was "
                    "provided. MisoTTS conditions on the (text, audio) pair, so "
                    "an inaccurate transcript will degrade voice cloning. Pass "
                    "--reference-transcript with the exact words spoken in the "
                    "reference clip."
                )
            self.reference_segment = self._load_reference_segment(
                reference_voice_wav, reference_transcript)

    def _detect_device(self) -> str:
        torch = self._torch
        if torch.cuda.is_available():
            return "cuda"
        mps_backend = getattr(torch.backends, "mps", None)
        if mps_backend is not None and mps_backend.is_available():
            return "mps"
        return "cpu"

    def _load_generator(self, device: str):
        from generator import load_miso_8b
        torch = self._torch
        try:
            return load_miso_8b(
                device=device,
                model_path_or_repo_id=self.model_path_or_repo_id,
                dtype=torch.bfloat16,
            )
        except Exception as e:
            if device == "mps":
                # MisoTTS's own run_misotts.py explicitly skips MPS "due to
                # float64 limitations" (the SilentCipher watermarker and/or
                # Mimi codec use ops MPS doesn't support). Fall back to CPU
                # rather than hard-failing.
                print(f"  WARNING: Failed to load Miso TTS on MPS ({e}).")
                print("  MisoTTS's reference script deliberately avoids MPS for "
                      "this reason. Falling back to CPU -- this will be much "
                      "slower. Pass --device cpu to skip this retry next time.")
                self.device = "cpu"
                return load_miso_8b(
                    device="cpu",
                    model_path_or_repo_id=self.model_path_or_repo_id,
                    dtype=torch.bfloat16,
                )
            raise

    def _load_reference_segment(self, wav_path: str, transcript: str):
        import torchaudio
        from generator import Segment

        audio, sr = torchaudio.load(wav_path)
        if audio.ndim > 1:
            audio = audio.mean(dim=0)
        audio = torchaudio.functional.resample(audio, orig_freq=sr, new_freq=self.sample_rate)
        return Segment(speaker=self.speaker, text=transcript, audio=audio)

    def generate_chapter_audio(self, segments: List[TextSegment]) -> np.ndarray:
        # Reset voice-consistency context at each chapter boundary.
        self.context_window.clear()

        audio_parts = []
        for seg in segments:
            if seg.seg_type == "pause":
                audio_parts.append(self._silence(seg.duration))
            elif seg.text.strip():
                audio = self._synthesize(seg.text)
                if audio is not None and len(audio) > 0:
                    audio_parts.append(audio)
        if not audio_parts:
            return np.zeros(self.sample_rate, dtype=np.float32)
        return np.concatenate(audio_parts)

    def _synthesize(self, text: str) -> Optional[np.ndarray]:
        chunks = chunk_text_for_miso(text, MISO_CHUNK_MAX_CHARS)
        audio_pieces = []
        for chunk in chunks:
            audio = self._generate_one(chunk)
            if audio is not None:
                audio_pieces.append(audio)
        if not audio_pieces:
            return None
        return np.concatenate(audio_pieces)

    def _generate_one(self, text: str) -> Optional[np.ndarray]:
        from generator import Segment

        max_ms = miso_max_audio_ms(text)
        context = list(self.context_window)
        if self.reference_segment is not None:
            context = [self.reference_segment] + context

        try:
            audio_tensor = self.generator.generate(
                text=text,
                speaker=self.speaker,
                context=context,
                max_audio_length_ms=max_ms,
                temperature=self.temperature,
                topk=self.topk,
            )
        except Exception as e:
            msg = str(e).lower()
            mps_related = self.device == "mps" and (
                "float64" in msg or "mps" in msg or "not implemented" in msg
            )
            if mps_related:
                print(f"    WARNING: MPS runtime error, falling back to CPU for "
                      f"the rest of this run: {e}")
                try:
                    self.generator = self._load_generator("cpu")
                    self.device = "cpu"
                    self.sample_rate = self.generator.sample_rate
                    audio_tensor = self.generator.generate(
                        text=text,
                        speaker=self.speaker,
                        context=context,
                        max_audio_length_ms=max_ms,
                        temperature=self.temperature,
                        topk=self.topk,
                    )
                except Exception as e2:
                    print(f"    WARNING: TTS error on text segment (after CPU "
                          f"fallback): {e2}")
                    print(f"    Text: {text[:80]}...")
                    return None
            else:
                print(f"    WARNING: TTS error on text segment: {e}")
                print(f"    Text: {text[:80]}...")
                return None

        self.context_window.append(
            Segment(speaker=self.speaker, text=text, audio=audio_tensor))

        return audio_tensor.detach().to(self._torch.float32).cpu().numpy()

    def _silence(self, seconds: float) -> np.ndarray:
        return np.zeros(int(self.sample_rate * seconds), dtype=np.float32)


def build_generator(args):
    if args.engine == "kokoro":
        return AudioGenerator(args.voice, args.speed)
    return MisoAudioGenerator(
        device=args.device,
        model_path_or_repo_id=args.miso_model,
        speaker=args.speaker,
        reference_voice_wav=args.reference_voice or REFERENCE_VOICE_WAV,
        reference_transcript=args.reference_transcript or REFERENCE_VOICE_TRANSCRIPT,
        temperature=args.temperature,
        topk=args.topk,
    )


# ============================================================
# PROGRESS TRACKING
# ============================================================

class ProgressTracker:
    """Tracks completed chapters per engine.

    progress.json predates the engine flag: it holds a flat dict of
    chapter_id -> completion record, all implicitly produced by Kokoro.
    Rather than requiring users to delete it when switching engines, new
    (non-Kokoro) completions are stored under an engine-namespaced key
    ("CH-01::miso") so they can never collide with -- or silently overwrite
    -- the legacy bare-chapter_id Kokoro entries ("CH-01"). This means
    --resume --engine kokoro keeps working exactly as before, while
    --resume --engine miso tracks its own progress independently and
    regenerates chapters that were only ever produced by Kokoro.
    """

    def __init__(self, path: str, engine: str):
        self.path = path
        self.engine = engine
        self.state = self._load()

    def _load(self) -> dict:
        if os.path.exists(self.path):
            with open(self.path) as f:
                return json.load(f)
        return {"completed": {}, "in_progress": None}

    def _save(self):
        with open(self.path, 'w') as f:
            json.dump(self.state, f, indent=2)

    def _key(self, chapter_id: str) -> str:
        # Kokoro keeps the legacy bare key for backward compatibility;
        # every other engine gets its own namespaced key.
        return chapter_id if self.engine == "kokoro" else f"{chapter_id}::{self.engine}"

    def is_completed(self, chapter_id: str) -> bool:
        if self._key(chapter_id) in self.state["completed"]:
            return True
        # Legacy entries (pre-engine-tagging) are all Kokoro output.
        if self.engine == "kokoro" and chapter_id in self.state["completed"]:
            return True
        return False

    def mark_started(self, chapter_id: str):
        self.state["in_progress"] = {"chapter": chapter_id, "engine": self.engine}
        self._save()

    def mark_completed(self, chapter_id: str, duration: float):
        self.state["completed"][self._key(chapter_id)] = {
            "chapter": chapter_id,
            "duration_seconds": round(duration, 1),
            "completed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "engine": self.engine,
        }
        self.state["in_progress"] = None
        self._save()


# ============================================================
# OUTPUT & TAGGING
# ============================================================

def save_chapter_mp3(audio: np.ndarray, chapter_id: str, title: str,
                     track_num: int, sample_rate: int = SAMPLE_RATE) -> str:
    wav_dir = os.path.join(OUTPUT_DIR, "wav")
    mp3_dir = os.path.join(OUTPUT_DIR, "mp3")
    os.makedirs(wav_dir, exist_ok=True)
    os.makedirs(mp3_dir, exist_ok=True)

    wav_path = os.path.join(wav_dir, f"{track_num:02d}_{chapter_id}.wav")
    mp3_path = os.path.join(mp3_dir, f"{track_num:02d}_{chapter_id}.mp3")

    sf.write(wav_path, audio, sample_rate)

    seg = AudioSegment.from_wav(wav_path)
    seg.export(mp3_path, format="mp3", bitrate=MP3_BITRATE)

    # ID3 tags
    audio_file = MP3(mp3_path)
    audio_file.tags = ID3()
    audio_file.tags.add(TIT2(encoding=3, text=title))
    audio_file.tags.add(TALB(encoding=3, text=BOOK_TITLE))
    audio_file.tags.add(TPE1(encoding=3, text=BOOK_AUTHOR))
    audio_file.tags.add(TPE2(encoding=3, text=BOOK_AUTHOR))
    audio_file.tags.add(TRCK(encoding=3, text=str(track_num)))
    audio_file.tags.add(TCON(encoding=3, text=BOOK_GENRE))
    audio_file.tags.add(TDRC(encoding=3, text=BOOK_YEAR))
    audio_file.save()

    return mp3_path


def format_duration(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


# ============================================================
# MANIFEST
# ============================================================

def generate_manifest(tracker: ProgressTracker, engine: str, sample_rate: int,
                      voice: Optional[str] = None, speed: Optional[float] = None):
    tracks = []
    total_duration = 0

    mp3_dir = os.path.join(OUTPUT_DIR, "mp3")
    for f in sorted(os.listdir(mp3_dir)):
        if f.endswith('.mp3'):
            mp3_path = os.path.join(mp3_dir, f)
            audio = MP3(mp3_path)
            dur = audio.info.length
            total_duration += dur
            tracks.append({
                "file": f,
                "duration_seconds": round(dur, 1),
                "duration_formatted": format_duration(dur),
            })

    manifest = {
        "title": BOOK_TITLE,
        "author": BOOK_AUTHOR,
        "engine": engine,
        "voice": voice,
        "speed": speed,
        "sample_rate": sample_rate,
        "total_duration_seconds": round(total_duration, 1),
        "total_duration_formatted": format_duration(total_duration),
        "total_tracks": len(tracks),
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "tracks": tracks,
    }

    with open(MANIFEST_FILE, 'w') as f:
        json.dump(manifest, f, indent=2)

    print(f"\n  Manifest: {MANIFEST_FILE}")
    print(f"  Total: {format_duration(total_duration)} across {len(tracks)} tracks")


# ============================================================
# COMBINE
# ============================================================

def combine_audiobook():
    mp3_dir = os.path.join(OUTPUT_DIR, "mp3")
    files = sorted(f for f in os.listdir(mp3_dir) if f.endswith('.mp3'))

    if not files:
        print("No MP3 files found to combine.")
        return

    print(f"Combining {len(files)} tracks...")
    combined = AudioSegment.empty()
    for f in files:
        print(f"  Adding {f}...")
        seg = AudioSegment.from_mp3(os.path.join(mp3_dir, f))
        combined += seg
        combined += AudioSegment.silent(duration=int(PAUSE_CHAPTER_END * 1000))

    out_path = os.path.join(OUTPUT_DIR, "full_audiobook.mp3")
    print(f"Exporting to {out_path}...")
    combined.export(out_path, format="mp3", bitrate=MP3_BITRATE)
    size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"Done! Full audiobook: {size_mb:.0f} MB")


# ============================================================
# PREVIEW
# ============================================================

def preview_chapter(chapter_id: str):
    filepath = os.path.join(CHAPTERS_DIR, f"{chapter_id}.md")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    cleaner = MarkdownCleaner()
    segments = cleaner.process_file(filepath)

    print(f"\n{'='*60}")
    print(f"PREVIEW: {chapter_id}")
    print(f"{'='*60}\n")

    for seg in segments:
        if seg.seg_type == "pause":
            print(f"  [PAUSE {seg.duration}s]")
        else:
            label = seg.seg_type.upper()
            text = seg.text[:120] + "..." if len(seg.text) > 120 else seg.text
            print(f"  [{label}] {text}")

    text_segs = [s for s in segments if s.seg_type != "pause"]
    total_words = sum(len(s.text.split()) for s in text_segs)
    print(f"\n  Total segments: {len(segments)}")
    print(f"  Text segments: {len(text_segs)}")
    print(f"  Total words: {total_words}")
    print(f"  Estimated duration: ~{format_duration(total_words / 150 * 60)}")


# ============================================================
# SMOKE TEST
# ============================================================

def run_smoke_test(args):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\n{'='*60}")
    print(f"  SMOKE TEST -- engine={args.engine}")
    print(f"{'='*60}\n")

    t_start = time.time()
    generator = build_generator(args)
    load_elapsed = time.time() - t_start
    print(f"\n  Model loaded in {format_duration(load_elapsed)} "
          f"({load_elapsed:.1f}s)")

    text = "This is a smoke test of the audiobook narration pipeline."
    print(f"  Synthesizing: \"{text}\"")

    t_gen = time.time()
    audio = generator._synthesize(text)
    gen_elapsed = time.time() - t_gen

    if audio is None or len(audio) == 0:
        print("\n  FAILED: no audio was produced. See warnings above.")
        sys.exit(1)

    out_path = os.path.join(OUTPUT_DIR, "smoke_test.wav")
    sf.write(out_path, audio, generator.sample_rate)
    audio_seconds = len(audio) / generator.sample_rate

    print(f"\n  Generated {audio_seconds:.2f}s of audio in "
          f"{format_duration(gen_elapsed)} ({gen_elapsed:.1f}s)")
    print(f"  Realtime factor: {gen_elapsed / audio_seconds:.2f}x "
          f"(> 1.0 means slower than realtime)")
    print(f"  Wrote: {out_path}")
    print(f"  Total time (load + generate): "
          f"{format_duration(time.time() - t_start)}")
    print("\nSmoke test complete. Listen to smoke_test.wav to confirm the "
          "voice and setup are what you expect before running a full chapter.")


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Generate audiobook")
    parser.add_argument("--engine", choices=["miso", "kokoro"], default=DEFAULT_ENGINE,
                        help=f"TTS engine to use (default: {DEFAULT_ENGINE})")
    parser.add_argument("--resume", action="store_true",
                        help="Resume from last checkpoint")
    parser.add_argument("--chapter", type=str,
                        help="Generate single chapter (e.g., CH-01)")
    parser.add_argument("--combine", action="store_true",
                        help="Combine existing chapters into full audiobook")
    parser.add_argument("--voice", type=str, default=VOICE,
                        help=f"Kokoro voice to use (default: {VOICE})")
    parser.add_argument("--speed", type=float, default=SPEED,
                        help=f"Kokoro speed (default: {SPEED})")
    parser.add_argument("--preview", type=str,
                        help="Preview preprocessing for chapter")
    parser.add_argument("--smoke-test", action="store_true",
                        help="Load the model, synthesize one sentence to "
                             "Audiobook/smoke_test.wav, print timing, and exit")

    # Miso-specific options
    parser.add_argument("--device", type=str, default=None,
                        choices=["cuda", "mps", "cpu"],
                        help="Override device for the miso engine "
                             "(default: auto-detect cuda > mps > cpu)")
    parser.add_argument("--miso-model", type=str, default=MISO_MODEL_REPO_ID,
                        help="Miso model path or HF repo id "
                             f"(default: {MISO_MODEL_REPO_ID})")
    parser.add_argument("--speaker", type=int, default=MISO_SPEAKER_ID,
                        help=f"Miso speaker id (default: {MISO_SPEAKER_ID})")
    parser.add_argument("--reference-voice", type=str, default=None,
                        help="Path to a reference WAV for Miso voice cloning "
                             "(overrides REFERENCE_VOICE_WAV)")
    parser.add_argument("--reference-transcript", type=str, default=None,
                        help="Exact transcript of --reference-voice audio "
                             "(required if --reference-voice is set)")
    parser.add_argument("--temperature", type=float, default=MISO_TEMPERATURE,
                        help=f"Miso sampling temperature (default: {MISO_TEMPERATURE})")
    parser.add_argument("--topk", type=int, default=MISO_TOPK,
                        help=f"Miso sampling top-k (default: {MISO_TOPK})")

    args = parser.parse_args()

    if args.smoke_test:
        run_smoke_test(args)
        return

    if args.preview:
        preview_chapter(args.preview)
        return

    if args.combine:
        combine_audiobook()
        return

    # Create output dirs
    os.makedirs(os.path.join(OUTPUT_DIR, "wav"), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "mp3"), exist_ok=True)

    print(f"\n{'='*60}")
    print(f"  AUDIOBOOK GENERATION")
    print(f"  {BOOK_TITLE}")
    print(f"  Engine: {args.engine}"
          + (f" | Voice: {args.voice} | Speed: {args.speed}" if args.engine == "kokoro" else ""))
    print(f"{'='*60}\n")

    generator = build_generator(args)
    tracker = ProgressTracker(PROGRESS_FILE, engine=args.engine)
    cleaner = MarkdownCleaner()

    track_number = 0
    pending_book_announcement = None
    start_time = time.time()
    chapters_done = 0

    for entry_type, content in BOOK_ORDER:
        if entry_type == "book":
            pending_book_announcement = content
            continue

        chapter_id = content.replace(".md", "")

        # Single chapter mode
        if args.chapter and chapter_id != args.chapter:
            track_number += 1
            continue

        # Resume mode
        if args.resume and tracker.is_completed(chapter_id):
            print(f"  [{track_number:02d}] {chapter_id}: SKIPPED (already done)")
            track_number += 1
            continue

        filepath = os.path.join(CHAPTERS_DIR, content)
        if not os.path.exists(filepath):
            print(f"  [{track_number:02d}] {chapter_id}: FILE NOT FOUND")
            track_number += 1
            continue

        print(f"  [{track_number:02d}] {chapter_id}: Processing...", end="", flush=True)

        # Preprocess
        segments = cleaner.process_file(filepath)

        # Prepend book announcement if this is first chapter in a Book
        if pending_book_announcement:
            segments = [
                TextSegment("book_announcement", pending_book_announcement),
                TextSegment("pause", duration=PAUSE_BOOK_ANNOUNCEMENT),
            ] + segments
            pending_book_announcement = None

        # Generate audio
        tracker.mark_started(chapter_id)
        audio = generator.generate_chapter_audio(segments)
        duration = len(audio) / generator.sample_rate

        # Get title for ID3
        with open(filepath) as f:
            first_line = f.readline().strip()
        title = first_line.lstrip('# ').strip() if first_line.startswith('#') else chapter_id

        # Save
        save_chapter_mp3(audio, chapter_id, title, track_number, generator.sample_rate)
        tracker.mark_completed(chapter_id, duration)
        chapters_done += 1

        print(f" {format_duration(duration)}")
        track_number += 1

    elapsed = time.time() - start_time
    print(f"\n  Generated {chapters_done} chapters in {format_duration(elapsed)}")

    # Manifest
    if args.engine == "kokoro":
        generate_manifest(tracker, args.engine, generator.sample_rate,
                          voice=args.voice, speed=args.speed)
    else:
        generate_manifest(tracker, args.engine, generator.sample_rate)
    print("\nAudiobook generation complete!")


if __name__ == "__main__":
    main()
