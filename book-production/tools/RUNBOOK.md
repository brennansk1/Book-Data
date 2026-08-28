# Per-Chapter Runbook — LEAN CYCLE (adopted 2026-08-27)

Supersedes the previous runbook. Same gates, same standard, roughly a third of the tokens.

## Why it changed

The old cycle cost ~1.4M tokens per chapter. Measurement showed most of that was not quality work:

| Waste | Cost | Fix |
|---|---|---|
| Every agent re-read 12,900 words of spec (STYLE_BIBLE + VOICE + IDIOLECT + detection-log + canon) | ~170k/chapter | `spec/BRIEF.md`, 999 words, compiled. Agents read one file. |
| Four reviewers each re-read the whole draft; three of them kept finding the same things | ~380k/chapter | Two reviewers: Referee (independent, adversarial) + Craft (cold-read, AI-tells and voice in one pass). |
| Verifier re-extracted every claim from prose before it could check anything | ~140k/chapter | Pass C emits `claims.tsv`. The verifier checks a list. |
| Audio script + endnotes hand-built per chapter | ~150k/chapter | `tools/mkaudio.py` does the mechanical 80% and emits a TODO of judgment calls. Batched at the end. |
| Rhythm review re-read the chapter to find long sentences and homographs | ~100k/chapter | `mkaudio.py --todo` and lint report those mechanically. |
| Research packets ran 25–30k words, most never used | ~150k/chapter | Capped: 3 candidate cases, 1,200-word packet. |

**Nothing that ever caught a real defect was removed.** The referee (which caught a fabricated
mechanism), the verifier (a fabricated statistic, a migrated quote, four factual failures) and the
three-pass drafting protocol are untouched.

## The cycle

**Inputs.** `research/<unit>/packet.md` — ONE file, ≤1,200 words: three candidate cases with the
vivid detail and the risks, then the claims the chapter needs with source and confidence. Gate 1
selection logged in `reviews/<unit>/decisions.md`.

1. **Pass A — the case, cold.** Reads: packet + `spec/BRIEF.md`. 400–700 words of reportage.
   No invented atmospherics for real events, ever.
2. **Pass B — the letter.** FRESH context, does NOT see Pass A. Reads: packet + BRIEF + the
   chapter's argument sentence + the canon sections it needs. The single highest-value step in the
   pipeline; do not skip or merge it.
3. **Pass C — the merge.** FRESH. Reads: pass-a, pass-b, BRIEF, ONE most-recently-frozen chapter as
   voice reference. Emits `draft-v1.md` **and `claims.tsv`** — every checkable claim it made, one per
   line: `claim<TAB>source-from-packet<TAB>confidence`. A claim with no packet source must be marked
   `CONJECTURE` and flagged as such in the prose.
4. **Gate 2 — lint** (`tools/lint.py … --frozen manuscript/frozen/*.md`). Hard fails fixed by the
   orchestrator directly; agents are not spawned for regex fixes.
5. **Gate 3 — two reviewers, parallel.** Both read BRIEF + draft only.
   - **Referee** — hostile domain expert. Argument, evidence, overclaiming, ignored literature.
   - **Craft** — one agent, three lenses: cold read (register, seams, drift), AI tells (uniform
     density, costless admissions, templates), voice (VOICE §10 scorecard, idiolect, cross-chapter
     repetition). These three overlapped heavily in practice; splitting them bought little.
6. **Revision.** One consolidated pass over both reviews. Reads: draft, two reviews, BRIEF.
7. **Gate 4 — verify.** Reads `claims.tsv`, not the chapter. Checks each claim independently against
   `Files/` (absolute path — see `research/FILES_INDEX.md`) or the web. PASS / NOTE / FAIL per line.
   Unchanged in rigour; cheaper because the extraction work is already done.
8. **Freeze.** Copy to `manuscript/frozen/`, log, update `reviews/concept-index.md`, rebuild the PDF.

## Deferred to a single batched run at the end
Audio scripts (`tools/mkaudio.py` per chapter, then ONE agent pass over all the `.todo.txt` files),
endnotes (assembled from the `verify.md` files), and the bibliography. Doing these per-freeze cost
~150k a chapter and bought nothing the batch won't.

## Part boundaries
Gate 6 detection panel, unchanged: 20 paragraphs, half from the Part and half from the model corpus,
proper nouns stripped, five blind judges. `reviews/panel/` holds the builder and the key.

## Model selection
Mechanical passes (audio TODO resolution, endnote formatting, lint fixes) go to Haiku. Drafting,
review and verification stay on Sonnet. Orchestration judgment stays here.
