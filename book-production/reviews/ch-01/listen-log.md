# Listen Log — Chapter 1 draft-v3.md

Simulated read-aloud pass, per STYLE_BIBLE.md §7 and AUDIO_SPEC.md §4/§9. Going through as sound, not as text on a page. Skimmed `frozen/prologue.md` and `frozen/ch-10.md` for cadence and term collisions only. Findings ordered by severity.

---

## 1. Breath rule: one sentence cannot be said aloud in one breath at all (severe)

> "You're the one I called because you'll actually argue back instead of saying "huh, interesting" and changing the subject to the Sox — you did that once standing in your driveway, cordless drill still running in your hand, and somehow won the argument anyway — and you've been wrong often enough in these calls that I still owe you at least one real apology, which isn't coming today either."

Line 19. Roughly 75 words, two stacked em-dash asides, then a trailing relative clause after the second dash closes. This is the longest and most structurally tangled sentence in the chapter, and it sits inside the paragraph that establishes Nate as a character — exactly the place a listener needs the syntax to be simple so the relationship can land. Needs at least two hard breaks: after "...to the Sox," and after "...won the argument anyway." The apology clause can stand alone.

## 2. Audible tic: three consecutive sentences with identical shape (severe)

> "The inshore fishermen weren't being unreasonable. The scientists weren't being unreasonable. Crosbie wasn't being unreasonable."

Line 91. Same subject-verb-negation-predicate contour, three times running, no variation in length or rhythm. On the page this reads as deliberate anaphora. At listening speed, with a CSM-style model that (per AUDIO_SPEC §4) "renders the same cadence every time," this will land as the model looping rather than as rhetorical build — the exact failure the spec names by name. The next sentence ("Add the mayors to that list too...") also implies a fourth "X wasn't being unreasonable" that never quite arrives, which softens the landing further. Recommend breaking the shape on the third beat — e.g., "Crosbie wasn't either" or fold Crosbie into a different construction entirely — so the triad resolves rather than just stopping.

## 3. Antecedent loss: "the first" / "the second" in the two-mechanisms passage (severe–medium)

Lines 57–63. Marchak's argument is introduced at line 57 ("...a tragedy of state mismanagement..."), followed immediately by "Two mechanisms compounded here, and they're worth taking apart separately" — but the two mechanisms are not labeled "first" and "second" when they're actually described. Paragraph at line 59 opens "The water ran on Hardin's arithmetic almost exactly..." (this turns out to be "the first"). Paragraph at line 61 opens "The ministry ran on different arithmetic entirely..." (this turns out to be "the second"). Only at line 63, a full two paragraphs and roughly 250 words later, do the ordinal labels actually appear:

> "Two mechanisms, then, compounding rather than repeating. The first is most of the reason the fish got overfished. The second is most of the reason nobody with the power to stop it ever did..."

A reader can flip back half a page to check which was first. A listener has to have silently tagged "water/fleet paragraph = one" and "ministry paragraph = two" in real time, unprompted, while also tracking dates, agency names, and the Marchak/Hardin framing in the same stretch — exactly the "listener can't glance back" problem AUDIO_SPEC §4 and STYLE_BIBLE §7 both call out. Recommend front-loading the ordinal at the top of each paragraph instead of only at the recap — "The first mechanism ran on Hardin's arithmetic almost exactly" / "The second ran on different arithmetic entirely" — so the label and the content arrive together.

## 4. Quote boundary: Sinclair's quote has no audible boundary on its second half (medium-high)

> "He put it almost that bluntly: overfishing by local inshore fishers "must be discounted as a major factor" in the collapse, even though they "seem to bear the brunt" of what happened."

Line 35. Attribution ("He put it almost that bluntly:") precedes the first fragment, satisfying STYLE_BIBLE §5's letter. But the quotation is split into two short embedded phrases grammatically woven into the sentence, and only the first fragment sits right after the attribution. The second fragment ("seem to bear the brunt") has no fresh attribution and no structural signal — it just continues inside the same sentence, introduced only by "even though they." In print, quotation marks carry the boundary. In Miso's no-SSML render, there is nothing to mark where Sinclair's words end and the narrator's resume, especially mid-sentence. This is also a second quoted extraction from the same source in the same chapter (see STYLE_BIBLE §5, one quote per source per chapter), which compounds the risk — two separate quote-boundary events from one attribution. Recommend either a single continuous quote ("must be discounted as a major factor... even though they seem to bear the brunt of what happened") with attribution once, or cut to the stronger of the two fragments and paraphrase the rest.

## 5. Breath rule: a cluster of secondary long or interrupted sentences (medium)

None fatal alone, but six-plus in a ~4,900-word chapter is a real pattern, and several combine length with a subject/verb interruption, which is harder on the ear than word count alone suggests:

- Line 3: "Bay Bulls is a fishing community about thirty kilometres south of St. John's, and on the first of July, 1992, a crowd of roughly a thousand people filled the wharf there for what was supposed to be a Canada Day event." (~44 words, one "and.")
- Line 13: "It put about thirty thousand fishers and plant workers out of work in a single announcement, the largest mass layoff in Canadian history, and it emptied out more than four hundred communities that had no other major employer." (~38 words.)
- Line 17: "When John Cabot's crew came back in 1497, the reports that reached Europe — a Milanese envoy in London wrote them down that December — described fish so thick that sailors claimed you could slow a ship just by sailing it through them." Subject ("the reports") and verb ("described") are split by an eight-word em-dash aside — the ear expects the verb right after "Europe" and has to hold the clause open across the interruption.
- Line 41: "The audit, run by an American fisheries scientist named D. L. Alverson, went further than a stale gauge — it found a specific mathematical fault built into the model itself, one that had been quietly expanding its own error for years." (~40 words, appositive plus em-dash plus trailing relative clause.)
- Line 43: "It was more like a series of people, each reasonably busy and reasonably confident in the system they worked inside, each deciding this particular red flag could wait for the next budget cycle, until there were no cycles left." (~38 words.)
- Line 57 (see also Finding 3): "A geographer named Patricia Marchak looked at this exact case and argued it isn't really a Hardin-style commons at all, but a tragedy of state mismanagement, since the fishermen never held the management rights; the state held them, and used them badly." (~43 words, semicolon-spliced — functionally two sentences.)
- Line 71: "The roughly thirty thousand fishers and plant workers counted as directly out of work is the number you'll usually see quoted; tallies of the wider economic damage, everyone whose income depended on the fishery indirectly, run meaningfully higher." (~38 words, semicolon plus appositive.)

Worth a pass to add a hard stop to at least the Marchak sentence (line 57) and the Cabot sentence (line 17) — both currently ask for a breath mid-clause, not just at length.

## 6. Weak beat: a paragraph closes on a stacked, self-contradicting hedge (medium)

> "Even knowing what we know now, I'm not sure I'd have cut the quota in his chair, at that podium, with that crowd in front of me, and I'd like to think I would have."

Line 69. The paragraph builds real tension about Crosbie's impossible position, then closes on two hedges pointed in opposite directions in the same breath — "I'm not sure I'd have cut it" immediately followed by "I'd like to think I would have." Read silently, this parses as earned ambivalence. Heard once, cold, it risks landing as the narrator contradicting himself in his own closing clause — the last thing the listener hears from the paragraph is a walk-back of the walk-back. This may be intentional (confidence modulation per STYLE_BIBLE rule 9), but if so it needs a beat of separation — a period and a shorter final clause — rather than one unbroken "and" tying both hedges together. Consider: "...with that crowd in front of me. I'd like to think I would have."

## 7. Numbers — audio handoff list (medium; mostly clean, two figures need a decision)

All spoken-form conversion is expected at the audio-script pass, not this print draft (per AUDIO_SPEC §8, confirmed as the working convention in the prologue's own listen-log). Flagging for that handoff:

- **Calendar years** (convert to spoken form, no ambiguity): 1992 (×2, incl. the quota line), 1497, 1977 (×2), 1987 (×2), 1968 (×2), 1833, 1989, 1990, 2017, 2019, 2024.
- **Dates**: "July 2" (line 13) needs "July second"; "the first of July, 1992" (line 3) is already ordinal-friendly, just needs the year converted.
- **Already in spoken form, no action needed**: "roughly a thousand," "thirty thousand," "five hundred years," "four hundred communities," "two-hundred-mile," "a hundred and thirty-five years," "under five percent," "Thirty-two years," "Two hundred and thirty-eight," "two billion dollars," "a billion and a half." These are already doing the right thing — worth noting as a positive pattern to keep.
- **Needs a decision, not just conversion**: "187,969 tonnes" and "129,033 tonnes" (line 41). These are exact, six-figure numbers used for a direct-comparison point (this year's quota was higher than last year's entire catch). Spoken aloud in full ("one hundred eighty-seven thousand, nine hundred sixty-nine tonnes") they are unretainable by ear and will likely wash past the listener as noise, undercutting the rhetorical point they exist to make. Recommend flagging to the Showrunner: either round for the audio script ("roughly 188,000 tonnes... more than the entire industry had caught the year before, about 129,000") or keep exact and accept the number is felt rather than retained. Either way this needs an explicit decision, not a silent auto-conversion.
- **Currency needs reformatting**: "$573 million" (line 79) — the "$" prefix convention doesn't survive to speech; needs to become "roughly five hundred seventy-three million dollars" in the audio script.
- **Discrepancy from the review brief**: the brief for this pass lists "$1.525 billion" as a number to check. That figure does not appear anywhere in draft-v3 — the nearest figures are "something like two billion dollars" (Chicago, line 79), "somewhere around a billion and a half" (New York, unquantified, line 79), and "$573 million" (Virginia, line 79). Worth confirming whether $1.525B was meant for an earlier draft or a different chapter; nothing to fix here, just flagging the mismatch so it isn't lost.

## 8. Homographs — "close" cluster is real, everything else is clean (low-medium)

Full AUDIO_SPEC §9 list checked (deliberate, moderate, separate, object, present, live, read, lead, refuse, minute, content, contract, wound, use, invalid, resume, conduct, entrance, desert, bow, close, tear, sow, house, abuse, record).

**"close" / "closest" / "closer" / "closely" — 7 hits, as the brief flagged:**

- Line 1: "The closest thing I have to one..."
- Line 19: "...that's the whole scene, or close to it."
- Line 35: "...fixed gear close to shore..." and "...tracked the collapse as closely as anyone did..." and "...They're closer to the people who show up first at a fire..."
- Line 49: "Cod fits Hardin's herdsman shape closely enough that..."
- Line 97: "A race to the bottom breaks for close to the opposite reason..."
- Line 103: "...find whoever's standing closest, yell at him..."

Every instance here is the adjective/adverb sense ("near," /kloʊs/), and most sit in strongly disambiguating idioms ("close to," "closely enough," "closest thing"). Grammatically low risk. But CSM-style TTS homograph errors aren't syntax-aware, and this is the single most repeated homograph-risk word in the chapter — seven hits is enough that one bad render is likely across a full read-through. Recommend running all seven through isolation-testing per AUDIO_SPEC §9 and adding to `homographs.tsv` regardless of the grammatical low-risk read.

**Everything else on the list — clean, low risk, noted only for the respelling table:**

- "abuse" (line 7, 9) — verb form both times ("no need to abuse him," "don't go abusing me"), forced by the object.
- "conduct" (line 91) — noun, forced by "their own conduct."
- "record" (line 43, "read into the record"; line 89, "on the record") — noun, fixed idiom both times.
- "used" / "use" — every instance in the chapter is past tense ("used to think," "used them badly," "used the phrase") or gerund-adjacent, not the bare ambiguous root. Low risk.
- "separately" (line 57) — the adverb form has only one pronunciation; the ambiguous root "separate" itself doesn't appear.
- No hits at all for: deliberate, moderate, object, present, live, read (as present tense), lead, refuse, minute, content, contract, wound, invalid, resume, entrance, desert, bow, tear, sow, house.

## 9. Quote attribution: one instance lands after, not before (low)

> "Collectively bargain, was the phrase he used, instead of collectively beg."

Line 81. Not set off in quotation marks, so it isn't a formal STYLE_BIBLE §5 violation, but the structure puts the phrase first and the attribution ("was the phrase he used") second — the opposite of the rule's rationale. A listener hears "collectively bargain" cold, with no signal yet that it's someone's specific coinage, and only gets the attribution after the fact. Low stakes since the phrase is short and self-explanatory, but an easy fix: "The phrase he used was collectively bargain, instead of collectively beg."

## 10. Minor: one paragraph ending lands dry after a vivid setup (low)

> "...and about the way a lot of small, ordinary preferences can tip into an extreme collective outcome once enough people hold them."

Line 93. The Schelling paragraph opens with a strong concrete image (segregated neighborhoods, traffic patterns) and closes on abstract-noun diction ("extreme collective outcome") that's a register step down from the rest of the chapter's ending beats. Not a hedge, so it's not a rule-11 violation in the strict sense, just a softer landing than this chapter's other paragraph closes. Optional polish.

## 11. Structural note: chapter closes on two forward-looking teases (low, production note)

AUDIO_SPEC §8 / STYLE_BIBLE §7: chapter handoffs belong at the *start* of the next chapter, one sentence, never as an end-of-chapter summary or tease. This draft previews upcoming content twice at the very end of Chapter 1: line 99 ("I'm saving it for next time," re: the stag-and-rabbit shape) and line 105 ("next time I'll tell you about the one structure in this family that doesn't need anybody, anywhere, to be good at all"). Neither is a "summary" in the banned sense, but both are end-of-chapter forward pointers rather than start-of-next-chapter handoffs, which is the specific placement the spec asks for. Worth a Showrunner call on whether to relocate one or both to the top of Chapter 2, or whether the epistolary format (this is a letter to Nate, not a lecture) earns an exception — flagging rather than assuming.

## 12. Frozen-chapter check: no term collisions, one soft cadence echo (clean)

No terminology collisions found against `frozen/prologue.md` or `frozen/ch-10.md` — "mechanism(s)" (ch-01) and "gate(s)"/"trigger" (ch-10) don't overlap, no Mode A/B language present, no reused proper nouns with conflicting referents. One soft structural echo, not a defect: both the prologue and this chapter open their ANCHOR block with the same "I wanted/expected a villain and went looking for one anyway" move (prologue: "scanning for the one person... who's actually being unreasonable"; ch-01: "I wanted it to be the fishermen... Find whoever's fault it looks like"). This is presumably a deliberate through-line for the book's opening movement, but two uses back-to-back in the first two chapters read aloud is enough that a third occurrence in Chapter 2 or 3 would start to feel formulaic. Flagging for the Showrunner's awareness, not a fix for this chapter.

---

## Verdict

**FIX, not pass.** The chapter is strong on the things that matter most — real named people, quote attribution mostly correct, confidence modulation present and audible, no summary sections, numbers already mostly in spoken-friendly form. But four items are load-bearing enough to block Gate 5 sign-off as-is: the 75-word unsayable sentence (#1), the three-beat negation tic (#2), the unsignposted "first/second" antecedent in the two-mechanisms passage (#3), and the split-boundary Sinclair quote (#4). Fix those four, take a pass at the long-sentence cluster (#5) and the stacked-hedge close (#6), and resolve the tonnage-number rounding question (#7) with the Showrunner — the rest are polish-pass items.
