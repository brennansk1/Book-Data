# The Manual of Harmonious Rationality — Project Operating Manual

## Mission
Build the **best possible moral system** — one rigorous enough to defeat rival systems in head-to-head debate, comprehensive enough to cover morality, politics, and economics in full depth, and practical enough to be fully lived by a real person.

The Framework (`Framework.md`) is the **seed**, not the ceiling. The system should grow far beyond it. If research reveals a better position on any topic, **swap it in**. The goal is truth, not loyalty to the starting document.

## Directory Structure

```
Book Data/
├── CLAUDE.md                ← You are here. Master operating manual.
├── Framework.md             ← The seed document (v12.0). Starting point only.
├── Files/                   ← Reference materials (PDFs/EPUBs from user)
├── Research/                ← Notes extracted from reference materials
│   └── {source-name}.md
├── Positions/
│   └── POSITION_REGISTRY.md ← Every stance the system takes, versioned & rated
├── Book/
│   ├── BOOK_INDEX.md        ← Master TOC + chapter status + position links
│   ├── BOOK_BIBLE.md        ← Living summary of every chapter (context bridge)
│   ├── Chapters/            ← Final chapter files (CH-01.md ... CH-48.md)
│   └── Drafts/              ← Work-in-progress before promotion
├── Debates/                 ← Deep comparative analyses vs rival systems
│   └── vs-{system}.md
├── Context/
│   ├── DECISIONS.md         ← Audit trail of every philosophical choice
│   └── OPEN_QUESTIONS.md    ← Unresolved tensions + material requests
└── WORKFLOW.md              ← Execution protocol
```

## The Position Swap System

This is the core innovation that makes the system self-correcting:

1. **Every substantive claim** is registered in `Positions/POSITION_REGISTRY.md`
2. Each position has a **confidence rating** and **vulnerability rating**
3. When writing a chapter, you must **stress-test** every position it depends on
4. If you find a stronger position during writing or research:
   - Register the new position in the Registry
   - Move the old one to the Archive with an explanation
   - Update `Context/DECISIONS.md` with the swap rationale
   - Revise all chapters that depend on the old position
   - Update `BOOK_BIBLE.md` for every affected chapter
5. **PROVISIONAL** and **EXPLORATORY** positions are expected to change
6. Even **STRONG** positions can be replaced if the evidence warrants it

## Key Rules

### Context Management
1. **Always read `BOOK_BIBLE.md` before writing or revising any chapter.** Non-negotiable.
2. **Always read `POSITION_REGISTRY.md` before writing.** Know what the system currently claims.
3. **Update BOOK_BIBLE.md immediately after completing any chapter** (150-300 word summary).
4. **Update BOOK_INDEX.md** when any chapter's status changes.

### Philosophical Standards
5. **The Framework is a seed, not scripture.** Go beyond it. Contradict it when warranted. The framework doesn't cover consciousness, animal ethics, disability, non-Western traditions, digital economy, intergenerational justice, or dozens of other critical topics. **You are expected to develop positions on all of these.**
6. **Steel-man before attacking.** Present the strongest version of any rival view before engaging it.
7. **Every position must survive the "swap test."** After writing a position, ask: "Is there a stronger version of this I'm not seeing? Would a smart opponent beat me here?" If yes, find the stronger position.
8. **No sacred cows.** If the framework says X but the best arguments say Y, go with Y and document why.
9. **Log every significant philosophical choice** in `Context/DECISIONS.md`.
10. **Flag weaknesses honestly.** If a position is vulnerable, say so in the Registry. Intellectual honesty is the system's greatest asset.

### Quality Standards
11. Every major claim needs an **argument**, not just an assertion.
12. Every chapter must **anticipate and address** the strongest objection.
13. Use concrete **examples and thought experiments**, not just abstractions.
14. **Write for a smart, skeptical reader** — philosophical literacy, no prior rationalist commitment.
15. Connect every chapter to the larger **web** of the system. No orphan arguments.

### Expansion Protocol
16. When writing any chapter, actively ask: "What does the framework NOT say about this topic that it should?"
17. If you identify a gap, add it to the **Expansion Zones** table in `BOOK_INDEX.md`.
18. If a gap is important enough, propose a new chapter and add it to the Index.
19. When expanding, maintain coherence with the foundations (Book I) but don't let the foundations artificially constrain applied conclusions.

### Material Requests
20. If a chapter needs reference material, add a request to `Context/OPEN_QUESTIONS.md`.
21. Continue writing what you can without it. Mark gaps as `[PENDING: material-name]`.
22. When material is provided in `Files/`, process it into `Research/` notes first, then use those notes.

## Chapter Writing Protocol

```
1. READ      → BOOK_BIBLE.md + POSITION_REGISTRY.md + BOOK_INDEX.md
2. READ      → DECISIONS.md + OPEN_QUESTIONS.md
3. READ      → Any Research/ notes relevant to this chapter
4. THINK     → What does the framework say? What doesn't it say? What should it say?
5. DRAFT     → Write in Book/Drafts/
6. TEST      → Stress-test every position. Ask: "What would [opponent system] say?"
7. IMPROVE   → Strengthen weak arguments. Swap positions if needed.
8. PROMOTE   → Move to Book/Chapters/ when satisfied
9. UPDATE    → Bible, Index, Registry, Decisions, Open Questions
10. REPORT   → Tell user what was written, what changed, what's next, what's needed
```

## Competitive Design Principles

This system is being built to **win**. That means:

- **Against Utilitarianism:** We must show why our dual-process architecture avoids the repugnant conclusion, utility monsters, and demandingness objections while preserving consequentialism's strengths.
- **Against Deontology:** We must show why our rules are better grounded (game theory, not intuition or divine command) and why having an override mechanism handles the hard cases Kant cannot.
- **Against Virtue Ethics:** We must show we take character seriously (Book III) while also providing decision procedures that virtue ethics lacks.
- **Against Divine Command:** We must show that our grounding (valence realism + game theory) is more verifiable and less arbitrary.
- **Against Nihilism:** We must show that the denial of value is performatively incoherent and empirically false.
- **Against Relativism:** We must show that moral systems can be objectively compared on empirical grounds (coordination success, suffering reduction, flourishing metrics).
- **Against Contractualism:** We must engage Rawls seriously — the veil of ignorance is close to our insurance argument but we may need to absorb some of it.
- **Against Marxism:** We must engage with exploitation, alienation, and structural critique without dismissing them — and show where our system handles these better.
- **Against Non-Western Systems:** We must not just defeat but genuinely learn from Confucian, Buddhist, Ubuntu, and other traditions. The system is weaker if it remains parochially Western.

The system wins not by being the loudest, but by being the most honest, the most comprehensive, and the most willing to incorporate the best ideas from everywhere.
