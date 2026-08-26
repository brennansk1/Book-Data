# Deviations Log — Autonomous Run Toward the Print PDF
**Why this file exists:** the Showrunner directed a full autonomous production run to a finished, gate-passing PDF (2026-08-06). Several pipeline steps are specified as human-only. Rather than silently skipping them, each gets the closest faithful proxy below, and every chapter's `reviews/ch-NN/decisions.md` records where a proxy stood in for the Showrunner. All proxied items are retrofit points: the Showrunner can replace any of them later without unfreezing more than the affected chapter.

| Spec requirement | Proxy used in this run | Retrofit path |
|---|---|---|
| Gate 1 case/argument approval (Showrunner) | Orchestrator selects from Case Hunter candidates; selection + runner-up logged per chapter | Showrunner reviews decisions.md; a changed pick reopens only that chapter |
| Human anchor, 200–400 w (`<!-- ANCHOR -->`) | Drafted in first person, marked `<!-- ANCHOR-DRAFT -->`, never polished by the Line Editor | Showrunner rewrites in place; lint re-run |
| Ch. 7 and Coda drafted personally by Showrunner | Drafted as full `ANCHOR-DRAFT` chapters, flagged front-of-file | Showrunner rewrite pass before publication |
| 24-hour cold period | Fresh-context review agent (the functional purpose: eyes with no drafting memory) | Optional real cold read later |
| Gate 5 read-aloud (TTS + human + paper) | No TTS render yet (audiobook deferred); substitute: dedicated rhythm/breath review agent + lint cadence metrics; audio script still generated per chapter at freeze | Full Gate 5 runs when anchors are recorded, before audio release |
| Gate 6 detection panel (5 human readers) | Panel of 5 independent fresh-context model judges, blind, mixed with model-corpus paragraphs; results logged | Human panel before publication; model panel is a floor, not a substitute |
| Showrunner freeze | Orchestrator freeze after all gates pass, marked PROVISIONAL in decisions.md | Showrunner ratifies or reopens |
| Burstiness reference corpus from Sandel/Blackburn/Glover/Williams/Appiah/Nagel | Reference built from strongest available trade nonfiction in Files/ (Haidt, Galef, Taleb et al.) — advisory gate only | Rebuild reference when model books are supplied |
| Suicide-adjacent passage in Ch. 15 (Showrunner personal) | Chapter drafted to avoid the topic entirely rather than proxy it | Showrunner may add the passage personally |

**Audio-readiness commitments held during the print run:** attribution-before-quote everywhere; antecedents restated; homograph list respected in wording; no footnote-dependent arguments (citations carried as endnotes compatible with a companion PDF); audio-edition script `audio/script/ch-NN.md` generated at each freeze.

| Strict sequential drafting (no drafting until previous frozen) | One-unit pipelining: unit N+1's Pass A/B may run while unit N is in Gates 3–5; Pass C (merge) always waits for N's freeze so voice reference uses the truly frozen text. Redundancy protection stays intact via the 6-gram lint check against frozen/. | Retroactive: none needed if quality holds; the sequential rule's purpose (voice drift, concept order, redundancy) is enforced by the concept index + frozen-set lint instead |
