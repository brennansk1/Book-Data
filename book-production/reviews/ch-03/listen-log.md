# Listen Log — Chapter 3 draft-v3.md ("Eight Rules from a Spanish Water Court")

Method: read STYLE_BIBLE.md §7 and AUDIO_SPEC.md §4/§9, then draft-v3.md straight through as sound. Cross-checked `frozen/ch-01.md`, `frozen/ch-02.md`, `frozen/ch-10.md`, `frozen/prologue.md` for cadence and term collisions, since ch-02 (Axelrod) sits directly upstream of this one and a listener will have heard it one chapter ago. Findings ordered by severity.

---

## 1. [SEVERE — cross-chapter collision] The stag-hunt passage re-renders ch-02's own definition, near word-for-word, one chapter after the listener heard it

Line 39: "the stag hunt, after an old parable about two hunters choosing whether to **chase something big together** or peel off alone **for something smaller and safer**... The stag hunt runs on belief, before either side has done anything at all."

`frozen/ch-02.md` line 23, one chapter earlier: "game theorists call it the stag hunt. Two hunters have to decide whether to trust each other enough to **chase something big together**, instead of settling separately **for something smaller and safer**... It runs on trust, not incentive — a different engine entirely."

Two separate five-word exact strings repeat verbatim ("chase something big together" / "for something smaller and safer"), and the framing sentence around them — "a different engine [than/entirely]" — repeats too. This sits one chapter downstream of the original, not ten, so a listener has the phrasing fresh; it will read as the narrator forgetting he already said this, or as a tic. It's also close enough to the mechanical 6-gram lint check that a small further overlap would trip it. Recommend cutting straight to the callback instead of re-defining: something like "That's the stag hunt from two chapters back — the two hunters, the shared kill versus the safe rabbit — except here it runs on belief instead of incentive, before either side has done anything at all." Restate the *label* and the *distinction* (belief vs. incentive), not the parable itself.

## 2. [SEVERE — antecedent, unintroduced entity] "The failed Turkish fisheries" has no referent anywhere in this chapter

Line 69: "the village had already gotten two of her eight design principles right before he ever showed up, more than either of **the failed Turkish fisheries she also studied** ever managed."

The only other Turkish material in the chapter is line 45: "Ostrom has another case built almost exactly like this one, turn-based fishing spots off Alanya, Turkey" — introduced as a *success* comparable to Valencia, then deliberately dropped ("A second would just be showing off"). Nothing establishes that Ostrom studied *failed* Turkish fisheries, plural, at all. A print reader can flip back and conclude these must be different cases from Alanya; a listener has no such option and will either silently assume Alanya failed (contradicting line 45) or lose the sentence entirely. This needs either a one-clause plant earlier (naming the failed case(s) when Alanya is mentioned, e.g. "...and a couple of others that didn't hold") or a cut of the comparison at line 69.

## 3. [HIGH — breath / unparsable structure] The "no transcript" sentence buries its own point

Line 5: "There is no transcript of the arguments; the decisions themselves are written down, and always have been, which is a smaller and more honest claim than 'no written records,' and the correct one."

A semicolon, a quoted counter-phrase with no attribution carrier, and a trailing appositive ("and the correct one") that only resolves four clauses after its subject. Read aloud this cannot be parsed in real time — by the time "and the correct one" lands, the listener has lost what it's modifying. It's also a weak paragraph-internal beat: the actual content (records exist, they just aren't transcripts of the arguments) gets buried under the meta-commentary about how to phrase it. Recommend splitting into two plain sentences: "There is no transcript of the arguments. But the decisions themselves are written down, and always have been — that's a smaller claim than 'no written records,' and it's the true one."

## 4. [HIGH — numbers handoff] Every year in this chapter is still in digit form; one is also mid-sentence-parenthetical

Bare-digit years needing a spoken-form pass (Style Bible §7, AUDIO_SPEC §9): **1321** (l.13), **1435** (l.13, again l.83 in closing paragraph), **1960** and **960** (l.13 — note "960" needs an explicit render choice, "nine sixty" not "nine hundred sixty," since the sentence is explicitly contrasting it with 1960), **1990** (l.17), **2009** (l.15 *and* l.23 — see below), **1933** (l.63), **1938** and **1941** (l.63), **1940 / 1942 / 1945** (l.63), **1946** (l.63, again l.67), **1964** (l.63), **1966** (l.65).

Two of these need more than a spelling pass:

- Line 63: "The villagers petitioned three separate times through the 1940s **(1940, 1942, 1945)** to get their own cap enforced." A parenthetical citation-style list of years is exactly the construction AUDIO_SPEC §8 bans for the audio script ("no parenthetical citations... lists converted to prose"). Convert to prose: "The villagers petitioned three separate times through the 1940s — in nineteen forty, nineteen forty-two, and nineteen forty-five — to get their own cap enforced." (Also a tricolon once converted; count it.)
- Lines 15 and 23 both land on **2009** for two unrelated facts (the UNESCO listing; Ostrom's Nobel) within nine lines of each other. A listener has no visual "2009" to anchor two different claims to and may merge them into one event. Consider moving one reference or adding a light differentiator ("that same year" is available and would actually help here if the chronology is deliberate — otherwise separate them further).

## 5. [MEDIUM — antecedent] "Two of her eight design principles" — which two?

Line 69. The chapter names boundaries (l.33), monitoring (l.37), and by implication sanctions (the fine-size discussion, l.47 area, not shown here) as three of Ostrom's principles, plus nested enterprises as the eighth (l.73). It never numbers or names a full list of eight, and never says which two Mawelle got right. A reader can accept the scorecard as a gesture; a listener, asked to hold "two of eight" with no antecedent for either number, gets an unverifiable statistic. Recommend naming the two explicitly: "the village had a clear boundary and real monitoring — two of her eight principles — before he ever showed up."

## 6. [MEDIUM — breath] Three more sentences worth a read-aloud pass at listening speed

- Line 13: "There's also a set of articles drawn up by eighty-four irrigators in 1435, who sat down at the monastery of St. Francis and wrote out, for the first time, exactly how the water would be shared in a dry year and a wet one." ~44 words, one breath, no natural mid-point.
- Line 17 (ANCHOR-adjacent paragraph, not shown above but same stretch): "It also, I noticed much later, going back through the numbers myself instead of trusting her prose to carry me, doesn't stretch quite as far as it can sound like it stretches." Subject ("It") and verb ("doesn't stretch") are separated by a 15-word parenthetical; by the time the verb arrives the subject has to be reconstructed from memory. Reorder so the parenthetical trails the verb instead of splitting it.
- Line 65: "he went straight to his own Member of Parliament, who arranged the permission; the local official who should have been the check came into it only afterward, refused at first, and was overruled from above." Two stacked relative clauses plus three verbs in a row on the second half ("came... refused... was overruled") without a connective — reads as a list without sounding like one is intended. This paragraph also carries five separate numbers (32, 84, 24, 1966, 108) in six sentences; dense but each is anchored to what precedes it, so flagging for density rather than requiring a rewrite.

## 7. [MEDIUM — quote length] Ostrom's "neither the state nor the market" quote runs to 31 words

Line 23: "What one can observe in the world, however, is that neither the state nor the market is uniformly successful in enabling individuals to sustain long-term, productive use of natural resource systems."

Style Bible §5 caps quotes at 25 words "unless the exact wording is doing real work." This is the book's opening statement of Ostrom's whole thesis and arguably earns the exception, but it's 6 words over and worth a deliberate keep-or-trim call rather than passing silently. Attribution is correctly placed before it ("Ostrom put it on the first page..."), so the boundary itself is audible either way.

## 8. [LOW-MEDIUM — homographs, per the requested check] Candidates for `lexicon.tsv` / `homographs.tsv`, print form → suggested render

- **close / closer** (5 instances, l.9, l.13, l.43, l.65, l.37) — all in the "near" sense (adjective/adverb), none in the "shut" sense, so internally consistent, but the word family should still be tested in isolation given how often it recurs across the book generally.
- **record / recorded** (l.9, l.13, l.61-area, l.51-area) — mixes noun ("the record") and past-participle ("recorded"/"catalogued") uses; test both stresses.
- **present** (l.79) — "necessary conditions... present in every long-lived case" — adjective sense, competes with the more frequent noun/verb readings; reword-test.
- **separate** (l.15, l.63) — one adjective ("a separate water court"), one adjective again ("three separate times") — same POS both times, lower risk, still worth an isolation test since AUDIO_SPEC names it as a chapter-recurring trap.
- Proper nouns / non-English terms for `lexicon.tsv`, render-spelling suggested: **Tribunal de las Aguas** (l.3) → "tree-boo-NAL deh lahs AH-gwahs"; **Micalet** (l.3) → "mee-kah-LET"; **huerta** (13 occurrences — highest-frequency term in the chapter, nail this first) → "WEHR-tah"; **regadiu** (l.33) → "reh-gah-DEE-oo"; **secano** (l.33) → "seh-KAH-no"; **extremales** (l.33) → "eks-treh-MAH-less"; **hereters** (l.43) → "eh-reh-TEHRS"; **Castellón** (4 occurrences) → "kas-teh-YOHN"; **madelia** (l.57-area) → "mah-DEH-lee-ah"; **Mawelle** (3 occurrences) → "mah-WEL-leh"; **Mahattea** (4 occurrences) → "mah-hah-TAY-ah"; **Alanya** (l.45) → "ah-LAHN-yah"; **Turia** (2 occurrences) → "TOOR-ee-ah". "Jaume" from the standing watch-list does not appear in this draft.

## 9. Quote boundaries — pass

Both direct quotations in the chapter follow the rule cleanly: attribution precedes the quote in both cases, with a clear verbal signal it's about to start.
- Ostrom, l.23: "Ostrom put it on the first page of the book that would make her, in 2009, the first woman to win the Nobel in economics." → quote. Clean start/end, no ambiguity about who's speaking.
- Glick, l.9: "The historian who dug up those books, an American named Thomas Glick, put it plainly: the fines were low and variable," → "a few pennies at the most." Clean, short, no issue.

## 10. Cadence — otherwise strong

Outside of Finding 1, this chapter doesn't show the monotony patterns flagged in earlier chapters' logs (repeated citation-clicks, anaphoric quote-stacking). The one-sentence paragraphs ("Pennies." / "None of it saved them." / "Good rules, honestly arrived at...") land as genuine strong beats, and the confidence modulation in the closing section (lines 79ff, "I'm confident in that much... I'm much less confident...") reads well aloud. No further monotony issues found in the three-principles stretch (ll. 33–43) beyond the stag-hunt collision already flagged, or in the Mawelle passage's numeric run beyond the density note in Finding 6.

---

## Verdict: FIX

Two SEVERE items (stag-hunt collision, unintroduced "failed Turkish fisheries") and the numbers/parenthetical conversion in Finding 4 should be resolved before this chapter is treated as audio-ready. Everything else is a clean, targeted pass — the chapter's confidence modulation, paragraph endings, and quote handling are otherwise in good shape.
