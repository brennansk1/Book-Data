# Execution Workflow

## Phase 1: Architecture (COMPLETE)
- [x] Design sandbox structure
- [x] Create all system files
- [x] Build position registry with swap mechanism
- [x] Design comprehensive chapter outline (48 chapters, 9 books)
- [x] Identify expansion zones
- [ ] Get user approval on design before proceeding

## Phase 2: Foundations (Book I — Chapters 1-5)
Write the metaphysical and epistemic bedrock. These must be airtight because every later chapter depends on them.

**Priority Order:** CH-01 → CH-03 → CH-02 → CH-04 → CH-05
- CH-01 first (introduces the whole project)
- CH-03 next (valence realism is the most critical axiom)
- CH-02 (epistemology — needed before game theory)
- CH-04 (evolution — needed before applied ethics)
- CH-05 (consciousness — hardest and newest; may require material requests)

**Stress Test:** After all 5 are drafted, re-read as a unit and attack from every rival system's perspective. Fix weaknesses before moving on.

## Phase 3: The Enemy (Book II — Chapters 6-8)
Game theory and coordination failure. This is the "engine" that powers the system's applied recommendations.

**After Phase 3 Checkpoint:** The core theoretical apparatus (foundations + game theory) should be solid enough to derive specific positions. Stress-test by asking: "Can I derive the political and economic positions from these foundations alone, or am I smuggling in unjustified assumptions?"

## Phase 4: The Architecture (Book III — Chapters 9-12)
The decision-making framework. Dual-process ethics, virtues, moral development.

**Key Risk:** The Mode A/B threshold (POS-A01) is rated HIGH vulnerability. This phase must resolve or substantially strengthen it.

## Phase 5: Personal Ethics (Book IV — Chapters 13-16)
Apply the system to individual life. This is where the "livability" test hits hardest.

**Livability Test:** After each chapter, ask: "Would a real person actually follow this? If not, is the problem with the person or with the system?" Be honest.

## Phase 6: Political Philosophy (Book V — Chapters 17-24)
The **comprehensive** political theory. 8 full chapters. Not a summary — a real political philosophy.

**Phase 6 Protocol:**
1. Before writing each chapter, check if the Framework's position on this topic is the best available or if research suggests something stronger
2. Identify at least 3 serious rival positions on each political topic
3. If the framework is silent on a topic (e.g., immigration, drug policy, criminal justice reform), develop a position from first principles and register it
4. After all 8 chapters: run the "policy gauntlet" — pick 10 contentious real-world policy debates and verify the system gives coherent, defensible answers

## Phase 7: Economic Philosophy (Book VI — Chapters 25-30)
The comprehensive economic theory. 6 full chapters.

**Phase 7 Protocol:**
1. Same as Phase 6 but for economics
2. Pay special attention to where the framework's libertarian-leaning defaults may need modification
3. After all 6 chapters: run the "economy gauntlet" — pick 10 real economic debates (minimum wage, trade policy, healthcare, housing, etc.) and verify coherent answers

## Phase 8: The Frontier (Book VII — Chapters 31-35)
Where the system meets unprecedented challenges. These chapters have the most PROVISIONAL positions.

**Expansion Protocol:** During this phase, actively propose new chapters or expansion zones for topics the framework never anticipated. Add them to the Index.

## Phase 9: Defense (Book VIII — Chapters 36-45)
Head-to-head debates with every major rival system. This is the stress test for the entire book.

**Phase 9 Protocol:**
1. Write the Debate files in `Debates/` first (deep research)
2. Then write the chapter versions (more accessible)
3. If any debate reveals a fatal weakness, **stop and fix the weakness before continuing** — even if it means revising foundation chapters
4. CH-45 (The Synthesis) must honestly acknowledge what we took from each rival system

## Phase 10: Synthesis (Book IX — Chapters 46-48)
Tie it all together.

## Phase 11: Integration Sweep
- Re-read entire BOOK_BIBLE.md end-to-end
- Identify and resolve any remaining contradictions
- Verify all cross-references
- Check that every PROVISIONAL position has been upgraded or explicitly defended as provisional
- Verify every Expansion Zone has been addressed or explicitly deferred

## Phase 12: Adversarial Review
- For each rival system, verify the debate chapter actually addresses their strongest arguments
- Invite the user to challenge specific positions
- Look for "convenient" positions where we may have chosen what's comfortable over what's true

---

## Per-Session Protocol

```
1. READ      → BOOK_BIBLE.md + POSITION_REGISTRY.md + BOOK_INDEX.md
2. READ      → DECISIONS.md + OPEN_QUESTIONS.md
3. ORIENT    → What's the next highest-priority task?
4. WRITE     → One chapter (or revise one chapter)
5. TEST      → Stress-test positions. Check for contradictions.
6. SWAP      → If a better position was found, execute the swap protocol
7. UPDATE    → Bible, Index, Registry, Decisions, Open Questions
8. REPORT    → What was done. What changed. What's next. What's needed.
```

## The Swap Protocol (When a Position Changes)

This is triggered whenever a better position is discovered during writing or research:

```
1. IDENTIFY  → Name the old position and the proposed replacement
2. ARGUE     → Write out why the new position is superior (in DECISIONS.md)
3. REGISTER  → Add new position to Registry, archive old one
4. TRACE     → Find every chapter that depends on the old position (use Registry links)
5. REVISE    → Update each affected chapter
6. UPDATE    → Update BOOK_BIBLE.md for every revised chapter
7. VERIFY    → Check that no new contradictions were introduced
```

## Material Request Protocol

```
1. IDENTIFY  → What specific material is needed and why
2. LOG       → Add to OPEN_QUESTIONS.md with chapter link and specificity
3. CONTINUE  → Write what you can. Mark gaps as [PENDING: material-name]
4. PROCESS   → When material arrives, extract notes to Research/{source}.md
5. INTEGRATE → Fill in [PENDING] sections and update positions if warranted
```

## Reference File Processing Protocol

When the user provides files in `Files/`:

### PDF Files
- Read directly with the Read tool (up to 20 pages per request)
- For large PDFs: read in page-range chunks (1-20, 21-40, etc.)
- Extract to `Research/{source-name}.md` with:
  - Key arguments and their structure
  - Direct quotes with page numbers
  - Data, examples, and thought experiments
  - How it relates to our positions (supports, challenges, or extends)

### EPUB Files
- Extract with: `unzip -o "Files/{name}.epub" -d "Files/{name}_extracted/"`
- Read the content files (usually in OEBPS/ or similar directory)
- Process into `Research/{source-name}.md` same as PDFs

### Articles / Other Formats
- Read directly if plain text or HTML
- Process into Research/ notes same as above

### Research Note Format
```markdown
# Research Notes: {Title} by {Author}

## Overview
[1-2 paragraph summary of the work's main thesis]

## Key Arguments
### [Argument 1 Name]
- [Summary]
- [Direct quote if important] (p. XX)
- [Relevance to our system: supports/challenges POS-XXX]

## Useful Examples & Thought Experiments
- [Example with page ref]

## Potential Position Impacts
- [POS-XXX]: [How this material affects our position]

## Quotes to Use
- "[Quote]" (p. XX) — useful for [chapter/topic]
```
