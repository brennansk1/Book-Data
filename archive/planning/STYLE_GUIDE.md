# MHR Second Edition — Master Style Guide

**Authority:** This document governs the full-book rewrite (Second Edition). Where it conflicts with older Review/ files, this document wins. Where a chapter's current text conflicts with it, rewrite the chapter.

## The Problem Being Fixed

The first edition grew by accretion. Chapters were drafted, then audited, then patched: a "What Moloch Cannot Explain" section bolted on here, an "Honest Assessment" appended there, a steelman inserted after the fact. The seams show. Sections read as responses to internal review notes rather than as parts of one argument. Headers meta-narrate the book's own process ("The Question That Organizes This Book") instead of teaching the subject.

The second edition must read as if a single author conceived each chapter whole — a definitive textbook of a complete moral system, written with the narrative confidence of Robert Greene and the intellectual honesty the system claims as its greatest asset.

## The Chapter Template

Every chapter follows this arc. Do not label the parts with these names; the structure should be felt, not announced.

1. **The Opening Case (500–900 words).** Begin with a concrete story told as narrative: a historical episode, a person, a decision, a disaster or triumph. Not a hypothetical, not a definition. Melos before the Athenians. Semmelweis and the maternity wards. Ostrom's Alanya fishermen. The Cuban Missile Crisis back-channel. Tell it with dates, names, stakes, and texture — then turn: *what happened here, and why does it keep happening?* The case must genuinely embody the chapter's principle, and the chapter should return to it at least once.

2. **The Principle.** State the chapter's central claim in one or two forceful paragraphs — the "law" of the chapter. This is the thesis a reader should be able to recite a year later.

3. **The Argument.** Build the case in ordered sections with substantive, declarative headers ("Bad Equilibria Can Be Stable," not "Section Overview" or "Introduction"). Every major claim gets an argument; every abstraction gets an example within a paragraph or two. Weave in at least two more real-world or historical cases, integrated into the argument's flow — not bullet-listed "modern examples are everywhere" inventories. Convert lists into prose wherever the list is really an argument. (Occasional short lists are fine when the content is genuinely enumerable — conditions, criteria, rules.)

4. **The Strongest Objection.** Steel-man the best objection *as its proponent would state it*, with a named opponent where one exists, then answer it. If the answer is incomplete, say so plainly — that honesty is the system's signature. One integrated objection section beats three scattered caveats.

5. **The Honest Ledger.** Where the chapter defends a position rated PROVISIONAL or HIGH-vulnerability in the Position Registry, the chapter text must say so and name the open weakness. Never let the prose be more confident than the Registry.

6. **The Close.** Return to the opening case or image, restate the principle now earned, and hand off to the next chapter in one or two sentences. End with **Chapter Summary** — a titled section of 150–250 words in flowing prose (no bullets) that a student could use for review, followed by nothing else.

## Voice

- Second-person address is permitted but rationed; the default is confident third-person exposition.
- Greene-style cadence: short declarative sentences at moments of thesis; longer periodic sentences for development. Aphoristic capstones are encouraged ("Rationality is not enough. The structure of the situation traps them.") — roughly one or two per section, not per paragraph.
- No hedging filler ("it could perhaps be argued"). When uncertain, state the uncertainty as a fact about the world or the system, not as authorial throat-clearing.
- No meta-commentary about the book's own drafting, audits, registry mechanics, or "this section will…" signposting. The Registry may be *referred to* where the system's self-correction is itself the topic (CH-01, CH-47), and confidence levels may be named in the Honest Ledger, but chapters never narrate the writing process.
- Define every technical term at first use, in-line, with an example. Assume a smart, skeptical reader with no rationalist background.

## Quotes (required)

Every chapter carries **at least three direct quotations** from primary sources, formatted as block quotes with author and work attribution, integrated at the point where they do argumentative work.

**Absolute rule: never fabricate or approximate a quotation.** Use only (a) quotes already present in the project's chapters/Research files, or (b) quotations you are certain of verbatim (canonical passages: Hume's is-ought, Nietzsche §125, Smith's invisible hand, Mill's On Liberty, etc.). If you cannot source a quote confidently, paraphrase with attribution instead ("As Korsgaard argues in *The Sources of Normativity*, …"). A paraphrase is never formatted as a quotation.

## Audiobook constraints (the text will be read aloud by TTS)

- **No tables.** Convert any table into prose or a short list. (The TTS pipeline skips tables entirely — a table is content that vanishes from the audiobook.)
- No footnotes; put the material in the text or cut it.
- Citations spoken-friendly: "(*A Theory of Justice*, Section 11)" not "(Rawls 1971: 60–65)".
- Avoid ASCII diagrams, math notation beyond simple arithmetic, and long parenthetical URL/code strings.
- Chapter H1 must keep the exact format: `# Chapter N: Title — Subtitle` (the audiobook script parses it).

## Length and cross-references

- Target 3,800–5,500 words per chapter (Book IX chapters may run shorter).
- Cross-reference chapters as "Chapter N" using the **new** numbering (the authoritative list is in Revision/CHAPTER_MAP.md). Never cite a chapter by its old number.
- Each chapter must connect to the web: at least two explicit links backward or forward to other chapters, integrated in prose.
