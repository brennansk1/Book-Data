# Book Production Repo

Introductory volume + Miso TTS audiobook for the moral framework
previously drafted as *The Manual of Harmonious Rationality*.

## Read in this order

1. `spec/PRODUCTION_BIBLE.md` — roles, workflow, gates, repo layout. Every agent reads this first.
2. `spec/STYLE_BIBLE.md` — prose rules, banned constructions, linter thresholds. Every agent reads this second.
2b. `spec/VOICE.md` — **the one that matters most.** The deep causes of machine-sounding prose, the idiolect sheet, the seed corpus, and the three-pass drafting protocol. STYLE_BIBLE catches the cheap failures; this catches the expensive ones.
3. `canon/CANON.md` — what the framework claims. Source of truth; overrides the 1,325-page draft.
4. `spec/CHAPTER_BRIEFS.md` — the 20 briefs. Drafters read only their own.
5. `spec/AUDIO_SPEC.md` — Miso pipeline, voice design, QC harness.

Background (not required reading for drafting agents):
`review/review-harmonious-rationality.md` — critical review of the 1,325-page draft.
`review/revision-plan-constructivist-realism.md` — the philosophical revisions CANON.md implements.

## Build first, write second

    python tools/lint.py manuscript/ch-10/draft-v1.md --frozen manuscript/frozen/*.md

`tools/lint.py` is Gate 2 and exits nonzero on hard fail. Wire it into CI
before any chapter is drafted.

    python tools/burstiness.py --build-reference voice/seed/models/*.md
    python tools/burstiness.py manuscript/ch-10/draft-v3.md

`tools/burstiness.py` is Gate 2.5 — advisory only. Its value is the printed
worklist of flattest sentences, not the score. Never optimise the score.

`tools/asr_diff.py` (spec in AUDIO_SPEC §10) is the audio QC harness and
should exist before the first render.

## Build the seed corpus before drafting

    voice/seed/author/    3-5k words of the Showrunner's real, unedited writing
    voice/seed/models/    6-10 annotated passages from the target books
    voice/seed/anti/      3 passages from the 1,325-page draft, labelled "this is the failure"

Samples produce voice; rules produce rule-following prose. This directory does
more for the book than the entire linter. See `spec/VOICE.md` §3.

## Still to build

- `canon/POSITIONS.md` — position, confidence, known vulnerability. Nothing
  in the book may exceed the confidence stated here.
- `canon/GLOSSARY.md` — one definition per term, used everywhere.
- `tools/asr_diff.py`, `tools/render.py`, `tools/assemble.py`
- `audio/lexicon.tsv`, `audio/homographs.tsv`
