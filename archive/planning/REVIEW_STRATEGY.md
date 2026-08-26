# Review Strategy — The Manual of Harmonious Rationality

**Purpose:** This document defines the comprehensive review protocol that must be completed before the 48-chapter manuscript is converted to a formatted PDF. The review is structured in seven sequential phases. Each phase has entry criteria, specific checks, concrete deliverables, and exit criteria. A phase is not complete until its exit criteria are met; a later phase does not begin until earlier phases are complete.

**Principle:** Review moves from **structural** (is the skeleton sound?) to **argumentative** (does the thinking hold?) to **textual** (is the prose doing its job?) to **editorial** (is it ready to print?). Reversing this order wastes work — polishing prose in a chapter whose argument still needs restructuring is labor that gets thrown away.

**Operator model:** Each phase is designed to be executable by a single reviewer (human or AI) with clear inputs and outputs. The reviewer should work phase-by-phase, completing all checks within a phase before moving on. Findings should be logged in a running `REVIEW_FINDINGS.md` file; significant issues should become tasks.

---

## Phase 0 — Pre-Review Inventory and Baseline

**Purpose:** Before reviewing anything, establish the ground truth of what currently exists. Most review failures come from reviewers operating on stale assumptions about the manuscript's state.

### Checks

1. **File inventory.** Enumerate every file in `Book/Drafts/`, `Book/Chapters/`, `Context/`, `Positions/`, `Debates/`, `Research/`. Confirm count matches BOOK_INDEX.md.
2. **Status map.** For each of CH-01 through CH-48: record current status (DRAFTED, FINAL, REVISION), word count, last modification date, and whether it has been summarized in BOOK_BIBLE.md.
3. **Cross-reference graph.** Extract every "Chapter N" / "CH-N" / "(Chapter N)" reference in every chapter. Build an adjacency list showing which chapters reference which.
4. **Position usage map.** For each POS-XXX, record which chapters are listed as arguing for it in POSITION_REGISTRY.md, and which chapters actually mention it.
5. **Source citation inventory.** Extract every book title and author mentioned in any chapter. Compare to the files in `Files/` to see which sources the book actually uses vs. merely name-drops.
6. **Epigraph inventory.** Every chapter opens with a quote. Record the quote, attributed author, and attributed work for each of the 48 chapters.

### Deliverable

A `Review/00_baseline.md` file containing:
- Chapter status table (48 rows)
- Cross-reference adjacency list
- Position → chapter map
- Sources cited → sources available table
- Epigraph list (48 entries)

### Exit criteria

- Every one of the 48 chapters has a status row.
- Every cross-reference has been extracted.
- The baseline file is stable (would not need to be re-run without new edits).

---

## Phase 1 — Structural Audit

**Purpose:** Verify the architectural integrity of the book before examining any individual argument in detail. Structural problems propagate; fix them first.

### 1A. Chapter-by-chapter presence and ordering

- Every chapter listed in BOOK_INDEX.md exists as a file.
- Every chapter file exists in BOOK_INDEX.md.
- Chapters are numbered sequentially with no gaps or duplicates.
- Book-level divisions in BOOK_INDEX.md match the book labels in the actual chapter files.

### 1B. Cross-reference resolution

For each cross-reference extracted in Phase 0:
- **Target exists.** "See Chapter 32" → Chapter 32 exists.
- **Target is correct.** "Chapter 32 (AI)" → Chapter 32 is actually about AI.
- **Direction is forward or flagged.** References to later chapters should only happen when necessary (forward-references are acceptable for setup but must not be load-bearing for a chapter's argument).
- **No dead links.** References to chapters that were renamed, renumbered, or deleted are flagged.

### 1C. Book-to-book connective tissue

Between-book transitions should be explicit. Check that:
- Book I → II transition is signaled (end of CH-05, start of CH-06).
- Book II → III (end of CH-08, start of CH-09).
- Book III → IV (end of CH-12, start of CH-13).
- Book IV → V (end of CH-16, start of CH-17).
- Book V → VI (end of CH-24, start of CH-25).
- Book VI → VII (end of CH-30, start of CH-31).
- Book VII → VIII (end of CH-35, start of CH-36).
- Book VIII → IX (end of CH-45, start of CH-46).

Each transition should tell the reader where they have been and where they are going. Missing or weak transitions are flagged.

### 1D. Position Registry completeness

- Every position referenced in a chapter is in the Registry.
- Every position in the Registry is referenced in at least one chapter.
- Confidence and vulnerability ratings are populated.
- HIGH-vulnerability positions have an in-chapter acknowledgment of their weakness (the framework is honest about what is fragile).

### 1E. BOOK_BIBLE coverage

- Every FINAL-status chapter has a bible entry.
- Every DRAFTED chapter that will be promoted should have at least a stub entry for the review phase.
- Bible entries match the current state of the chapter (not a stale earlier version).

### Deliverable

`Review/01_structural_audit.md` containing:
- List of all structural issues found, prioritized by severity (BLOCKER / SIGNIFICANT / MINOR)
- Resolution notes for each

### Exit criteria

- Zero BLOCKER issues (the manuscript structure is sound).
- All SIGNIFICANT issues have resolution plans logged.
- MINOR issues are logged but may be deferred to Phase 6.

---

## Phase 2 — Argument Integrity Review (Chapter-by-Chapter)

**Purpose:** For each of the 48 chapters, verify that the argument actually holds: premises are defended, conclusions follow, objections are addressed, and the chapter delivers what its opening promises.

### Per-chapter checklist

For each chapter, the reviewer answers:

1. **What is the core argument?** Stateable in 2–3 sentences.
2. **What is the argument's structure?** Premises → inferences → conclusion. Are the inferential steps valid?
3. **What are the key premises?** Each premise should either be defended in this chapter, defended in a referenced earlier chapter, or explicitly marked as axiomatic.
4. **Is the strongest opposing view steel-manned?** The chapter should present the best version of whatever it is arguing against, not a weak version.
5. **Is the strongest objection addressed?** Not just "an objection," but the strongest one a serious critic would raise.
6. **Are empirical claims supported?** Every empirical claim should either cite evidence or be marked as illustrative/anecdotal.
7. **Are the chapter's promises kept?** Chapters often promise ("this chapter will show that…"). The chapter must actually show what it promised.
8. **Does the conclusion follow?** The conclusion should not be stronger than the arguments support. Overclaim is a common failure mode in moral philosophy.
9. **Are direct quotes from primary sources present?** Per the project's documented standard, every chapter should include direct quotes from the sources it engages.
10. **Is the Known Weaknesses section honest?** Every chapter should acknowledge what it does not fully settle. Missing or dishonest Known Weaknesses sections are flagged.

### High-priority chapters for Phase 2

Some chapters carry more load than others. The following are especially important and should be reviewed first:

- **CH-01 (Third Way)** — sets the project; failures here compromise everything.
- **CH-03 (Valence Axiom)** — the foundational normative claim; weakness here propagates.
- **CH-09 and CH-10 (Dual-Process Ethics)** — the system's architecture; POS-A01 is HIGH vulnerability.
- **CH-24 (Policy Evaluation)** — the hinge chapter between political and economic books; recently expanded, needs verification.
- **CH-36 through CH-45 (Book VIII Defense)** — steel-manning quality is especially critical here.
- **CH-48 (Oath)** — the book's closing commitment; tone and substance must be exactly right.

### Deliverable

`Review/02_argument_integrity.md` — one section per chapter with:
- Core argument restated
- Issues found (by category: steel-manning, empirical support, inferential gap, missing quotes, dishonest weakness acknowledgment, overclaim)
- Severity rating
- Proposed fix

### Exit criteria

- Every chapter has been reviewed.
- Zero chapters with BLOCKER argument issues.
- SIGNIFICANT issues have fixes drafted.
- No chapter overclaims relative to its arguments.

---

## Phase 3 — Cross-Chapter Consistency and Terminology

**Purpose:** The book is a system, and systems break when the same concept gets defined or used differently in different places. This phase audits the whole book for consistency.

### 3A. Terminology consistency

Build a glossary of key terms by scanning the whole manuscript:

- **Foundational terms:** valence, constructivist realism, complex value vector, epistemic duty, performative incoherence.
- **Diagnostic terms:** Moloch, coordination failure, shadow of the future, Nash equilibrium, Schelling point, mechanism design.
- **Architectural terms:** Mode A / Mode B, Chesterton Fence, dual-process, the twelve virtues, instinct/reflection/habit, informed automaticity.
- **Political/economic terms:** subsidiarity, error-correction primacy, Hayekian knowledge test, Pigovian fit test, capability approach.
- **Position labels:** POS-M01, POS-A01, POS-P06, etc.

For each term: is it used consistently across all chapters? Is it defined once (ideally on first use) and then deployed without re-definition?

### 3B. Position consistency

For each position in the Registry:
- Does every chapter that invokes it use it in the same way?
- Are there contradictions between chapters — e.g., does one chapter invoke a strong form and another a weaker form of the same position?
- Does the language in the chapter match the language in the Registry?

### 3C. Argument consistency

This is the hardest check. Are there substantive contradictions between chapters? Examples of contradictions to watch for:
- CH-X says "rules should almost never be broken" and CH-Y treats a rule-break as routine.
- CH-X treats the veil-of-ignorance as accepted and CH-Y critiques it as incoherent.
- CH-X says "we are not utilitarian" and CH-Y makes an explicitly utilitarian inference.

Resolution options: (a) the contradiction is real and one side must change; (b) the contradiction is apparent only because of missing distinctions — add the distinction; (c) the contradiction is real but productive (flagged tension, not resolved) — mark it explicitly in both chapters.

### 3D. Tone consistency

The book's voice should be consistent: serious but not pompous, confident but not arrogant, engaged but not glib. Flag passages that drift into any of the failure modes:
- Academic jargon without payoff
- Informal asides that break the register
- Emotional appeals where argument is required
- False modesty or false certainty
- Contempt for rivals the book claims to steel-man

### 3E. Cross-reference accuracy

Re-run the Phase 1B check after Phase 2 changes: make sure revisions have not introduced broken cross-references.

### Deliverable

`Review/03_consistency.md` containing:
- Glossary of key terms with chapter-by-chapter usage
- List of terminological inconsistencies
- List of position inconsistencies
- List of argument contradictions (each with resolution)
- Tone flags by chapter

### Exit criteria

- Glossary is complete and consistent.
- Zero unresolved argument contradictions.
- Terminology is uniform across the manuscript.

---

## Phase 4 — Source, Citation, and Quote Verification

**Purpose:** Every empirical claim, every attributed quote, every historical reference, and every citation must be accurate. This is the factual integrity phase.

### 4A. Direct quote verification

For every direct quote in the manuscript:
- **Quote is accurate.** The text matches the source exactly (allowing for legitimate editorial ellipses).
- **Attribution is correct.** The author and work are correctly named.
- **Context is not distorted.** The quote is used in a way consistent with the original's meaning. Out-of-context quotes are a serious integrity failure and must be fixed.
- **Edition is documented.** For sources with multiple editions (e.g., translations of Aristotle), the specific edition used should be noted.

### 4B. Paraphrase verification

For every paraphrased argument ("Rawls argues that…"):
- **The author actually argued this.** Not something broadly in the tradition, not a later interpretation — the specific author's actual view.
- **Paraphrase is fair.** Does not strengthen or weaken the original author's claim.
- **Citation points to the right place.** Where possible, paraphrases should point to a specific work.

### 4C. Empirical claim verification

For every empirical or historical claim ("Ostrom's Valencia huertas achieved an infraction rate of 0.008 over 600 years"):
- **Claim is verified.** Source checked; number correct.
- **Source is authoritative.** Not a popular article's citation of a citation; the original study or primary record.
- **Claim has not been updated.** If subsequent research has revised the original finding, the revision is reflected.

### 4D. Epigraph verification

Every chapter opens with an epigraph. For each:
- The quote is accurate.
- The attribution is correct.
- The source work is correctly named.
- The quote is not apocryphal (famous quotes are often misattributed).

### 4E. Syllabus verification (CH-47)

Every book recommended in CH-47:
- Is a real book.
- Is by the attributed author.
- Has the attributed publication date.
- Is actually on the topic the syllabus says it is on.
- Is still available to readers (out-of-print editions should be noted).

### 4F. Registry source verification

Every work cited in POSITION_REGISTRY.md should be verified against the manuscript and the source file.

### Deliverable

`Review/04_citations.md` containing:
- Quote verification results (one row per quote: status OK / FIX / REMOVE)
- Paraphrase verification results
- Empirical claim verification results
- Epigraph verification results
- Syllabus verification results
- Any sources that cannot be verified with high confidence — flagged for removal or for additional research

### Exit criteria

- 100% of direct quotes verified.
- 100% of empirical claims with specific numbers verified or removed.
- Zero apocryphal epigraphs.
- Every book in CH-47 confirmed real and correctly attributed.

---

## Phase 5 — Steel-Manning and Vulnerability Audit

**Purpose:** The framework's claim to intellectual honesty depends on two things: (1) presenting rivals in their strongest form before critiquing them, and (2) honestly acknowledging the framework's own weaknesses. This phase audits both.

### 5A. Steel-man audit (Book VIII focus, but applies throughout)

For each rival system engaged (DCT, nihilism, utilitarianism, deontology, relativism, Rawlsian contractualism, virtue ethics, Marxism, natural law, and traditions in CH-45):

- **Is the steel-man presented before the critique?** Structural: the steel-man should come first, not be interleaved with critique.
- **Would a serious adherent of the rival recognize this as their view?** If a Kantian would say "that's not what Kant says," the steel-man has failed.
- **Is the steel-man presented as strongly as the author would present it?** The best version, not the average version.
- **Are the rival's strongest arguments specifically engaged?** Not ignored, not deflected — engaged.
- **Does the critique concede what can be conceded?** Acknowledgment of what the rival gets right is required before explaining what it gets wrong.

Reviewers for this phase should ideally include (or at minimum consult) someone sympathetic to the rival tradition being assessed. A Kantian should look at CH-39. A Rawlsian should look at CH-41. A Catholic natural law theorist should look at CH-44. If actual sympathetic reviewers are not available, the reviewer must explicitly adopt the rival's perspective as a discipline.

### 5B. Vulnerability audit

For every HIGH-vulnerability position in POSITION_REGISTRY.md:
- **Is the vulnerability acknowledged in the relevant chapter?** A HIGH-vulnerability position hidden behind confident prose is an integrity failure.
- **Is the current rebuttal stated, not merely referenced?** The reader should see what the defense is, even if the defense is incomplete.
- **Is the residual weakness named?** "This is as far as we can go today; here is what we would need to close it fully."

### 5C. Open question audit

Every item in `Context/OPEN_QUESTIONS.md` should be:
- Referenced in the chapter(s) where it is load-bearing.
- Not silently resolved — if a question has been answered, mark it resolved and update the relevant chapter. If it remains open, the chapter should acknowledge the openness.
- Not silently worsened — if new arguments have strengthened a previously weak objection, the chapter should reflect this.

### 5D. Known-weaknesses consistency

Each chapter's "Known Weaknesses" section in BOOK_BIBLE.md should match weaknesses acknowledged in-chapter. A chapter that presents itself as airtight but has honest weaknesses in the bible is dissembling.

### Deliverable

`Review/05_steelman_and_vulnerability.md` containing:
- Steel-man assessment per Book VIII chapter (with specific feedback from sympathetic perspective)
- Vulnerability acknowledgment per HIGH-vulnerability position
- Open question sync status
- Bible ↔ chapter weakness consistency check

### Exit criteria

- Every Book VIII chapter passes the "would a serious adherent recognize this?" test.
- Every HIGH-vulnerability position has in-chapter acknowledgment.
- Every open question is either resolved-and-noted or explicitly-still-open.

---

## Phase 6 — Prose, Readability, and Editorial Polish

**Purpose:** Now that the skeleton, arguments, citations, and steel-manning have been verified, the prose itself gets attention. This is the phase that determines whether the book is pleasant to read or a slog through valid arguments.

### 6A. Paragraph-level review

For each chapter:
- **Paragraph length variation.** Long paragraphs should be broken up unless they are doing real argumentative work. A 400-word paragraph with one argument inside it should probably become three paragraphs.
- **Paragraph topic sentences.** The first sentence of each paragraph should signal where that paragraph is going.
- **Transition quality.** Between paragraphs, the reader should be able to see why paragraph N+1 follows paragraph N.
- **Redundancy.** Repeated points within a chapter should be cut or consolidated. Some repetition across chapters is acceptable (and sometimes necessary), but within-chapter repetition is usually a flaw.

### 6B. Sentence-level review

- **Sentence length variation.** Long sentences and short sentences should alternate. Chapters that are all long sentences become unreadable; chapters that are all short sentences feel choppy.
- **Passive voice.** Passive where active is available should be changed. Passive is acceptable when the agent is genuinely unknown or irrelevant.
- **Jargon.** Technical terms should be used where they do real work. Jargon that is merely signaling seriousness without adding precision should be cut.
- **Hedging.** Epistemic humility is a virtue; epistemic cowardice is not. "This may possibly be the case, though of course it might not be, and reasonable people could disagree" is hedging beyond what the evidence demands.
- **Abstraction level.** Alternate between concrete examples and abstract formulations. Chapters that are all abstraction lose the reader; chapters that are all examples lose the argument.

### 6C. Chapter-level rhythm

- **Opening.** Does the chapter hook the reader in the first 200–300 words?
- **Development.** Does the argument build, or does it just list points?
- **Turn.** Good chapters have a moment where the argument turns — a surprise, a counterexample, a distinction that changes how the reader sees the topic. Flag chapters that lack this.
- **Closing.** The summary section should re-ground the reader and point forward.

### 6D. Epigraph fit

For each chapter's opening epigraph:
- Does it actually connect to the chapter's argument?
- Is it earning its place, or is it decorative?
- Is it the best available epigraph for this chapter?

### 6E. List and table quality

Tables and numbered lists should:
- Be used only where they add clarity (not as filler).
- Have parallel structure (every row the same grammatical form).
- Be concise (tables with long rambling cells defeat their own purpose).

### 6F. Reader experience check

For each chapter, the reviewer should ask: **would a smart, skeptical, philosophically literate reader who is not already convinced keep reading?** If the answer is no, the chapter needs work before it is the reader's problem.

### Deliverable

`Review/06_prose_and_editorial.md` containing:
- Per-chapter editorial notes
- Sentences/paragraphs flagged for rewriting
- Epigraphs flagged for replacement
- Redundancies flagged for cutting
- Chapters flagged for structural prose rework

### Exit criteria

- Every chapter has received a paragraph-level pass.
- Every chapter has received a sentence-level pass.
- No chapter has been flagged as "reader will stop here."
- No chapter exceeds a reasonable length unless its complexity justifies it.

---

## Phase 7 — Final Integration, Planning Document Sync, and PDF Preparation

**Purpose:** Make the manuscript ready for typesetting. All planning documents must match the manuscript; all chapters must be promoted from Drafts/ to Chapters/; all metadata must be correct.

### 7A. Planning document sync

- **BOOK_INDEX.md** reflects final chapter statuses, titles, positions.
- **BOOK_BIBLE.md** has an entry for every chapter matching its final state.
- **POSITION_REGISTRY.md** matches what the chapters actually argue, with confidence and vulnerability ratings current.
- **DECISIONS.md** has an entry for every significant decision made during review (substantial rewrites, position swaps, chapter restructurings).
- **OPEN_QUESTIONS.md** is current — resolved questions marked, remaining questions explicit.

### 7B. Draft promotion

Every chapter in `Book/Drafts/` that has passed all six prior phases is promoted to `Book/Chapters/`. Draft files are retained for audit.

### 7C. Front matter and back matter

For the PDF, the book needs:
- **Title page.** Title, subtitle (if any), author.
- **Dedication** (optional).
- **Epigraph** (book-level; optional).
- **Table of Contents.** Generated from BOOK_INDEX.md.
- **Preface or Foreword.** Explains what the book is, who it is for, how to read it.
- **Notes on the Position Registry and Self-Correction.** Essential — the reader needs to understand the architecture.
- **Bibliography.** Full citations for every source used. Can be generated from the syllabus in CH-47 plus additional sources cited in individual chapters.
- **Index of Positions** (POS-* reference).
- **Index of Key Terms.** Important for a 48-chapter book.
- **Index of Thinkers Engaged.** Secondary index for readers interested in specific traditions.
- **About the Author** (optional).
- **Colophon** (optional — typeface, production notes).

Each of these components must be drafted and reviewed before PDF conversion.

### 7D. Consistency of formatting

- **Chapter headers.** Every chapter uses the same heading hierarchy (# for title, ## for main sections, ### for subsections).
- **Epigraphs.** Every chapter's epigraph uses the same formatting.
- **Quotes.** Block quotes are formatted consistently.
- **Lists.** Bulleted and numbered lists use consistent conventions.
- **Cross-references.** A single format for internal references (e.g., "Chapter 17" consistently, not mixing "CH-17" and "Chapter 17").

### 7E. Length and pacing review

Before typesetting:
- Estimate total word count.
- Estimate total page count at intended typeface and trim size.
- Flag imbalances: e.g., if Book I averages 8,000 words per chapter and Book VIII averages 3,000 words per chapter, decide whether this reflects substance or neglect.

### 7F. Legal and permissions

- Every quoted passage should be within fair use, or permissions should be secured.
- Epigraphs from copyrighted works may require permissions depending on length and jurisdiction.
- Any illustrative material (diagrams, tables reprinted from sources) must be cleared.

### 7G. Final proofread

A full read-through by a reviewer who has not been doing the substantive review. Catches what familiar eyes miss.

### Deliverable

A clean manuscript ready for typesetting, plus:
- `Review/07_final_integration.md` — sign-off record for each chapter
- Front matter and back matter drafts
- Permissions log

### Exit criteria

- Every chapter in Chapters/ (not Drafts/).
- All planning documents in sync with Chapters/.
- Front and back matter drafted.
- Legal review complete.
- Fresh proofread complete.
- **The manuscript is ready for typesetting.**

---

## Phase 8 (Post-PDF) — Errata and Revision Track

**Purpose:** Even after PDF conversion, the framework treats itself as revisable. A public book that cannot be corrected when errors are found would contradict the Position Registry architecture.

### Ongoing

- Maintain an errata log.
- When a position is swapped (per the Registry protocol), flag whether the swap warrants a book revision.
- Track reader feedback that identifies specific errors.
- Plan for second editions or supplements as the system grows.

This phase is not blocking the initial PDF, but it should be set up before publication.

---

## Review Sequencing and Parallelism

Most phases are sequential — you cannot meaningfully audit arguments (Phase 2) before verifying that chapters exist and cross-reference correctly (Phase 1). Some phases permit parallelism:

- **Parallelizable:** Phase 4 (citation verification) can run in parallel with Phase 5 (steel-manning audit) because they touch different aspects.
- **Parallelizable within phase:** Phase 2 can be split across reviewers by chapter.
- **NOT parallelizable:** Phase 3 (consistency) requires Phase 2's findings; Phase 6 (prose) requires Phases 1–5 to be complete because revision from earlier phases would discard prose work.

Realistic order:
1. Phase 0 (short)
2. Phase 1 (short)
3. Phase 2 (long — most of the review time)
4. Phase 3 and Phase 4 in parallel
5. Phase 5
6. Phase 6 (long — second largest time sink)
7. Phase 7

---

## Review Roles

For a serious review, the following roles should be filled (possibly by the same person wearing different hats, but ideally not):

### Architect reviewer

Looks at structure, architecture, cross-references, consistency. Phase 1, 3, 7A.

### Argument reviewer

Goes deep on arguments, inferences, premises, conclusions. Phase 2.

### Adversarial reviewer

Tries to break the book. Especially the Book VIII defense chapters and HIGH-vulnerability positions. Phase 5.

### Citation reviewer

Verifies every quote, attribution, empirical claim. Phase 4.

### Editorial reviewer

Reads for prose, pacing, readability. Phase 6.

### Sympathetic rival reviewers (plural)

One per major rival tradition (Kantian, Rawlsian, utilitarian, natural law theorist, Marxist, religious ethicist, virtue ethicist, etc.). Phase 5A. These can be informal (friendly experts, online philosophy communities) or formal (paid external review).

### Fresh-eyes proofreader

Never reads the book until Phase 7G. Finds what the others have stopped seeing.

A review executed by one person wearing all seven hats is possible but produces lower quality than a distributed review. For a book of this scope and seriousness, distributing the work is worth the coordination cost.

---

## Risk Register

Risks that can derail the review:

### R1. Reviewer capture
The reviewer starts agreeing with the manuscript and stops noticing problems. Mitigation: adversarial review role (above); explicit checklists that force engagement with weaknesses; fresh reviewers for critical phases.

### R2. Phase-skipping under deadline pressure
"We don't need Phase 2, the arguments seem fine." Mitigation: treat phases as non-optional. A rushed review is worse than a delayed publication.

### R3. Revision whiplash
A late-phase edit reintroduces a problem that an earlier phase already fixed. Mitigation: when Phase 6 edits affect argument substance, re-run the relevant Phase 2 checks on the edited chapter.

### R4. Consistency drift during revision
Fixes to one chapter create contradictions with untouched chapters. Mitigation: after any substantive edit, re-run Phase 3 on affected chapters.

### R5. Review finding volume overwhelms capacity
Phase 2 generates hundreds of small issues and they cannot all be addressed. Mitigation: strict severity triage (BLOCKER / SIGNIFICANT / MINOR); BLOCKERs and SIGNIFICANTs must be resolved, MINORs can be deferred to Phase 8.

### R6. "Good enough" fatigue
After months of review, the reviewer stops fighting for quality and waves things through. Mitigation: short review sessions, breaks, external reviewers for final phases.

### R7. Scope creep during review
"While we're in here, let's add a section on…" Mitigation: new content requires a new planning document entry (DEC-XXX) and explicit prioritization against the review timeline. Feature freeze for the duration of the review.

---

## Definition of Done

The manuscript is ready for PDF conversion when:

1. Every one of the 48 chapters has passed Phases 1 through 6.
2. Every planning document (BOOK_INDEX, BOOK_BIBLE, POSITION_REGISTRY, DECISIONS, OPEN_QUESTIONS) reflects the final manuscript state.
3. Every chapter file is in `Book/Chapters/` (not Drafts/).
4. Front matter and back matter are drafted and reviewed.
5. Every direct quote is verified.
6. Every HIGH-vulnerability position has in-chapter acknowledgment.
7. Every rival system in Book VIII has been steel-manned to a level a serious adherent would recognize.
8. A fresh-eyes proofread has been completed.
9. The errata track is set up for Phase 8.
10. The review findings are archived in `Review/` for audit.

No shortcuts on any of these. A book that claims to be "the best possible moral system" must be reviewed with commensurate seriousness.

---

## Practical Checklist (Condensed)

For a reviewer who wants a single-page summary to run the review, here it is:

**Phase 0 — Baseline**
- [ ] Chapter status table built
- [ ] Cross-reference graph built
- [ ] Position → chapter map built
- [ ] Sources cited vs. available table built
- [ ] Epigraph list built

**Phase 1 — Structural Audit**
- [ ] All 48 chapters present and correctly numbered
- [ ] Zero broken cross-references
- [ ] Book-to-book transitions explicit
- [ ] Position Registry complete and consistent with chapters
- [ ] Bible entries exist for every chapter

**Phase 2 — Argument Integrity** (per chapter)
- [ ] Core argument restated in 2–3 sentences
- [ ] Inferential steps verified
- [ ] Strongest opposing view steel-manned
- [ ] Strongest objection addressed
- [ ] Empirical claims supported
- [ ] Chapter promises kept
- [ ] Direct quotes from primary sources present
- [ ] Known Weaknesses honest

**Phase 3 — Consistency**
- [ ] Glossary built and uniform
- [ ] No position contradictions across chapters
- [ ] No argument contradictions (or explicitly flagged tensions)
- [ ] Tone consistent

**Phase 4 — Citation Verification**
- [ ] Every direct quote verified against source
- [ ] Every paraphrase checked for fairness
- [ ] Every empirical claim verified
- [ ] Every epigraph verified
- [ ] CH-47 syllabus verified

**Phase 5 — Steel-Manning and Vulnerability**
- [ ] Book VIII chapters would be recognized by serious adherents
- [ ] HIGH-vulnerability positions acknowledged in-chapter
- [ ] Open questions synced

**Phase 6 — Prose and Editorial**
- [ ] Paragraph-level pass complete per chapter
- [ ] Sentence-level pass complete per chapter
- [ ] Redundancies cut
- [ ] Epigraphs earning their place
- [ ] Reader experience check passed per chapter

**Phase 7 — Final Integration**
- [ ] Planning documents synced
- [ ] Chapters promoted to Chapters/
- [ ] Front matter drafted
- [ ] Back matter drafted
- [ ] Formatting consistent
- [ ] Permissions cleared
- [ ] Fresh-eyes proofread complete

**Phase 8 — Post-PDF**
- [ ] Errata track set up

When every box is checked, the manuscript is ready for typesetting.
