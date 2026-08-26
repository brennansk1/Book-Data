# Voice Spec — How the Prose Stops Sounding Machine-Made

`STYLE_BIBLE.md` catches the surface tells. Those are the cheap failures. This file addresses the expensive ones: the properties that make prose read as machine-made even when every banned phrase has been removed and every threshold passes.

A draft can satisfy the entire linter and still be obviously synthetic. This is the file that fixes that.

---

## 1. The eight deep causes

Surface tells are vocabulary. These are structural, and none of them is detectable by regex.

### 1.1 Uniform information density

Human prose breathes. Dense passage, then a beat that carries nothing, then an aside the writer couldn't resist, then dense again. Machine prose is relentlessly informative — every sentence advances something. Over 4,000 words this produces a specific fatigue readers describe as "exhausting" or "flat" without being able to say why.

**Requirement:** every chapter contains at least four **beat sentences** — sentences that carry no argumentative load. A scene detail. A short aside. A restatement in plainer words. Something that just lets the reader stand still.

> Ostrom went to Valencia in the nineteen-eighties. It rains there in October and almost never otherwise.

The second sentence does nothing. Keep it.

### 1.2 No cost

Human writing shows the writer paid something to produce it: a fact they had to go get, an admission that embarrasses them, an anecdote only they possess, a prediction that could be checked and found wrong. Machine prose is costless — it says defensible things at no risk.

**Requirement — the costly signal quota.** Every chapter contains at least three of:
- A specific number, date, or proper noun that could only come from actually looking it up
- A first-person admission that does not flatter the author
- An anecdote from the author's own life
- A named prediction with a date attached
- A concession that materially weakens the chapter's own argument
- A disagreement with someone the author otherwise admires

### 1.3 Symmetry and completeness

Machine prose covers all angles evenly and finishes every thread. Human prose is lopsided: the writer is disproportionately interested in one thing, spends too long on it, and skips something a textbook would have covered.

**Requirement:** every chapter has **one deliberate obsession** — a sub-topic given roughly twice the space it strictly deserves, because the author finds it interesting — and **one deliberate omission**, named in a single clause and left alone. ("There's a whole literature on how Ostrom's principles fail in fisheries. I'm not going to get into it.")

### 1.4 Mid-range diction

Machine prose avoids both ends of the register. No "thing," "stuff," "sort of," "a mess" — and equally, no genuinely odd or technical word where a neutral one exists. It lives permanently in the middle band, which is why it sounds like everyone and no one.

**Requirement:** every chapter uses at least six **plain-band** words (thing, stuff, mess, bad, weird, gets, big, awful) and at least three **high-band** words that are exactly right and slightly unexpected. Not thesaurus words — precise ones.

### 1.5 No physical world

Machine prose has no weather, no bodies, no rooms, no time of day, no food. It happens nowhere. This is the fastest reader-level tell after vocabulary and it is almost never mentioned.

**Requirement:** every chapter contains at least three **sensory anchors** — a room, a season, a body, a sound, a piece of clothing, a meal. They can be small. They cannot be zero.

### 1.6 Every paragraph is a complete thought

Machine paragraphs are little essays: topic, development, close. Human paragraphs break early, run long, land mid-argument, and sometimes exist to hold one sentence.

**Requirement:** every chapter contains at least two **one-sentence paragraphs** and at least one paragraph over 160 words. Paragraph length standard deviation ≥ 45.

### 1.7 Named transitions

"However." "Moreover." "Furthermore." "Additionally." "That said." Machine prose names the logical relation between paragraphs because it is not confident the relation will be felt. Human prose usually just continues, and the relation is obvious from the content.

**Requirement:** at most four explicit connective openers per chapter. Delete the rest; the sentence almost always survives intact.

### 1.8 No idiolect

This is the deepest one. Machine prose is consistent but has no habits. Real writers have tics — a preferred sentence shape, a recurring image, a joke they keep making, a word they overuse. Consistency without personality reads as corporate.

The fix is not to remove the tics. It is to **specify them**, deliberately, and require them. See §2.

---

## 2. The idiolect sheet

The book needs an actual voice, defined as a constraint rather than hoped for. The Showrunner fills this in before Chapter 1 is drafted; every Drafter reproduces it. These are placeholders to be replaced with real ones — the point is that there must be exactly this many, they must be specific, and they must recur.

**Sentence shapes.** Two or three signature moves. E.g.: a short declarative followed immediately by a longer sentence that complicates it. Or: a sentence that ends on a two-word fragment.

**A recurring image family.** Pick one domain and return to it — engineering, weather, card games, carpentry, navigation. The framework already leans on engineering (the bridge, the fence, firmware). Commit to it and use it consistently rather than mixing four metaphor families per chapter.

**A joke shape.** One kind of humour, used four or five times across the book. Understatement is the safest for this material.

**Two overused words.** Every real writer has them. Pick two and let them recur. Readers register this as voice, not repetition.

**One rhetorical habit the author knows is a weakness** — and does anyway. Naming it in the Coda is itself a costly signal.

**One thing the author refuses to do.** Never uses exclamation marks. Never begins a chapter with a quotation. Never says "obviously." Consistency in refusal is as legible as consistency in habit.

---

## 3. Seed corpus — the highest-leverage intervention

Rules produce rule-following prose. **Samples produce voice.** This does more than the entire linter.

**Build `voice/seed/` before drafting begins:**

1. **`author/` — 3,000–5,000 words of the Showrunner's actual unedited writing.** Emails, Slack messages, notes, arguments in comment threads, a long text to a friend. Unpolished is better than polished; the goal is to capture how he actually sounds when he's explaining something he cares about to one person.

2. **`models/` — 6–10 passages of 800–1,500 words** from the target books, chosen for a specific quality and annotated with what to steal:
   - Sandel, *Justice* — a case-first chapter opening
   - Glover, *Humanity* — moral weight carried by historical particularity
   - Blackburn, *Being Good* — compression without condescension
   - Williams, *Ethics and the Limits of Philosophy* — conceding hard and staying persuasive
   - Appiah, *The Honor Code* — narrative and argument braided
   - Nagel — sentence-level clarity on genuinely hard material

3. **`anti/` — 3 passages from the prior 1,325-page draft**, labelled *this is the failure*. Negative examples are unusually effective; the drafter needs to see the exact register it must not produce.

Every Drafter receives all three directories. This is non-negotiable and it is the reason the pipeline works at all.

**Copyright note:** model passages are internal reference only. Nothing from them appears in the manuscript, and the Verifier checks for it.

---

## 4. Drafting protocol — three passes, never one

The single most reliable cause of expository register is asking for a finished chapter in one request. The model reaches for its highest-probability nonfiction continuation, which is the encyclopedia entry.

**Pass A — the case, cold.** Write only the opening case, 400–700 words. No argument, no framing, no "this illustrates." Just the scene: who, where, when, what happened, what it cost. Treat it as reportage. Stop.

**Pass B — the letter.** In a *fresh context*, write the chapter's argument as a letter to one specific named person who is smart, skeptical, and not a philosopher. Address them directly. Use "you." Include the digressions a letter would include. Do not organise it well.

This is the highest-value trick in the entire pipeline. Expository register cannot survive the second person. A letter cannot contain "in this chapter we will," cannot contain a numbered list of five conditions, and naturally produces beat sentences, asides, and admissions.

**Pass C — the merge.** In a third context, given Pass A and Pass B, produce the chapter. Keep the case as the opening. Keep the letter's rhythm, digressions, and directness. Convert "you" to the reader where it works and to a named interlocutor where it doesn't. **Do not tidy the argument into sections.** The merge's job is to preserve looseness, not remove it.

**Pass D — delete the first paragraph.** Machine drafts warm up. Read the chapter starting from paragraph two; nine times out of ten it is a better opening and nothing is lost. Do this before the Line Editor sees it.

---

## 5. Human anchors

**Every chapter contains 200–400 words written personally by the Showrunner**, placed at the load-bearing point — usually the passage where a judgment call is made or a concession offered. Marked in the draft as `<!-- ANCHOR -->` and never rewritten by an agent.

Chapters where the Showrunner writes the *whole* thing: the Prologue's opening case, Chapter 7 (*What I Don't Know*), the suicide passage in Chapter 15, and the Coda.

Why this works beyond authenticity: an agent drafting around fixed human paragraphs has to match them, and matching a real voice is a much better instruction than following style rules. The anchors pull the surrounding prose toward themselves.

---

## 6. The imperfection budget

Perfectly clean prose reads as machine-made. Real writing carries small deliberate looseness.

Per chapter, permit and expect:
- One or two sentences that are grammatically loose because that is how speech works. Sentence fragments. A comma splice where the rhythm wants one.
- One sentence that starts with "And" or "But."
- One place where the author is visibly irritated.
- One place where a sentence is longer than it should be because the thought didn't want to break.

**The Line Editor is explicitly forbidden from smoothing these.** Mark them `<!-- KEEP -->`. A Line Editor's default instinct is to regularise, and regularised prose is exactly the failure.

---

## 7. Burstiness scoring (Gate 2.5)

`tools/burstiness.py` computes per-sentence token surprisal against a small local language model and reports the **variance** across sentences.

The signal: machine prose is *predictable in a uniform way*. Human prose spikes — an unexpected word choice, an odd construction, a fact the model couldn't have guessed. Low variance means flat prose even when mean surprisal looks fine.

The output that matters is not the score. It is **the ranked list of the twenty flattest sentences in the chapter**, which is a direct rewrite worklist. Those sentences are, empirically, the ones a reader's attention slides off.

Run against a reference corpus built from `voice/seed/models/` so the targets are calibrated to the books you're trying to sound like, not to an abstract ideal.

Thresholds are advisory, not hard fails — the metric is gameable and should never be optimised directly. It is a pointer, not a judge.

---

## 8. The detection panel (Gate 6, per part)

At the end of each of the five parts, run a blind test.

Assemble twenty paragraphs: ten from the finished part, ten from the model books in `voice/seed/models/`, stripped of proper nouns that would give the source away. Give them to five readers who don't know the ratio. Ask one question: *which of these were written by a machine?*

**Target: readers perform at chance.** Any paragraph identified as synthetic by three or more readers gets rewritten, and the reason is logged in `reviews/detection-log.md` so the pattern feeds back into this file.

This is the only measurement in the pipeline that tests the actual thing you care about. Everything else is a proxy. Run it early — after Part One, not after the manuscript — so the findings can shape the remaining four parts.

---

## 9. Cold-read discipline

- Every draft sits **24 hours minimum** between Pass C and the Line Editor. Fresh eyes catch register failures that same-session review cannot.
- Every chapter gets **one human read-aloud** — an actual person, out loud, not the TTS — before freeze. The TTS read-aloud gate catches rhythm; a human reading aloud catches the sentences that are physically unpleasant to say, which correlate almost perfectly with sentences that are unpleasant to read.
- The Showrunner reads every chapter **on paper**, once. Screen reading forgives flatness; paper does not.

---

## 10. Quality metrics summary

Added to `STYLE_BIBLE.md` §6 as soft targets, checked by the Voice Curator rather than the linter where they require judgment.

| Metric | Target | Source |
|---|---|---|
| Beat sentences | ≥ 4 | §1.1 |
| Costly signals | ≥ 3 | §1.2 |
| Deliberate obsession | 1 | §1.3 |
| Deliberate omission, named | 1 | §1.3 |
| Plain-band words | ≥ 6 | §1.4 |
| High-band precise words | ≥ 3 | §1.4 |
| Sensory anchors | ≥ 3 | §1.5 |
| One-sentence paragraphs | ≥ 2 | §1.6 |
| Paragraphs > 160 words | ≥ 1 | §1.6 |
| Paragraph length SD | ≥ 45 | §1.6 |
| Explicit connective openers | ≤ 4 | §1.7 |
| Idiolect markers present | ≥ 3 of 6 | §2 |
| Human anchor words | 200–400 | §5 |
| Marked imperfections | 2–4 | §6 |
| Sentence surprisal variance | ≥ model corpus median | §7 |
| Detection panel accuracy | ≈ chance | §8 |
