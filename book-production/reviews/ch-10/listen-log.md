# Listen Log — ch-10 draft-v3 ("Three Gates")

Method: read STYLE_BIBLE §7 and AUDIO_SPEC §4 + §9, then draft-v3.md straight through as sound — no eye-skimming, no re-reading a sentence to parse it, exactly the discipline a listener is stuck with. Cross-checked against manuscript/frozen/prologue.md for term/image collisions, and against reviews/ch-10/decisions.md + cold-read.md to verify which prior findings actually got fixed. 4,847 words, 32 em-dashes.

Overall: this is close. The macro architecture (trigger → delay → review, five conditions built as a chain of holes) reads as connected reasoning at listening speed, not a disguised list — that's the hard part and it holds. The problems below are real but are all fixable at the sentence level; nothing here requires reopening the argument.

---

## Findings, severity order

**1. [HIGH — antecedent/forward-reference] "The four" is invoked before a listener has heard four of anything.**
Line 91: "A soldier starts with the most scaffolding... A physician like Priya has a hospital ethics board... Strip away the board, the license, and the chain of command, and what's left is the private citizen... **That's the thinnest reed of the four**, and it probably means the trigger should sit lower for them, not higher." At this point exactly three roles have been named — soldier, physician, private citizen. The fourth (civil servant) isn't introduced until the *next* paragraph: "The civil servant is the interesting case... rather than filing it next to the other three." A reader can flip back or read ahead and reconcile the count. A listener can't — they hit "of the four" having heard three, and either stall to recount or quietly conclude they missed one. This is a straightforward reorder fix: name the civil servant in the same breath as the other three (even a fragment — "and a fourth, the civil servant, who's its own case") before cashing "of the four."

**2. [HIGH — quote boundary] "Next April?" has no audible speaker.**
Line 7: "According to later testimony, he asked Thiokol when it wanted him to launch. Next April?" The preceding sentence is clearly marked reported speech (correctly — per decisions.md, Mulloy's line is testimony, not transcript, so it's right that it isn't in quotation marks). But "Next April?" then lands as an unattributed, unquoted fragment. On the page, italics-free but paragraph-adjacent, a reader infers it's Mulloy's paraphrased jab. Read aloud, with no attribution tag and no vocal quotation mechanism (Miso has no SSML, and per AUDIO_SPEC §6 only block quotes get the separate "Quotation" voice — a two-word interjection like this won't trigger it), a listener cannot tell whether that's Mulloy speaking, the narrator's own sarcastic aside, or the narrator's paraphrase of Mulloy. All three readings are plausible from audio alone. Fix: either fold it back into the attribution ("he asked Thiokol when it wanted him to launch — next April, maybe?") or give it an explicit tag ("the closest thing to an exact quote anyone remembers is 'next April?'").

**3. [MEDIUM-HIGH — cross-chapter collision, per your instruction to check against the prologue] "Coffee gone cold" is doing double duty across two chapters.**
Ch-10 opens Priya's first call with "coffee gone cold in her hand" (line 21) and closes the whole chapter on "Near midnight, coffee gone cold, that's everyone I know" (line 111) — a deliberate bookend, and it works on its own. But the frozen prologue already spent this exact image at its own confessional turn: "It's late while I write this part, coffee gone cold next to the keyboard, the kind of hour where a person's guard comes down" (prologue.md, line 30), immediately before its own ANCHOR admission. Both chapters now use "coffee gone cold + late hour" as the signal that a costly personal admission is coming. Heard back to back across the book (or even just in proximity during a listen-through), the image stops feeling specific to Priya or to the author's Sarah story and starts reading as the house move for "now I'm being vulnerable." Doesn't hit the letter of the repeated-6-gram linter (the shared span is three words, not six), but it's the kind of thing that linter exists to catch in spirit. Recommend swapping the ch-10 instance for a different sensory anchor, or confirming this is an intentional idiolect signature (per IDIOLECT.md) rather than an accident — if intentional, it should probably not also be the *literal* image, just the confessional structure.

**4. [MEDIUM — quotation rule, apparently unresolved from cold-read] Boisjoly is quoted twice.**
Line 5: "a catastrophe of the highest order — loss of human life" (the 1985 memo). Line 13: "At that moment I felt totally helpless and felt that further argument was fruitless, so I, too, stopped pressing my case" (later testimony). STYLE_BIBLE §5: "One quote per source per chapter. If you want a second thing from Ostrom, paraphrase it." This exact issue was flagged in cold-read.md finding 6 against draft-v1. decisions.md's "Cold-review repair" entry lists five fixes (gate count, five conditions, role-relativity, Loewenstein dating, 2036 pinning) — the Boisjoly double-quote isn't among them, and it's still here in v3. For audio this also means the "Quotation" voice anchor gets invoked for the same speaker twice in twelve lines, which is a smaller ask on a listener than two different sources but still worth collapsing. Keep the testimony line (it's the one doing the emotional work) and paraphrase the memo: "wrote to Robert Lund warning that unaddressed O-ring erosion could cost lives."

**5. [MEDIUM — tic purge, partial] The "X isn't Y. It's Z." pattern is gone in its banned single-sentence form but has migrated into a two-sentence variant, and it clusters late.**
The literal banned construction ("This is not X — it is Y" as a closer) doesn't appear anywhere in v3 — that purge holds. But the same rhetorical fingerprint — flat denial, then flat assertion, as consecutive short sentences — recurs three times in the back third of the chapter, close enough together that a listener will hear it as a habit:
- Line 64: "A procedure that never resolves isn't a procedure. It's an excuse with a longer runway."
- Line 81: "Sometimes the failure isn't overriding when you shouldn't. Sometimes it's complying —"
- Line 89: "That's not nothing. It isn't everything either."
Each is fine alone — the third is genuinely good, terse confidence-modulation. Together, in three passages spanning roughly 25 lines, the shape is audible. Recommend cutting or restructuring at least one, probably line 81's, since it's the closest to the original banned frame.

**6. [MEDIUM — hidden-list rhythm in the passage you flagged] The five-conditions passage runs on the word "hole" as its connective tissue, and it's audible as a device.**
Lines 49–55 are the passage doing the real work of converting the five conditions into prose per rule 5, and structurally it succeeds — each condition's inadequacy motivates the next, which is exactly what a bulleted list would hide. But the mechanism used to signal that inadequacy is the same word, four times in seven sentences: "has a hole the next one exists to plug" (49) → "the hole last resort exists to close" (51) → "Last resort has its own hole" (53) → "Even that has a hole" (55). Read silently this scans as a controlling metaphor. Read aloud, "hole" starts to function the way a bullet marker would — a click the ear starts anticipating before the sentence gets there, which is the same failure mode the prose conversion was supposed to avoid, just moved from formatting into vocabulary. Vary at least two of the four instances (e.g., "attribution isn't enough either, because a gentler path might have existed that nobody looked for" instead of repeating "hole").

**7. [MEDIUM — breath] Two sentences that don't fit in one breath.**
- Line 93: "In practice it functions in something closer to half of them, with no reliable way to know in advance which half you're in — whether the letterhead connects to a person with an actual mandate, or to a windowless office that hasn't issued a finding against its own agency in a decade." 51 words, one breath group, a bifurcated "whether... or..." clause riding on top of an already-long main clause. Split it: end after "which half you're in," start fresh with "Maybe the letterhead connects to..."
- Line 51: "Priya's honest answer, when we talked it through late on the phone, my kitchen the only lit room in the apartment, was that she doesn't know." The subject ("Priya's honest answer") and its verb ("was") are separated by two stacked parenthetical clauses. Not unbreathable, but the listener's ear is asked to hold the subject open for nine words before the verb resolves it — reorder so the scene-setting comes first: "We talked it through late on the phone, my kitchen the only lit room in the apartment. Priya's honest answer was that she doesn't know."

**8. [LOW-MEDIUM — weak ending] One paragraph closes on a trailing qualifier instead of the strong image that precedes it.**
Line 93 ends: "The civil servant is betting on scaffolding that might be load-bearing steel or might be a stage flat, **with no way to test which**." "Stage flat" is the strong beat and it's one clause too early — "with no way to test which" is a hedge tacked on after it, which is exactly what rule 11 says not to do. Cut the trailing clause or move it earlier: "The civil servant can't tell in advance whether the scaffolding is load-bearing steel or a stage flat." (Contrast with line 111's "coffee gone cold, that's everyone I know. It's me." — that's the chapter doing this correctly.)

**9. [LOW] Tricolon count is at 4, above the ≤3 target, though under the >5 hard fail.**
"while furious, while exhausted, while certain" (31); the three-item italicized self-talk list (62); "the correct form... the correct channel... the correct rejection" (81); "the board, the license, and the chain of command" (91). None individually reads as excessive, but STYLE_BIBLE's own note is that tricolons "become audible in TTS within twenty minutes" — this chapter is right at the edge of that window. Not a hard fail; flagging because a listen-through is exactly the condition the warning describes.

**10. [LOW] Minor pronoun-person drift.**
Line 39: "...because the hot version is provably not a reliable witness to **his** own reasoning." The passage has been addressing "you" ("puts a cold version of you back in the room") and then shifts to third-person "his" for the same referent inside the same sentence. Momentary, not confusing on a second read, but a listener's ear catches the switch. Either "your own reasoning" or commit to third person a sentence earlier.

**11. [LOW] Em-dash density is above the stated target, not the hard fail.**
32 em-dashes / 4,847 words ≈ 6.6 per 1,000, against a target of ≤4 (hard fail >7). No single sentence stacks them badly — checked for 3+ in one sentence, found none — so this is a density note, not a construction violation. Worth a light pass if the audio-script rewrite is touching sentences anyway, since every em-dash pair is a spoken parenthetical, and parentheticals are exactly what makes a sentence hard to read aloud smoothly.

---

## Homograph pass (STYLE_BIBLE §7 / AUDIO_SPEC §9 list)

Checked every instance of *deliberate, moderate, separate, object, present, conduct, subject, minute, content, live, read, lead, refuse, resume, invalid, use, close/closer, wound* in the chapter. Most of the words on that list (*moderate, separate, present, conduct, subject* [singular], *minute, content, live, lead, refuse, resume, invalid, wound*) don't actually occur in draft-v3 — nothing to fix. The ones that do occur, and their risk:

- **"a slow, deliberate one"** (line 29) — adjective, parallel to "a fast, intuitive mode," context should force the right reading but it's the one genuine judgment call in the chapter; worth testing in isolation per AUDIO_SPEC §9's process.
- **"a cold read"** (line 57) — noun use of *read*, should render as "reed" (like "a good read"), but nothing in the sentence forces present-tense over past-tense the way "human subjects" or "close to thirty" do elsewhere. This is the one I'd flag as an actual trap, not a formality — reword to "a cold reappraisal" or "a beat to read it cold" if the render comes back wrong, or add to homographs.tsv now.
- **"human subjects"** (line 43), **"an object on an org chart"** (line 87), **"It ran close to thirty"** (line 9), **"something closer to half"** (line 93), **"the hole last resort exists to close"** (line 51) — all have strong enough grammatical/collocational context (fixed phrase, preceding article/determiner, infinitive "to close") that I'd expect correct rendering, but they're cheap to add to the isolation-test batch since they're on the watch list anyway.

## Numbers needing spoken-form treatment for the audio script (print correctly keeps numerals — nothing to fix here in draft-v3 itself, this is the handoff list)

Dates: **January 27, 1986** (3); **1966** ×2 (73); **1968** (75); **1972** (75); **1974** ×2 (75); **2005** (19); **2002** ×2 (83, 85); **2036** (101).
Time: **11:38** (15) — recommend the audio script add "a.m." explicitly rather than relying on "next morning" context two sentences up, since chunks render in isolation per AUDIO_SPEC §7.
Temperature: **53 degrees Fahrenheit** / **53 degrees** ×2 (3, 7).
Money: **$3.8 billion** (83) — watch the symbol-before-number order in render text.
Already correctly spelled out in print, no action needed: seventy-three seconds, a hundred and twenty-four, six months, twenty years, five minutes, thirty, four, twenty (largest hospital systems).

---

## Direct answers to your checklist

1. **Breath violations:** two, both quoted above (§7). Neither is catastrophic; both are easy rewrites.
2. **Cadence monotony / the documented tic:** purge holds for the literal banned construction; a two-sentence variant recurs 3x late in the chapter (§5). The five-conditions and gates passages: the *gates* (trigger/delay/review) read as genuine sequence, no hidden-list problem. The *five conditions* passage is structurally sound but runs the word "hole" as an audible tic (§6). Tricolon count is at the edge of the twenty-minute warning (§9).
3. **Weak paragraph endings:** one real instance (§8), everywhere else the chapter reliably lands on the strong beat — including the closing line, which is excellent.
4. **Quote boundaries:** one real ambiguity ("Next April?", §2) and one still-open one-quote-per-source violation (Boisjoly, §4).
5. **Homographs:** two genuine watch-items ("deliberate," "cold read"); everything else on the list either doesn't appear or is context-protected.
6. **Numbers:** full handoff list above; nothing wrong in print, just needs the spoken-form pass before rendering.
7. **Antecedent losses:** one significant forward-reference break ("of the four," §1), one minor pronoun drift (§10).

**Verdict: FIX, not PASS.** Nothing here touches the argument, and most items are single-sentence edits. But #1 (the four/three miscount) and #2 (the unattributed "Next April?") are the kind of thing that actively confuses a listener rather than just sounding slightly off, and #4 (Boisjoly double-quote) is a named style-bible rule that looks like it fell through the cold-review repair pass rather than being intentionally kept. Recommend a fast v4 pass on items 1–6, then this chapter is ready for anchor-prompt recording.
