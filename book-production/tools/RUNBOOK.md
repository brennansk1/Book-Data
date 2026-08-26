# Per-Chapter Production Runbook (Autonomous PDF Run)

The orchestrator executes this cycle once per unit, strictly in book order after the register pair (Prologue, Ch-10). Each numbered step names the agent context (all fresh unless stated), its inputs, and its output file. No agent ever sees the whole manuscript.

## Inputs prepared before the cycle
- `research/<unit>/evidence.md` + `cases.md` (Researcher/Case Hunter — may be prepared one unit ahead, in parallel with the previous unit's gates)
- Gate 1: orchestrator selects case + confirms the brief's one-sentence argument; logs pick + runner-up in `reviews/<unit>/decisions.md` (PROXY for Showrunner — see reviews/DEVIATIONS.md)

## Drafting (three passes, three separate agent contexts)
1. **Pass A — the case, cold.** Inputs: cases.md (chosen case only), evidence.md, VOICE §1.5/§1.1. Output: `manuscript/<unit>/pass-a.md` (400–700 w, reportage only, no argument, no "this illustrates"). HARD RULE (added after ch-01 Gate 4): sensory anchors in historical scenes must come from the record (footage, reporting, testimony in the packet) or be framed as general truths/the author's own present — NEVER invented atmospheric specifics (weather, background sounds, unrecorded objects) asserted as fact about a real event.
2. **Pass B — the letter.** FRESH context. Inputs: the brief's argument sentence, CANON sections for the unit, evidence.md, seed corpus (author/ if present, models/, anti/). NOT Pass A. Output: `manuscript/<unit>/pass-b.md` — the argument as a letter to a named skeptical non-philosopher friend, digressions included, badly organized on purpose.
3. **Pass C — the merge.** FRESH context. Inputs: pass-a.md, pass-b.md, STYLE_BIBLE, VOICE, the brief, the two most recently frozen chapters (voice reference). Output: `manuscript/<unit>/draft-v1.md`. Case opens; letter's rhythm survives; "you" converted; looseness preserved; Pass D applied (delete the first paragraph; keep only if genuinely load-bearing, logged). Insert `<!-- ANCHOR-DRAFT -->` block of 200–400 w in first person at the load-bearing judgment point; add 2–4 `<!-- KEEP -->` marked imperfections.

## Gates

**COMPRESSED CYCLE (adopted at ch-04, 2026-08-06).** The original cycle ran cold-read → repair →
line-edit → Gate 3 → revision as five serial steps. From ch-04 onward the four readers (cold,
referee, red team, voice curator) all run in PARALLEL against draft-v1, and their findings are
resolved in ONE consolidated revision, followed by the line edit. This halves the serial depth per
chapter without reducing coverage — the reviewers were never dependent on each other's output, only
on the draft. Verification, rhythm review and freeze are unchanged.

4. **Gate 2 — lint (orchestrator, Bash):** `python3 tools/lint.py manuscript/<unit>/draft-v1.md --frozen manuscript/frozen/*.md`. Hard fail → targeted fix agent with the lint report only; re-run until pass.
5. **Gate 2.5 — burstiness worklist:** `python3 tools/burstiness.py manuscript/<unit>/draft-v1.md`. Advisory. Pass the 20-flattest-sentences worklist to the same fix agent for rewrites of the worst offenders (never optimise the score).
6. **Cold review (24h proxy):** fresh-context agent reads draft-v1 knowing nothing of its production; flags register failures, self-echo, seams. Fixes applied → `draft-v2-pre.md`.
7. **Line edit:** agent with STYLE_BIBLE only; cuts 10–20%; forbidden from `<!-- ANCHOR-DRAFT -->` and `<!-- KEEP -->` blocks. Output: `manuscript/<unit>/draft-v2.md`.
8. **Gate 3 — adversarial, three parallel fresh agents:**
   - Referee (hostile professional; strongest objection, ignored literature, tone-vs-strength gaps) → `reviews/<unit>/referee.md`
   - Red Team (find every AI tell with line numbers) → `reviews/<unit>/redteam.md`
   - Voice Curator (VOICE §1 deep causes + §10 judgment metrics: beat sentences, costly signals, obsession/omission, diction band, sensory anchors, idiolect) → `reviews/<unit>/voice.md`
9. **Revision:** drafter-role agent given draft-v2 + all three reviews + CANON + brief. Every finding fixed, conceded in text, or escalated (logged in decisions.md). Output: `draft-v3.md`.
10. **Gate 4 — continuity + verifier, two agents:**
    - Continuity: reads draft-v3 + `reviews/concept-index.md` (running registry of where each concept is introduced; updates it); flags use-before-introduction and restatement of frozen material → fixes applied.
    - Verifier: re-checks EVERY quotation and empirical claim against sources in Files/ or the web, independently of the evidence packet; pass/fail per claim → `reviews/<unit>/verify.md`. Any fail → fix or cut. A fabricated source is a project-ending error.
11. **Gate 5 proxy — rhythm review:** fresh agent reads draft-v3 aloud-minded (breath rule, cadence monotony, tricolon audibility, weak paragraph closes, quote-boundary clarity for future audio). Fixes applied.
12. **Freeze (PROVISIONAL):** copy to `manuscript/frozen/<unit>.md`; log freeze + all proxies in decisions.md; update concept-index; generate `audio/script/<unit>.md` (audio edition per STYLE_BIBLE §7: spoken numbers, restated antecedents, no cross-refs, homograph rewording from audio/homographs.tsv) — kept in sync so the audiobook run later is render-only; collect citations into `notes/<unit>.md` (endnote form) and append new sources to `research/sources.bib.md`.
13. **Partial PDF:** `python3 tools/build_pdf.py --draft` after each freeze — the book is always buildable.

## Part boundaries
After the last unit of each Part: **Gate 6 proxy** — 5 fresh blind judge agents, 20 paragraphs (10 from the Part, 10 from voice/seed/models/), proper nouns stripped; ≥3-of-5 flags → rewrite + pattern logged in `reviews/detection-log.md` and VOICE.md updated.

## Escalation
Three failures at the same gate → stop the unit, log in decisions.md, move on ONLY if a later unit doesn't depend on it; otherwise surface to Showrunner. Session/API limit deaths: every step writes to disk first; re-run the step, never the whole cycle.
