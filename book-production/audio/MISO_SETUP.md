# Audiobook Pipeline: MisoTTS Setup Guide

`generate_audiobook.py` now defaults to **MisoTTS** (`MisoLabs/MisoTTS`, a
Sesame-CSM-style 8B-parameter model) instead of Kokoro. This doc covers
environment setup, first-run weight download, realistic performance
expectations on an Apple M4 Mac mini (24 GB unified RAM), memory guidance,
and the Kokoro fallback path.

The MisoTTS inference code is already cloned into `./MisoTTS` (code only —
no model weights). It requires Python 3.10, while the system Python on this
machine is 3.9, so you need a dedicated virtual environment.

---

## 1. Create a Python 3.10 environment

The repo ships a `uv`-based workflow and pins `requires-python = ">=3.10,<3.13"`.
`uv` is already installed on this machine (`~/.local/bin/uv`), so this is the
easiest path — it downloads an isolated Python 3.10 for you, no system Python
changes needed:

```bash
cd /Users/brennankelley/Desktop/Projects/Book-Data-main/MisoTTS
uv sync --python 3.10
source .venv/bin/activate
```

If you'd rather use `pyenv` + `pip`:

```bash
brew install pyenv
pyenv install 3.10.14
cd /Users/brennankelley/Desktop/Projects/Book-Data-main/MisoTTS
~/.pyenv/versions/3.10.14/bin/python3.10 -m venv .venv
source .venv/bin/activate
pip install -e .
```

Either way, once the venv is active, also install the packages
`generate_audiobook.py` itself needs (shared across both engines):

```bash
pip install soundfile numpy pydub mutagen
brew install ffmpeg   # if not already installed (pydub needs it)
```

**Do not `pip install kokoro` into this venv** — it's a separate dependency
tree only needed for `--engine kokoro`. Keep that in whatever environment you
originally ran the Kokoro pipeline in, or install it separately if you want
one venv for both.

---

## 2. Hugging Face access (first run only)

MisoTTS's tokenizer loader (`generator.py: load_llama3_tokenizer`) pulls
`meta-llama/Llama-3.2-1B` from Hugging Face — this is a **gated repo**. Before
your first run:

1. Log in at huggingface.co and accept the Llama 3.2 license on the
   [meta-llama/Llama-3.2-1B model page](https://huggingface.co/meta-llama/Llama-3.2-1B).
2. Authenticate locally: `huggingface-cli login` (paste an access token from
   your HF account settings), or `export HF_TOKEN=...`.

Without this, the first run will fail on the tokenizer download with a 403.

---

## 3. First run: weights download (~30–40 GB disk)

Nothing was downloaded by this setup step — only the inference *code* was
cloned. The first time you actually run the pipeline (or `--smoke-test`), it
will download and cache, via the Hugging Face Hub cache (`~/.cache/huggingface`):

- The MisoTTS 8B checkpoint (`MisoLabs/MisoTTS`) — the bulk of the ~30–40 GB.
- The Mimi audio codec weights (via `moshi`).
- The SilentCipher watermarking model (`sony/silentcipher`) — a separate
  download; if it times out, just rerun the command, the cache resumes.
- The Llama 3.2 tokenizer files.

Make sure you have at least ~40 GB of free disk before starting, and a
stable connection (or patience — retries resume rather than restart).

---

## 4. Validate the setup before a full run

**Always run the smoke test first.** It loads the model, synthesizes one
sentence, and writes a WAV so you can confirm the voice and pipeline work
before committing to a multi-hour (or multi-day) generation run:

```bash
python3 generate_audiobook.py --smoke-test
```

This prints load time, generation time, and a realtime factor, and writes
`Audiobook/smoke_test.wav`. Listen to it.

If you want to force CPU (see the MPS caveat below) instead of letting it
auto-detect:

```bash
python3 generate_audiobook.py --smoke-test --device cpu
```

---

## 5. Performance expectations on the M4 Mac mini (24 GB, MPS)

Be realistic about this. Miso TTS 8B is an **8-billion-parameter
autoregressive model** generating audio one Mimi frame at a time — it is
nothing like the ~80M-parameter Kokoro model the pipeline used before.

- **This is not a fast local model.** MisoTTS's own README describes it as
  designed for high-VRAM GPU inference (24 GB+ recommended) and explicitly
  says CPU/consumer-GPU inference is slow. There is no Apple Silicon
  benchmark published by the model authors.
- **MPS has a known limitation with this repo.** MisoTTS's own reference
  script (`run_misotts.py`) deliberately **skips MPS and uses CPU instead**,
  with the comment "skipping MPS due to float64 limitations" — some op in
  the Mimi codec or the SilentCipher watermarker doesn't work on MPS.
  `generate_audiobook.py`'s Miso engine still *tries* MPS first (per your
  request for cuda → mps → cpu auto-detection), but wraps model loading and
  generation in a fallback: if MPS throws (float64/"not implemented"-style
  errors), it automatically reloads on CPU and keeps going, printing a
  warning. Expect this fallback to trigger — treat MPS as "best effort,"
  and use `--device cpu` directly if you'd rather skip the failed attempt.
- **Whichever device you land on (MPS or CPU), expect this to run
  significantly slower than realtime** — likely several times slower than
  real-time audio, given the 8B backbone doing full autoregressive decoding
  per Mimi frame with no CUDA kernels, kv-cache-friendly attention, or
  batching to help it. The existing Kokoro-generated audiobook is **~28
  hours 45 minutes** across 52 chapters (see `Audiobook/manifest.json`) — a
  full from-scratch Miso run of a book that size could plausibly take
  **multiple days** of continuous local compute on this hardware. Do not
  plan to run the whole book start-to-finish in one sitting.

### Recommended workflow given this

1. Run `--smoke-test` first (above) to confirm setup and voice quality.
2. Generate **one chapter at a time**:
   ```bash
   python3 generate_audiobook.py --chapter CH-01
   ```
   Time it, then extrapolate to estimate the full-book runtime on your
   hardware before committing.
3. Use `--resume` for everything else, so an interrupted run (sleep, crash,
   closing the laptop) doesn't cost you re-work:
   ```bash
   python3 generate_audiobook.py --resume
   ```
   Progress is tracked per-engine in `Audiobook/progress.json` (Kokoro's
   existing completed-chapter records are untouched and namespaced
   separately from Miso's, so switching engines is safe — no need to delete
   the file).
4. **If the full-book timeline is impractical, rent a cloud GPU** with
   24 GB+ VRAM (RTX 4090, A5000, L4, A100) for a few hours instead of running
   for days locally:
   ```bash
   python3 generate_audiobook.py --resume --device cuda
   ```
   On CUDA with bf16, this should be dramatically faster (the model was
   designed for this). A single rented GPU-hour or two is likely cheaper
   than the electricity + wall-clock cost of a multi-day local CPU/MPS run.

---

## 6. Memory guidance

- The pipeline always requests `dtype=torch.bfloat16` when loading Miso
  (`load_miso_8b(..., dtype=torch.bfloat16)`) — **this is required**. The
  bf16 weights are ~16 GB; float32 weights are ~33 GB and will not fit in
  24 GB of unified memory (macOS also needs headroom for the OS, the Mimi
  codec, the SilentCipher watermarker, and KV caches on top of the weights).
- **Close other memory-heavy apps** (browsers with many tabs, IDEs, Docker,
  etc.) before a run — on unified memory, GPU and system RAM are the same
  pool, so a full browser can push you into swap and tank performance or
  cause an out-of-memory crash mid-chapter.
- If you see out-of-memory errors even in bf16, that's a sign to switch to
  `--device cpu` (slower, but different memory pressure characteristics) or
  move to a cloud GPU rather than trying float32 locally.

---

## 7. Falling back to Kokoro

The original Kokoro engine is fully preserved and still available. If Miso
proves impractical for your timeline, or you just want the original voice
back:

```bash
python3 generate_audiobook.py --engine kokoro --resume
```

This uses the same preprocessing, pause handling, ID3 tagging, and combine
logic as before, at Kokoro's original 24 kHz / near-realtime speed. Kokoro's
already-completed chapters in `Audiobook/progress.json` are recognized
automatically (they predate the `--engine` flag and are treated as legacy
Kokoro entries).

---

## 8. Quick reference

```bash
# One-time setup
cd MisoTTS && uv sync --python 3.10 && source .venv/bin/activate
pip install soundfile numpy pydub mutagen
huggingface-cli login   # accept meta-llama/Llama-3.2-1B license first

# Validate
cd ..
python3 generate_audiobook.py --smoke-test

# Generate one chapter, time it
python3 generate_audiobook.py --chapter CH-01

# Resume the rest (interruption-safe)
python3 generate_audiobook.py --resume

# Force a device
python3 generate_audiobook.py --resume --device cpu
python3 generate_audiobook.py --resume --device cuda   # on a rented GPU box

# Combine finished chapters into the full audiobook
python3 generate_audiobook.py --combine

# Fall back to the original engine
python3 generate_audiobook.py --engine kokoro --resume
```
