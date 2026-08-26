# Style Bible

Read this before writing a single sentence. The thresholds in §6 are enforced by `tools/lint.py` and fail the build.

---

## 1. The register we're writing in

A person who has thought carefully about something difficult, explaining it to an intelligent friend who has not. Confident where confidence is earned, openly uncertain where it isn't, occasionally funny, never showing off.

The register we are **not** writing in: the framework document, the executive summary, the encyclopedia entry, the LinkedIn essay, the textbook.

The distinction is testable. Framework prose *announces its structure* — it tells you what it's about to do, does it, then tells you what it did. Book prose *has* structure and doesn't mention it.

---

## 2. The eleven rules

**1. Open every chapter with a case, never a thesis.** A person, a decision, a specific difficulty, in a place, at a time. The argument emerges from the case. If a chapter opens with "This chapter examines…" or "Before we can understand X, we must first…", it has failed before the second sentence.

**2. One argument per chapter,** statable in one sentence you could say out loud without a subordinate clause. It appears in the brief. If the chapter is making two, it's two chapters or one of them is padding.

**3. Objections are people, not headers.** Not "Objection 1: the egoist reply." Instead: someone real or plausibly real says the thing, gets a genuinely fair hearing — the strongest version, not a straw one — and is answered. Every chapter has at least one named interlocutor.

**4. No summary sections. Ever.** Not "Summary," not "What This Chapter Established," not "In this chapter we have seen." If the argument needs a recap, it was built wrong.

**5. One list per chapter maximum. Zero is better.** This is the hardest rule and the most consequential. The five override conditions and the three procedural gates must be prose. Prose forces you to explain why each item follows from the one before — information a list hides. Nested lists are banned outright.

**6. Headers earn their place.** Two per chapter maximum. A header every 500 words is the surest sign of framework register.

**7. First person singular for judgment calls.** "I think the fourth condition does the real work, and I'm less sure about the fifth" beats "the framework holds that…" The institutional "we" is evasive and readers hear it as evasive. Use "we" only for genuine joint reasoning with the reader ("suppose we run the case again, but…").

**8. Concrete particularity quota.** Every chapter contains at least three distinct real people, named, doing something specific. Elinor Ostrom walking the Valencia huerta. Robert Axelrod opening submissions to his tournament. Not "researchers have found."

**9. Modulate confidence audibly.** The prior draft stated a bare axiom and a contested labour-economics literature at identical pitch. Vary it explicitly and often: *I'm confident about this. I'm much less sure here. I don't know, and I don't think anyone does.* This is the single fastest way to earn a skeptical reader.

**10. Write for a breath.** If you cannot say the sentence aloud in one breath, the TTS cannot either, and the reader's inner ear can't. Sentences that need three subordinate clauses before the main verb get rebuilt.

**11. End paragraphs on the strong beat.** The last clause of a paragraph is the one the reader hears. Don't spend it on a qualifier. Move the hedge into the middle of the paragraph or the start of the next one.

---

## 3. Banned constructions

Hard bans. The linter flags all of these.

| Banned | Why |
|---|---|
| "It's not just X, it's Y" | LLM tell, near-universal |
| "Not X, but Y" as a rhetorical frame | Overused to the point of tic; max 2 per chapter |
| Three-item parallel lists in a sentence (tricolon) | Max 3 per chapter; the prior draft used them constantly and they become audible in TTS within twenty minutes |
| "Let us be precise about…" / "Let us examine…" / "Consider the following" | Throat-clearing; signposts structure |
| "The key insight is…" / "The crucial point is…" | If it's key, the sentence should demonstrate that |
| "In this chapter we will…" | See rule 4 |
| "It's worth noting that…" / "Importantly," / "Notably," | Delete the phrase; keep the sentence |
| "This is not X — it is Y" as a paragraph closer | Same tic as above, in closing position |
| "delve," "tapestry," "landscape" (figurative), "navigate" (figurative), "underscore," "multifaceted," "nuanced" (as praise), "robust" (outside statistics), "leverage" (verb), "at its core," "fundamentally," "profound" | LLM vocabulary signature |
| "The framework holds/argues/maintains" | See rule 7 |
| Em-dash stacking (2+ in one sentence) | Max 4 em-dashes per 1,000 words |
| Rhetorical question followed immediately by its answer, more than twice per chapter | Cheap momentum |
| Sentences beginning with a nominalization ("The recognition that…", "The realization that…") | Abstract-noun subjects; rebuild around a person or a verb |

---

## 4. Worked examples

**Framework register (from the prior draft):**

> Let us be precise about what we are trying to build. Mode B is not "use consequentialism whenever you think the stakes are high." That is the slippery slope. Mode B is specifically for cases where:
> 1. Following the rule would produce catastrophic, irreversible harm…

**Book register:**

> The obvious objection to a rule is that rules are stupid. They don't know what's happening. A rule against lying doesn't know there's a man with a knife on your porch asking where your sister went.
>
> So there has to be an exception. The trouble is that everyone who has ever done something terrible believed, at the moment of doing it, that they were in the exception. That is not a rhetorical flourish; it is close to a historical universal. The bureaucrat signing the deportation order, the executive burying the safety report, the officer who fired first — none of them thought of themselves as breaking a rule for convenience. Each of them had a reason, and the reason felt enormous at the time.
>
> Which means the interesting question is not *when may I break the rule*. It's *how would I know*.

Note what changed: the case arrives first, the objection is voiced rather than labelled, real actors appear, the list is gone, the paragraph ends on the strong beat, and the chapter's actual argument is now a question the reader wants answered.

---

**Weak (abstract subject, buried verb, hedged closer):**

> The recognition that institutional structures encode accumulated wisdom is an important consideration that should perhaps inform our approach to reform in most cases.

**Strong:**

> Chesterton's point was that the fence is evidence. Somebody built it, at cost, for a reason. You may not be able to see the reason from where you're standing — but the fence is still evidence, and "I can't see why this is here" is a fact about you before it's a fact about the fence.

---

## 5. Handling quotations

- **Attribution before the quote, always.** "Chesterton put it this way:" then the quote. Never quote-then-attribute; in audio the listener doesn't know they're in a quotation until it ends.
- **Under 25 words** unless the exact wording is doing real work.
- **One quote per source per chapter.** If you want a second thing from Ostrom, paraphrase it.
- **Never use a quotation as an argument.** A quotation shows how someone put it. It doesn't establish that they were right.
- **Every quote in the evidence packet with exact wording, work, year, page** before it enters a draft. No exceptions, no reconstruction from memory.

---

## 6. Linter thresholds (Gate 2)

`tools/lint.py` computes these per chapter. Any hard fail blocks the build.

| Metric | Target | Hard fail |
|---|---|---|
| Word count | 4,000–4,800 | <3,200 or >5,600 |
| Mean sentence length | 15–20 words | >24 |
| Sentence length SD | ≥ 9 | < 7 |
| Sentences under 8 words | ≥ 8% | < 4% |
| Sentences over 40 words | ≤ 2% | > 5% |
| Mean paragraph length | ≤ 110 words | > 150 |
| Longest paragraph | ≤ 200 words | > 260 |
| Headers | ≤ 2 | > 3 |
| Lists | ≤ 1 | > 1, or any nested list |
| Distinct named real people | ≥ 3 | < 2 |
| First-person singular ("I") | ≥ 5 | < 3 |
| Explicit confidence modulation | ≥ 2 | 0 |
| Em-dashes per 1,000 words | ≤ 4 | > 7 |
| Tricolons | ≤ 3 | > 5 |
| "not X but Y" frames | ≤ 2 | > 4 |
| Banned-phrase hits (§3) | 0 | ≥ 1 |
| Sentences opening with nominalization | ≤ 2 | > 5 |
| Passive voice rate | ≤ 12% | > 18% |
| Repeated 6-grams vs. frozen chapters | 0 | ≥ 1 |

### Additional thresholds from `VOICE.md`

| Metric | Target | Hard fail |
|---|---|---|
| Paragraph length SD | ≥ 45 | < 30 |
| One-sentence paragraphs | ≥ 2 | 0 |
| Paragraphs over 160 words | ≥ 1 | 0 |
| Explicit connective openers (However/Moreover/Furthermore/Additionally/That said) | ≤ 4 | > 8 |
| Plain-band words (thing, stuff, mess, bad, weird, big, awful, gets) | ≥ 6 | < 3 |
| `<!-- ANCHOR -->` block present, 200–400 words | 1 | 0 |
| `<!-- KEEP -->` marked imperfections | 2–4 | 0 |

**Note on gaming.** These metrics are proxies, and a sufficiently determined agent can satisfy every one of them while writing badly. That is exactly what happened to the prior draft in a different key: it was internally consistent and unpublishable.

The proxies exist so that cheap failures are caught cheaply and human attention goes to the expensive ones. The expensive ones are handled by `VOICE.md` — uniform information density, costlessness, symmetry, mid-band diction, absent physical world, and missing idiolect. **Read `VOICE.md` before drafting. It matters more than this file.**

---

## 7. Notes for the audio edition

The audio script is a **separate manuscript**, not the print text piped through a renderer. Miso has no SSML layer — prosody comes only from sentence construction and audio context — so the writing *is* the prosody spec. Full pipeline in `AUDIO_SPEC.md`. Writing-side implications:

- Numbers in spoken form: "nineteen seventy-one," not "1971."
- No footnotes, no "see Chapter 12," no parenthetical citations. Companion PDF carries all of it. Say "as I argued earlier."
- Restate antecedents. A listener can't glance back: "Ostrom's third principle — the one about who gets to write the rules —" not "her third principle."
- Chapter handoffs go at the *start* of the next chapter, one sentence, never as an end-of-chapter summary.
- Check every instance of *deliberate, moderate, separate, object, present, contract, minute, live, lead, read, wound, use, refuse, invalid* — all homograph traps, and all frequent in this material. Reword or add to `homographs.tsv`.
- Every proper noun goes through `lexicon.tsv` before rendering. Test in isolation first.
