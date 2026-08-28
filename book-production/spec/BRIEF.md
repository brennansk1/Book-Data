# The Brief — the only spec file an agent needs

This file supersedes STYLE_BIBLE, VOICE, IDIOLECT and detection-log for drafting and review work.
Read this; do not open those. (Canon Keeper and Verifier still go to `canon/` for content questions.)

## Register
A person who has thought carefully about something difficult, explaining it to an intelligent friend
who has not. Confident where confidence is earned, openly uncertain where it isn't, occasionally
funny, never showing off. **Not** the framework document, the executive summary, or the textbook.
Framework prose announces its structure. Book prose has structure and doesn't mention it.

## The rules that matter
1. Open with a case, never a thesis. A person, a place, a date.
2. One argument per chapter, sayable aloud in one sentence.
3. Objections are people, not headers. A named interlocutor says the thing and gets the strongest
   version, then an answer.
4. **No summary sections. Ever.**
5. **One list per chapter maximum; zero is better.** Conditions and gates must be prose — the prose
   has to explain why each item follows from the last, which is what a list hides.
6. Two headers per chapter, maximum.
7. First person singular for judgment calls. The institutional "we" reads as evasion.
8. At least three real named people doing specific things.
9. Modulate confidence audibly — and **not all in the closing paragraph** (see DL-10).
10. Write for a breath. If you can't say it in one, rebuild it.
11. End paragraphs on the strong beat; move hedges inward.

## Banned outright
"It's not just X, it's Y" · "Let us examine/consider the following" · "The key insight is" ·
"In this chapter we will" · "It's worth noting" · "Importantly," · "Notably," ·
delve, tapestry, landscape (fig.), navigate (fig.), underscore, multifaceted, nuanced (as praise),
robust (outside stats), leverage (verb), at its core, fundamentally, profound ·
"The framework holds/argues" · **"flattering"/"unflattering"** · **"obviously"** ·
exclamation marks · opening a chapter with a quotation ·
**"than the argument/chapter strictly needs"** · em-dash stacking (2+ per sentence).

## The negation family — the book's most dangerous tic
"X isn't [vice]; [structural reason]" and every disguise it wears: "not X — it's Y", "X isn't Y.
It's Z.", "wasn't being X". Budget: **ONE cluster per chapter** (up to three instances in the single
passage where it IS the argument), zero strays elsewhere. `lint.py` counts this as `negate_correct`.

## Voice signature (reproduce these)
- **Sentence shapes:** the deflating one- or two-word paragraph after a build ("Seventy."); a short
  flat declarative then a longer sentence that complicates it.
- **Image family:** hydraulics and water under pressure — leaks, holes, walls, climbing totals.
  Engineering (fences, gates) is available. No more than two families per chapter.
- **Joke shape:** understatement, at the writer's own expense. Never at the people in the cases.
- **Two overused words:** "unreasonable" and "climbing." Let them recur.
- **Named weakness:** impatience first, verification second.
- **Refusals:** see banned list.

## Standing rules earned from ten reviews (the detection log, compressed)
- **DL-1/4:** admissions enter COLD — no "I'll admit", no "this isn't comfortable". Never narrate a
  requirement while satisfying it ("I'm spending more time on this than…"). ONE named omission per
  chapter. "thing" ≤4 uses.
- **DL-3:** vary where the interlocutor's objection lands — early, distributed, or as agreement the
  writer argues against. Not always the back third.
- **DL-5:** correspondents vary on relationship AND mode. Never introduce one with
  profession-plus-quirk in a single paragraph. Used already: Nate, Marisol, Grace, Dana, Priya,
  Jonah, Helen.
- **DL-6:** no confession staged as a solitary writer in transit or at rest with one prop (kitchen,
  carrel, plane seat). Retired.
- **DL-8:** the anchor may not always run fast-judgment→correction. Half the remaining anchors must
  break it: an admission never corrected, a correction that came from someone else, a cost with no
  lesson.
- **DL-9:** don't end on admitted uncertainty — one chapter per Part may, and Part One's is spent.
- **DL-10:** calibration goes where the uncertainty lives, NOT banked in the closing paragraph.
  `lint.py` measures `conf_mods_in_tail_pct` (≤60%).
- **General:** if you find yourself repeating a device, check whether a rule is causing it.

## Quotes
Attribution BEFORE the quote, always. Under 25 words unless the exact wording does real work.
**One quote per source per chapter.** A quotation shows how someone put it; it never establishes that
they were right. Every quote must exist in the evidence packet with exact wording — never
reconstruct from memory. **Never invent a citation, statistic, quotation or date.**
**Never state a causal mechanism the evidence packet doesn't contain** — if you want one anyway, mark
it in the text as your own conjecture and demote it from load-bearing.

## Lint thresholds (Gate 2, hard fails)
4,000–4,800 words (prologue/coda exempt) · mean sentence ≤24 · sentence SD ≥7 · <4% short sentences
fails · >5% over-40-word fails · paragraph mean ≤150 · longest paragraph ≤260 · headers ≤3 ·
lists ≤1 · named people ≥2 · first-person ≥3 · em-dashes ≤7/1k · tricolons ≤5 · negate_correct ≤8 ·
conf_mods_in_tail_pct ≤100 (target 60) · banned phrases 0 · repeated 6-grams vs frozen 0 ·
anchor 200–400 words · KEEP marks 2–4.

## Audio-readiness (the print text carries these; the audio script is generated later)
No tables, no footnotes. Attribution before quotes. Restate antecedents a listener can't glance back
for. Avoid parenthetical citations in prose. Homograph traps to reword when context doesn't force the
reading: defect, read, close, deliberate, separate, record, present, lead, live, minute, object.

## Canon essentials
The position is **phenomenal value realism** — the badness of suffering is constitutive of the
experience, not appended to it. Banned: the label "Constructivist Realism", the three-layer grounding
defence, the thermometer analogy, the six-dimensional value vector, burden-shifting onto the egoist,
Moloch as the sole diagnosis, policy conclusions presented as derivations.
The internal labels "Mode A"/"Mode B" NEVER appear: the book says **"the standing rules"** and
**"the override"**. Nothing may be stated at higher confidence than `canon/POSITIONS.md` allows.
