# Production Bible

**Project:** a general-audience introduction to the moral framework previously drafted as *The Manual of Harmonious Rationality*.
**Deliverables:** an ~80,000-word trade book (18 chapters + prologue + coda), a synthetic-narration audiobook produced with Miso TTS 8B, and a free ~90-minute gateway edition cut from the finished master.
**Standard:** prose quality comparable to Sandel's *Justice*, Blackburn's *Being Good*, or Glover's *Humanity*. Argument quality that survives a hostile professional referee.

This document is the operating manual for the agent team. Every agent reads this file and `STYLE_BIBLE.md` before doing anything. Drafting agents additionally read `CANON.md` and their own brief from `CHAPTER_BRIEFS.md`.

---

## 1. The failure this project exists to avoid

A previous draft of this material ran 1,325 pages and ~207,000 words. It was competent and unpublishable, for reasons the team must internalize because they are the default failure mode of LLM-drafted nonfiction:

- Section headers every ~500 words; "Summary" and "What This Chapter Established" closers on nearly every chapter
- Nested bullet lists carrying the primary exposition instead of prose
- The institutional "we" throughout; no first-person judgment
- Almost no scenes — no named individuals doing things in places at times
- Every claim stated at the same confidence, from a bare axiom to a contested empirical literature
- Persistent tricolon rhythm and "not X, but Y" construction
- Quotations dropped in as authority-decoration
- Zero citations, no bibliography, in a book whose thesis is epistemic honesty
- Massive cross-chapter redundancy, because chapters were drafted without knowledge of each other

**Every one of these is mechanically detectable.** This pipeline detects them with a linter and a red-team pass rather than hoping a reviewer notices. Style compliance is a *test that fails the build*, not a note in a review.

---

## 2. Roles

Roles are functions, not necessarily separate models. Each runs in its own context with only the inputs listed. **Do not merge the Drafter with the Researcher or the Red Team** — the whole point is that different agents have different incentives and blind spots.

### 2.1 Showrunner (human — Brennan)
Final authority on voice, argument, and what ships. Approves every chapter freeze. **Not delegable.** The book's credibility depends on a single identifiable person standing behind its judgment calls, and the first-person passages must be genuinely his.

### 2.2 Canon Keeper
Owns `canon/CANON.md`, `canon/POSITIONS.md`, `canon/GLOSSARY.md`.
Answers every "what does the framework say about X" question from other agents. Resolves contradictions between chapters. Logs any change to a canonical position with a reason.
**Never writes manuscript prose.**

### 2.3 Researcher
Produces one `research/ch-NN/evidence.md` packet per chapter before drafting begins. Contains: every empirical claim the chapter needs with a source and a confidence rating, every quotation with exact wording, author, work, year, and page, and a note on any claim the literature does not actually support at the confidence the brief assumes.
**Never writes manuscript prose.** Explicitly tasked with saying "the brief overstates this."

### 2.4 Case Hunter
Produces `research/ch-NN/cases.md`: three to five candidate opening cases per chapter — real people, named, in places, at dates, doing things. Includes the specific detail that makes each one vivid.
This is a separate role because it is a different skill and because it is the first thing an efficiency-seeking pipeline drops. **A chapter without a concrete case does not pass Gate 3.**

### 2.5 Drafter
Writes exactly one chapter per context. Inputs: `STYLE_BIBLE.md`, `CANON.md`, the chapter brief, the evidence packet, the case packet, and **the two most recently frozen chapters** as voice reference.
Never receives the whole manuscript. Full-manuscript context causes self-echo and redundancy, which is what produced the 207,000-word draft.

### 2.5b Voice Curator
Owns `spec/VOICE.md`, the seed corpus in `voice/seed/`, and the idiolect sheet. Checks every draft against the judgment-based targets the linter can't compute: beat sentences, costly signals, the deliberate obsession and omission, sensory anchors, diction band, idiolect markers.

Also owns the detection panel (Gate 6) and maintains `reviews/detection-log.md`, feeding every identified paragraph back into `VOICE.md` as a new pattern.

**This role exists because the linter measures proxies and the Voice Curator measures the thing.**

### 2.6 Line Editor
Sentence-level rewrite against `STYLE_BIBLE.md`. Runs after the linter, fixes what the linter flags plus what it can't see: dead metaphors, buried verbs, throat-clearing openings, paragraphs that end weakly.
Authorized to cut. Expected to cut 10–20% on average.

### 2.7 Referee (adversarial — philosophy)
Reads the chapter as a hostile professional in the relevant subfield. Writes `reviews/ch-NN/referee.md`: the strongest objection, the literature the chapter ignores, any place the argument is weaker than its tone suggests, and any claim that would be laughed at in a seminar.
**Instructed to be unfair.** The chapter must either answer the objection, concede it in text, or the Showrunner overrules with a logged reason.

### 2.8 Red Team (adversarial — AI tells)
One job: find evidence the chapter was written by a machine. Writes `reviews/ch-NN/redteam.md` listing every tell with a line number. Runs after the Line Editor, on text that has already passed the linter — its job is the tells the linter can't regex.

### 2.9 Continuity
Owns cross-chapter consistency: terminology, whether a concept is introduced before it is used, and **repetition detection**. Maintains a running concept-introduction index. Flags any passage that restates material from a frozen chapter.

### 2.10 Verifier
Independently re-checks every quotation and every empirical claim against the source, after the chapter is otherwise final. Does not trust the Researcher's packet. Produces a pass/fail per claim.
This role exists because the previous draft shipped with zero verifiable citations and that is the single most damaging thing about it.

### 2.11 Audio Producer
Owns the audio edition script, the pronunciation and homograph tables, rendering, assembly, mastering, and the ASR-diff QC harness. See `AUDIO_SPEC.md`.

---

## 3. Workflow

Chapters are produced **strictly in sequence**. No chapter begins drafting until the previous one is frozen. This is the single most important process rule: parallel drafting is what produces redundancy, style drift, and concepts used before they are introduced.

```
BRIEF (Canon Keeper confirms brief against canon)
  ↓
EVIDENCE PACKET (Researcher)  +  CASE PACKET (Case Hunter)     [parallel]
  ↓
GATE 1 — Showrunner approves the case and the argument shape
  ↓
PASS A — the case, cold          (Drafter, fresh context)
PASS B — the letter              (Drafter, FRESH context — see VOICE §4)
PASS C — the merge               (Drafter, third context)
PASS D — delete the first paragraph
  ↓
[24-HOUR COLD PERIOD — mandatory, VOICE §9]
  ↓
GATE 2   — LINTER            (tools/lint.py; hard fail)
GATE 2.5 — BURSTINESS        (tools/burstiness.py; advisory + rewrite worklist)
  ↓
SHOWRUNNER writes the human anchor (200–400 w, VOICE §5)
  ↓
LINE EDIT (Line Editor — forbidden from touching <!-- KEEP --> or <!-- ANCHOR -->) → v2
  ↓
GATE 3 — REFEREE + RED TEAM + VOICE CURATOR   [parallel]
  ↓
REVISION (Drafter, given all three review files) → v3
  ↓
GATE 4 — CONTINUITY + VERIFIER
  ↓
GATE 5 — READ-ALOUD (TTS render + one human reading aloud + Showrunner on paper)
  ↓
SHOWRUNNER FREEZE → manuscript/ch-NN/frozen.md

  ↓ [end of each Part]
GATE 6 — DETECTION PANEL (blind A/B against the model corpus, VOICE §8)
```

**The three-pass drafting protocol is not optional and not a suggestion.** Asking any model for a finished chapter in one request produces the encyclopedia register, every time, regardless of how good the style guide is. Pass B — writing the argument as a letter to one named skeptical friend, in a fresh context — is the single highest-leverage step in this pipeline. Expository register cannot survive the second person.

A chapter that fails a gate returns to the previous stage. Three failures at the same gate escalate to the Showrunner — it usually means the brief is wrong, not the draft.

---

## 4. Gates

**Gate 1 — Argument and case.** Does the chapter have exactly one argument, statable in one spoken sentence? Is there a real, specific opening case? If either is missing, drafting does not start.

**Gate 2 — Linter.** Automated, hard fail. Thresholds in `STYLE_BIBLE.md` §6. The linter does not give advice; it fails the build.

**Gate 2.5 — Burstiness.** `tools/burstiness.py` scores sentence-level surprisal variance against a reference corpus built from the model books. Advisory, never a hard fail — the metric is gameable and must never be optimised directly. What matters is the printed worklist of the twenty flattest sentences, which is where reader attention slides off.

**Gate 3 — Adversarial.** Referee, Red Team, and Voice Curator run in parallel on the line-edited text. Every finding is either fixed, conceded in the text, or overruled by the Showrunner with a written reason in `reviews/ch-NN/decisions.md`.

**Gate 4 — Continuity and verification.** No concept used before introduction. No passage restating frozen material. Every quotation exact and cited. Every empirical claim at defensible confidence.

**Gate 5 — Read-aloud.** Three passes: the TTS render (rhythm and monotony), one human reading it aloud (sentences that are physically unpleasant to say), and the Showrunner reading it on paper (screens forgive flatness; paper doesn't). See §5.

**Gate 6 — Detection panel.** Run at the end of each Part, not at the end of the book. Twenty paragraphs, ten from the finished Part and ten from the model corpus, proper nouns stripped, given to five readers who don't know the ratio. One question: which were written by a machine? Target is chance performance. Any paragraph flagged by three or more readers is rewritten and the pattern is logged in `reviews/detection-log.md` and added to `VOICE.md`.

This is the only measurement in the pipeline that tests the actual objective. Everything else is a proxy. Running it after Part One rather than at the end is what lets the findings shape the remaining four parts.

---

## 5. The read-aloud gate

**Every chapter is rendered to audio with Miso and listened to before it is frozen.**

This is not an audiobook step. It is the primary prose QA instrument, and it is the reason the audiobook and the book must be built together rather than sequentially.

Text review does not catch: tricolon rhythm tics, sentence-length monotony, abstract nouns as subjects, paragraphs that end on a weak beat, or the specific flatness of prose that was assembled rather than written. All of these are obvious within thirty seconds of listening.

Procedure: render the chapter with the standard pipeline, listen at 1.0x on headphones, log every place attention drifts in `reviews/ch-NN/listen-log.md` with a timestamp. **Attention drift is the finding.** Don't diagnose it in the moment; mark it and diagnose later. Any passage that loses the listener twice across two rendered versions gets cut or rewritten from scratch.

Secondary benefit: by the time the manuscript is finished, every chapter has already been rendered and QC'd once, and the pronunciation and homograph tables are already built.

---

## 6. Repository structure

```
canon/
  CANON.md              framework content — the single source of truth
  POSITIONS.md          every position, confidence, known vulnerability
  GLOSSARY.md           terms, with the one definition used everywhere
spec/
  PRODUCTION_BIBLE.md   this file
  STYLE_BIBLE.md        prose rules, anti-patterns, linter thresholds
  CHAPTER_BRIEFS.md     all 20 briefs
  AUDIO_SPEC.md         Miso pipeline, voice design, QC harness
research/
  ch-NN/evidence.md     claims + sources + confidence
  ch-NN/cases.md        candidate opening cases
  sources.bib
manuscript/
  ch-NN/draft-v1.md ... draft-v3.md
  ch-NN/frozen.md       immutable once frozen
reviews/
  ch-NN/referee.md      philosophical adversary
  ch-NN/redteam.md      AI-tell adversary
  ch-NN/listen-log.md   read-aloud findings
  ch-NN/decisions.md    Showrunner overrules, with reasons
audio/
  script/ch-NN.md       audio edition (differs from print — see AUDIO_SPEC)
  lexicon.tsv           print form → render respelling
  homographs.tsv        flagged words + resolution
  renders/ masters/
tools/
  lint.py               Gate 2
  asr_diff.py           audio QC harness
  render.py assemble.py
```

**Freeze discipline:** `frozen.md` is immutable. Changing a frozen chapter requires a Showrunner decision logged in `reviews/ch-NN/decisions.md` and a Continuity re-run on every subsequent chapter.

---

## 7. Standing instructions for every agent

1. **Never invent a citation, a quotation, a statistic, or a date.** If the evidence packet doesn't contain it, write around it or flag it. A fabricated source in a book about epistemic honesty is a project-ending error, not a small one.
2. **Never state a contested empirical claim at high confidence.** The framework's own Chapter 2 makes epistemic calibration a moral duty. The book must model it. Where the literature is genuinely divided, the text says so.
3. **Never write a summary section.** Not at the end of a chapter, not at the end of a part.
4. **Prefer cutting.** The prior draft's problem was volume, not scarcity. If a passage is not clearly earning its place, it goes.
5. **When the brief and the canon conflict, stop and ask the Canon Keeper.** Do not resolve it silently.
6. **Write in the Showrunner's voice, not a house voice.** First-person judgment passages are marked in the briefs; those get drafted as placeholders and rewritten by the Showrunner personally.
7. **One argument per chapter.** If you find yourself making a second one, flag it — it's probably a chapter that was scoped wrong.

---

## 8. Schedule shape

Sequential drafting means the critical path is ~20 chapters × (research + draft + 5 gates). Realistic per-chapter cycle is 2–4 days at sustained pace. Front-load the two hardest chapters — the Prologue and Chapter 10 (*Three Gates*) — because they establish the register at both extremes, narrative and technical, and everything after is written against them.

**Build order:**
1. `tools/lint.py` and `tools/asr_diff.py`. Before any prose.
2. `CANON.md`, `POSITIONS.md`, `GLOSSARY.md` finalized and frozen.
3. Prologue + Chapter 10, through full gates. Iterate the anchor voice prompts against these.
4. Everything else, in order.
5. Full audio render, assembly, master, listen-through.
6. Cut the gateway edition.
