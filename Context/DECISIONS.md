# Philosophical Decisions Log

Every major philosophical choice is recorded here with rationale. This prevents re-litigating settled questions and provides an audit trail of the system's evolution.

**Format:**
```
### DEC-XXX: [Decision Title]
**Date:** YYYY-MM-DD
**Context:** [What prompted this decision]
**Decision:** [What was decided]
**Alternatives Rejected:** [What else was considered and why it lost]
**Implications:** [What this means for the rest of the system]
**Positions Affected:** [POS-XXX references]
```

---

### DEC-001: System Name — "Constructivist Realism"
**Date:** 2026-03-26
**Context:** The framework needed a name that distinguishes it from existing positions.
**Decision:** Retain "Constructivist Realism" from the Framework as a working name. Values are constructed by agents but constrained by objective reality (biology, game theory, physics).
**Alternatives Rejected:**
- "Rational Ethics" — too generic
- "Harmonious Rationality" — good subtitle, not specific enough as a philosophical label
- "Cooperative Realism" — considered but doesn't capture the constructivist element
**Implications:** The name must be defended in CH-01. We must show it is genuinely distinct from moral realism and constructivism. **Name is provisional — may change if the system evolves beyond its original framing.**
**Positions Affected:** POS-M01

### DEC-002: Book Structure — 48 Chapters in 9 Books
**Date:** 2026-03-26
**Context:** Original 20-chapter design was too compressed. Politics had 1 chapter, economics had 1 chapter. Not enough to build a comprehensive, debatable system.
**Decision:** Expand to 48 chapters across 9 books:
- Book I (5 ch): Foundations
- Book II (3 ch): Game Theory / Coordination
- Book III (4 ch): Moral Architecture
- Book IV (4 ch): Personal Ethics
- Book V (8 ch): Political Philosophy
- Book VI (6 ch): Economic Philosophy
- Book VII (5 ch): Frontier Problems
- Book VIII (10 ch): Defense Against Rival Systems
- Book IX (3 ch): Synthesis
**Alternatives Rejected:**
- 20 chapters — too compressed for political and economic depth
- Separate volumes for politics/economics — loses the argument that these derive from the same foundations
**Implications:** Longer project but much more comprehensive and defensible. Each chapter targets 5,000-8,000 words. Total: ~240,000-384,000 words.
**Positions Affected:** All

### DEC-003: Framework as Seed, Not Scripture
**Date:** 2026-03-26
**Context:** The Framework (v12.0) is strong but incomplete. It doesn't address consciousness, animal ethics, non-Western traditions, digital economy, intergenerational justice, or many other critical topics.
**Decision:** The Framework is explicitly treated as a starting point. Claude is expected to:
- Develop positions on topics the Framework doesn't cover
- Replace Framework positions when better ones are found
- Engage with traditions the Framework ignores
- Document all changes in this log and the Position Registry
**Alternatives Rejected:**
- Strict adherence to Framework — would produce an incomplete and possibly wrong system
- Ignoring the Framework — would lose the valuable starting structure
**Implications:** The final book may differ substantially from v12.0. The Position Registry and this Decision Log are the mechanisms that ensure changes are principled, not arbitrary.
**Positions Affected:** All

### DEC-004: Position Swap System
**Date:** 2026-03-26
**Context:** A moral system that can't update is no better than dogma. Need a formal mechanism for changing positions when better ones are found.
**Decision:** Every substantive claim is registered in `Positions/POSITION_REGISTRY.md` with confidence and vulnerability ratings. Positions can be deprecated and replaced via the Swap Protocol, with full audit trail.
**Alternatives Rejected:**
- No formal system — leads to drift and inconsistency
- Version control only (git) — too granular, doesn't capture philosophical reasoning
**Implications:** This is the system's core claim to intellectual honesty: "We have positions, not dogmas. Every stance is held provisionally, with explicit confidence levels and known weaknesses."
**Positions Affected:** All
