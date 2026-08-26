# Project Instructions

The active project is `book-production/` — an ~80k-word introductory volume + Miso TTS audiobook, produced under a gated pipeline. The old 49-chapter manuscript and its entire apparatus are ARCHIVED under `archive/v1/` and must not be edited or treated as current.

## Read before doing anything
1. `book-production/spec/PRODUCTION_BIBLE.md` — roles, workflow, gates
2. `book-production/spec/STYLE_BIBLE.md` then `spec/VOICE.md` — prose rules (linted, hard-fail)
3. `book-production/canon/CANON.md` + `POSITIONS.md` + `CANON_KEEPER_LOG.md` — what the framework claims; frozen; overrides everything in archive/
4. `book-production/tools/RUNBOOK.md` — the per-chapter production cycle
5. `book-production/PLAN.md` — the full execution plan and Showrunner decision queue

## Hard rules
- Chapters are drafted STRICTLY sequentially, via the three-pass protocol (VOICE §4). Never draft in parallel; never ask one context for a finished chapter.
- Never invent a citation, quotation, statistic, or date. Evidence packets in `research/` carry the verified material; the Verifier re-checks independently.
- Nothing may state a position at higher confidence than `canon/POSITIONS.md` allows.
- `manuscript/frozen/` is immutable; changes require a decisions.md entry + continuity re-run.
- Gate proxies for Showrunner-only steps are governed by `reviews/DEVIATIONS.md`; log every proxy, never silently skip a gate.
- Banned content list: CANON.md §9. Banned constructions: STYLE_BIBLE §3. Internal labels "Mode A/Mode B" never appear in prose (use "the standing rules" / "the override").
- Run `python3 tools/lint.py <draft> --frozen manuscript/frozen/*.md` before treating any draft as done.
- The user is the Showrunner: Gate 1 case picks, human anchors, Ch. 7, the Coda, and freezes are theirs to ratify; proxied decisions are provisional and flagged for their review.
