# Execution Plan — From Current Assets to Finished Product
**Compiled:** 2026-08-06 · Owner: Showrunner (Brennan) · Orchestrator: Claude
**Deliverables:** (1) ~80,500-word introductory volume (Prologue + 17 chapters + Coda), (2) ~9.5-hour Miso TTS audiobook in the author's cloned voice, (3) free ~90-minute gateway edition (Parts One–Two).

---

## A. Asset inventory (what exists today)

**Complete and adopted as governing:**
- `spec/PRODUCTION_BIBLE.md` — roles, sequential workflow, six gates. Adopted.
- `spec/STYLE_BIBLE.md` — register rules, banned constructions, linter thresholds.
- `spec/VOICE.md` — eight deep causes of machine prose, seed-corpus design, three-pass drafting protocol, detection panel.
- `spec/CHAPTER_BRIEFS.md` — 19 briefs (Prologue, Ch. 1–17, Coda), ~80.5k words total. Note: PRODUCTION_BIBLE says "18 chapters"/README says "20 briefs" — the briefs file is authoritative: 19 units.
- `spec/AUDIO_SPEC.md` — Miso pipeline design (rolling context + fixed anchor, three anchor voices, chunking ≤200 chars, silence table, LUFS mastering, ASR-diff QC, disclosure).
- `canon/CANON.md` — revised framework content. Overrides the old 207k-word draft. Bans: "Constructivist Realism" label, three-layer grounding, thermometer analogy, value vector, burden-shift impartiality, Moloch monism, policy-as-derivation, the Oath.
- `review/` — the critical review and revision plan CANON implements (background reference).
- `tools/lint.py` (Gate 2, verified runnable) and `tools/burstiness.py` (Gate 2.5, runnable).

**Existing project assets that carry over:**
- **Old draft (49 chapters, ~207k words)** at `Book/Chapters/` + backup at `Revision/FirstEdition_Backup/` — now source material and the anti-corpus quarry. Five chapters (01, 02, 04, 05, 08) were rewritten under the superseded plan; treat all as source only.
- **Source library, 34 works in `Files/`** — strong coverage for the Researcher: Ostrom (Governing the Commons), Axelrod, Schelling (Strategy of Conflict), Parfit (Reasons and Persons), Singer (Practical Ethics), Rawls, Aristotle (NE), Kahneman, Haidt, Galef, Dawkins, Sen, Scott, Sowell, Taleb, Bostrom, and more.
- **MisoTTS integration** — repo cloned at `MisoTTS/`; `generate_audiobook.py` already speaks the real API (load_miso_8b, Segment, bf16, rolling context). Will be superseded by `tools/render.py`/`assemble.py` built to AUDIO_SPEC, but the API learnings and MPS-fallback work carry over. Setup doc at `Revision/AUDIOBOOK_MISO_SETUP.md`.
- Old `Positions/POSITION_REGISTRY.md` — feeds the new `canon/POSITIONS.md` (confidence ceilings), updated to CANON's revisions.

**Missing — must be built before prose (README "Build first, write second"):**
| Item | Builder | Notes |
|---|---|---|
| `canon/POSITIONS.md` | Canon Keeper (agent draft → Fable review → Showrunner freeze) | Position, confidence, vulnerability; nothing in the book may exceed it |
| `canon/GLOSSARY.md` | Canon Keeper | One definition per term |
| `tools/asr_diff.py` | delegated | Whisper transcript diff vs. source; AUDIO_SPEC §10 calls it the highest-value engineering step |
| `tools/render.py`, `tools/assemble.py` | delegated | Per AUDIO_SPEC §7: anchor+rolling context, chunking, silence table, room tone, LUFS targets |
| `audio/lexicon.tsv`, `audio/homographs.tsv` | delegated starter, iterated during renders | Seed with the §9 proper-noun and homograph lists |
| `voice/seed/anti/` (3 failure passages) | orchestrator | Pulled from the first-edition backup |
| `voice/seed/author/` (3–5k words) | **Showrunner only** | Real unedited writing — emails, notes, arguments |
| `voice/seed/models/` (6–10 annotated passages) | **Showrunner supplies texts** | Sandel *Justice*, Blackburn *Being Good*, Glover *Humanity*, Williams *ELP*, Appiah *Honor Code*, Nagel — none currently in `Files/` |
| Idiolect sheet (VOICE §2) | **Showrunner** (Claude drafts candidates from author corpus) | Sentence shapes, image family, joke shape, overused words, one refusal |

**Research-library gaps** (new-canon literature not in `Files/`; Researcher works from web/secondary sources until supplied): Sinhababu *Humean Nature*; Kahane "Pain, Dislike and Experience"; Bramble; Crisp *Reasons and the Good*; Grahek *Feeling Pain and Being in Pain* (pain asymbolia, Ch. 5's likely opening case); Binmore *Natural Justice*; Greif (Maghribi traders); Appiah *The Honor Code*; Boehm; Annas *Intelligent Virtue*; Doris; Frank *Passions Within Reason*; Jackall *Moral Mazes*; Tetlock; Newfoundland cod-collapse literature.

---

## B. The plan

### Phase 0 — Infrastructure (now; ~2–3 days; fully delegable except Showrunner items)
1. Draft `canon/POSITIONS.md` + `canon/GLOSSARY.md` from CANON + old registry (agent) → Fable-level review → **Showrunner freeze**. Canon is then immutable; changes go through the Canon Keeper with logged reasons.
2. Build `tools/asr_diff.py`, `render.py`, `assemble.py`; seed lexicon/homograph tables; wire `lint.py` into a `make check` entry point.
3. Assemble `voice/seed/anti/` (3 labeled failure passages from the old draft).
4. **Showrunner:** supply author corpus, model-book texts, idiolect sheet. → Claude drafts the idiolect sheet from the corpus for approval.

### Phase 1 — Register-setting pair: Prologue + Ch. 10 (~1–2 weeks incl. cold periods)
Per PRODUCTION_BIBLE §8 these two are drafted first because they set the register at both extremes.
1. Researcher + Case Hunter packets for both (parallel, delegable — Prologue case candidates per brief: professional arms race / fishery / workplace-hours spiral; Ch. 10: institutional cover-up with paper trail).
2. **Gate 1 (Showrunner):** pick the case, approve the one-sentence argument.
3. Three-pass drafting — each pass a fresh agent context (Pass A case-cold; Pass B letter to a named skeptic; Pass C merge; Pass D delete first paragraph).
4. 24-hour cold period (hard stop; calendar it).
5. Gate 2 lint + Gate 2.5 burstiness worklist → targeted rewrites.
6. **Showrunner:** write the 200–400-word anchor (`<!-- ANCHOR -->`).
7. Line edit (agent; forbidden from ANCHOR/KEEP blocks) → Gate 3: Referee + Red Team + Voice Curator, three parallel adversarial agents → revision → Gate 4: Continuity + Verifier (independent quote/claim re-check) → Gate 5: read-aloud (TTS render + human read + **Showrunner on paper**) → **Showrunner freeze**.

### Phase 2 — Sequential production of the remaining 17 units (~6–10 weeks)
Strict order: Ch. 1→9, 11→17, then Prologue-adjacent Coda last (Coda and Ch. 7 are **Showrunner-drafted**, agent-supported). One chapter in flight at a time; the two most recently frozen chapters ride along as voice reference. Research/case packets for chapter N+1 are prepared while chapter N is in gates (allowed parallelism — packets aren't prose).
**Gate 6 detection panel after each Part:** 20 paragraphs, 5 human readers, target chance accuracy; failures feed `reviews/detection-log.md` and update VOICE.md. (Showrunner recruits the readers; this is the one gate that cannot be simulated.)

### Phase 3 — Audio production (~1–2 weeks, overlaps late Phase 2)
1. **Showrunner records three anchors** (narration / quotation / part-opening; 45–60s each, same mic and room, ~150 wpm).
2. Anchor iteration against Prologue + Ch. 10 on a rented CUDA GPU (L40S/A100/4090; the full-book render is an estimated 8–20 GPU-hours — tens of dollars. Local M4 handles prep, assembly, mastering, QC only).
3. Audio-edition scripts per chapter (separate manuscript: spoken numbers, restated antecedents, no cross-references, homograph rewording) — produced at freeze time for each chapter, not in one batch at the end.
4. Render Ch. 10 end-to-end, master, full QC → fix pipeline → batch render.
5. ASR-diff every segment (Whisper), human listen-through at 1.0x, mastering to −18/−20 LUFS, room-tone bed, chapter assembly.
6. Synthetic-narration disclosure in front matter, metadata, and first 30 seconds. Watermark stays.
7. Cut the gateway edition (Parts One–Two, ~90 min) from the finished master.

### Phase 4 — Ship checklist
Companion PDF (citations, notes, bibliography — the full apparatus the audio can't carry); final continuity pass; verify distributor AI-narration policy; version print and audio manuscripts together.

---

## C. Decision queue for the Showrunner (blocking items in bold)
1. **Author seed corpus** (3–5k words unedited) — highest-leverage single input in the pipeline.
2. **Model-book texts** for `voice/seed/models/` (six titles above).
3. **Gate 1 picks for Prologue and Ch. 10** once packets are ready (~2 days after go).
4. Idiolect sheet approval (Claude drafts once #1 arrives).
5. Title direction (spec candidates: *The Thing Nobody Chose* / *Everyone Hates This* / *The Physics of Trust* / *Three Gates*; system name demoted to subtitle).
6. Repugnant-conclusion stance: CANON defaults to person-affecting restriction with costs acknowledged — confirm or pick critical-level / bite-the-bullet.
7. Anchor voice recordings (Phase 3 start).
8. Detection-panel readers: five people willing to do a 15-minute blind test, five times.

## D. Risks and mitigations
- **Session/API limits killing long agent runs** (happened 2026-08-05): chapters are produced one at a time now, so blast radius is one pass; every pass writes to disk immediately.
- **Canon drift:** POSITIONS.md freeze + Canon Keeper as the single answer-source; drafters never read the old manuscript.
- **Quote fabrication:** Researcher packets carry exact wording/page; Verifier re-checks independently; standing instruction #1 (a fabricated source is a project-ending error).
- **Miso on Apple Silicon:** upstream repo skips MPS (float64 limitation); local renders fall back to CPU for smoke tests only; production renders on rented CUDA per AUDIO_SPEC §11.
- **Voice mimicry ethics:** the cloned voice is the author's own, recorded by him, with disclosure baked into the deliverable. No third-party voice is cloned.
