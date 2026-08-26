# Verifier Report — ch-02 draft-v3.md

Method: independent re-check against the primary source PDF (`Files/The_Evolution_of_Cooperation_Revised_z_library_sk,_1lib_sk,_1773177483514_0.pdf`, 265 pp.), via `pdftotext -layout` and page-by-page (`-f N -l N`) extraction — the packet's page citations were NOT trusted going in. Offset re-verified independently: located the exact phrase "eliciting long-term cooperation" at true PDF page 71; the book's own printed footer on that page reads "54". PDF page − 17 = printed page confirmed at this control point (71 − 17 = 54) and used throughout. Nowak & Sigmund and "courtroom workgroup" checked via CrossRef/web.

Counts: **50 items checked — 46 PASS, 4 FAIL, 3 items carry a NOTE (folded into PASS or FAIL below).**

## Tournament mechanics

| # | Item | Verdict | Source |
|---|---|---|---|
| 1 | Axelrod, political scientist, University of Michigan, late 1970s | PASS | PDF p.1 bio note ("the University of Michigan... He lives in Ann Arbor, Michigan"); Dawkins foreword p.xi ("In the late 1970s... an American political scientist... Robert Axelrod") |
| 2 | "When should a person cooperate, and when should a person be selfish..." (paraphrase, not quoted) | PASS | Preface, p.vi: "THIS PROJECT began with a simple question: When should a person cooperate, and when should a person be selfish, in an ongoing interaction with another person?" |
| 3 | Dawkins wrote foreword to revised edition | PASS | Title page: "With a new Foreword by Richard Dawkins"; signed "RICHARD DAWKINS" at end of foreword |
| 4 | "Computer Prisoner's Dilemma Tournament" framing, announced as tournament | PASS | p.30 (PDF 47): "It was structured as a round robin... As announced in the rules of the tournament..."; table headers throughout use this exact name |
| 5 | 14 entries + RANDOM (15th) | PASS | p.30: "each entry was also paired with its own twin and with RANDOM"; Appendix Table 2 lists ranks 1–14 + RANDOM as 15 |
| 6 | Five disciplines: psychology, economics, political science, mathematics, sociology | PASS | p.31: "came from five disciplines: psychology, economics, political science, mathematics, and sociology" — exact |
| 7 | 200 moves | PASS | p.30: "Each game consisted of exactly two hundred moves" |
| 8 | Round robin incl. self and RANDOM | PASS | p.30, as above |
| 9 | Five runs | PASS | p.31: "the entire round robin tournament was run five times" |
| 10 | 120,000 moves / 240,000 choices | PASS | p.31: "In all, there were 120,000 moves, making for 240,000 separate choices" — exact |
| 11 | Rapoport, U. of Toronto, TIT FOR TAT | PASS | p.31: "TIT FOR TAT, submitted by Professor Anatol Rapoport of the University of Toronto, won the tournament" |
| 12 | TFT shortest program (4 lines), "shortest by a wide margin" | PASS-WITH-NOTE | Appendix Table 2: Rapoport = 4 lines (shortest); next-shortest are Davis and Feld at 6 lines. Shortest confirmed, but "wide margin" overstates it — the gap to the next entry is only 2 lines, not wide. Fix: drop "by a wide margin" or reword to "shorter than anything else submitted." |
| 13 | Won first and second tournament | PASS | p.42: "TIT FOR TAT... won the first round... won the second round" |
| 14 | Tideman & Chieruzzi, 41 lines | PASS | Appendix Table 2, rank 2: "Nicholas Tideman & Paula Chieruzzi, Economics, 41" — exact |
| 15 | Stein & Rapoport, 50 lines | PASS | Appendix Table 2, rank 6: "William Stein & Amnon Rapoport... 50" — exact |
| 16 | Anonymous ("Name withheld") entry, 77 lines, finished second-to-last ahead only of RANDOM | PASS | Appendix Table 2, rank 14: "Name withheld, 77, 282.2"; rank 15: "RANDOM, 276.3" — exact match |
| 17 | Second tournament: 62 entries, six countries | PASS | p.41: "a total of sixty-two entries from six countries... United States, Canada, Great Britain, Norway, Switzerland, and New Zealand" |
| 18 | Second-round entrants had round-one results, knew which program won | PASS | p.41–42: "they all had the report of the earlier round, showing that TIT FOR TAT was the most successful rule so far" |
| 19 | Only Rapoport resubmitted TFT | PASS | p.42: "only one person submitted TIT FOR TAT. This was Anatol Rapoport, who submitted it the first time" — exact |
| 20 | FRIEDMAN, permanent retaliation, scored worst of the "nice" rules (Ch.2/p.36 framing) | PASS | p.36: "Of all the nice rules, the one that scored lowest was also the one that was least forgiving. This is FRIEDMAN, a totally unforgiving rule that employs permanent retaliation." Draft accurately reflects Axelrod's own claim (note: Appendix Table 2 actually shows Davis at 471.8 vs. Friedman's 473.4 — a ~1.6-point discrepancy internal to Axelrod's own book, not a draft error) |
| 21 | FRIEDMAN "loses... to almost everything, including strategies pettier than plain forgiveness" (draft line ~64, ANCHOR section) | **FAIL** | Appendix Table 2: FRIEDMAN ranked **7th of 15** in round one, score 473.4 — it beat Graaskamp (401), Downing (391), Feld (328), Joss (304), Tullock (301), Name Withheld (282), and RANDOM (276), i.e., half the field. It did not "lose to almost everything." Fix: reword to something Axelrod's data actually supports — e.g., "permanent retaliation scored worse than every rule that forgave" (true: it was the lowest-scoring *nice* rule) — not a claim that it lost broadly. |
| 22 | Downing's entry: modeled opponent, calculated, opened by assuming the worst, self-fulfilling | PASS | p.34: outcome-maximization; p.35: "By initially assuming that the other player is unresponsive, DOWNING is doomed to defect on the first two moves. These first two defections led many other rules to punish DOWNING" — Downing, psychologist, ranked 10/15 (score 390.6), consistent with "ahead of only a handful" |
| 23 | Ecological simulation: 50th generation bottom third gone; HARRINGTON early success then extinct by 1000th gen | PASS | p.51: "By the fiftieth generation, the rules that ranked in the bottom third of the tournament have virtually disappeared"; p.52: HARRINGTON "only non-nice rule among the top fifteen finishers in the second round"..."by the one thousandth generation HARRINGTON was as extinct as the exploitable rules on which it preyed" |
| 24 | Four-properties synthesis quote, exact, p.54 | PASS (minor note) | PDF p.71 = printed p.54, verbatim: "Its niceness prevents it from getting into unnecessary trouble. Its retaliation discourages the other side from persisting whenever defection is tried. Its forgiveness helps restore mutual cooperation. And its clarity makes it intelligible to the other player, thereby eliciting long-term cooperation." Draft matches word-for-word. Only deviation: draft lowercases the opening "Its" → "its" to splice into its own sentence — technically not verbatim capitalization, but standard integration convention. |

## Trench material (Ch. 4)

| # | Item | Verdict | Source |
|---|---|---|---|
| 25 | Framed formally as iterated PD between small units (battalions), pp.73, 75 | PASS | p.75: battalion (~1,000 men) as the player; p.73–75 lays out the T>R>P>S inequalities for small units |
| 26 | Scope: "concentrated in the quiet, static stretches... a minority experience of the war rather than its rule, on Ashworth's own accounting" | **FAIL** | Axelrod's own language cuts the other way: p.73, "This is not an isolated example. The live-and-let-live system was endemic in trench warfare"; p.74, material drawn "from virtually every one of the fifty-seven British divisions." "Sector-dependent" (quiet sectors, lulls between offensives) is supported; "minority experience... rather than its rule" is not stated anywhere in Axelrod's chapter and is in tension with "endemic" / "not an isolated example." Fix: drop the "on Ashworth's own accounting" attribution for the minority claim, or soften to something like "concentrated in the quiet stretches, not the set-piece battles" without the "minority of the war" quantifier. |
| 27 | "the historian Tony Ashworth" | **FAIL** | p.74: "This excellent work by a British **sociologist**, Tony Ashworth (1980)." Axelrod explicitly calls him a sociologist, not a historian. Fix: change "historian" to "sociologist." |
| 28 | Ashworth-disclosure clause: leans on Ashworth's research/quotes rather than the diaries themselves, "secondhand twice over" | PASS | p.74: "This chapter relies upon Ashworth's fine work for its illustrative quotes and for its historical interpretation" — confirms even the primary-source-looking quotes (Dugdale, Kelly, Hay, Rutter, Koppen, etc.) are drawn via Ashworth, not independently by Axelrod |
| 29 | Ration parties get careless, quiet hour, pp.77–78 | PASS | p.77 quote: "the ration parties became careless because of it, and laughed and talked" |
| 30 | Direct fraternization suppressed fast, courtmartialed, p.78 | PASS (minor note) | p.78: "several soldiers were courtmartialed and whole battalions were punished." The specific details "trade tobacco, shake hands across the wire" are not in Axelrod's text (which mentions "extensive fraternization" generically) — plausible period color but unsourced specifics; not false, just embellished beyond the citation. |
| 31 | Foul-weather truces, p.78 | PASS | p.78: "Another way in which mutual restraint got started was during a spell of miserable weather... ad hoc weather truces emerged" |
| 32 | German snipers, cottage wall, demonstrating accuracy not malice, p.79 | PASS | p.79: "German snipers showed their prowess to the British by aiming at spots on the walls of cottages and firing until they had cut a hole"; "showing that restraint was not due to weakness" |
| 33 | British "evening gun," predictable, watched at ~7pm, pp.79–80, 86 | PASS | p.86: German soldier quote, "At seven it came—so regularly that you could set your watch by it... some inquisitive fellows who crawled out... a little before seven, in order to see it burst" |
| 34 | New units briefed informally by outgoing units, pp.80–81 | PASS | p.80–81: informal handoff, "Mr. Bosche ain't a bad fellow. You leave 'im alone; 'e'll leave you alone" |
| 35 | Ashworth quote, "both sentiments of fellow-feelings, and beliefs that the enemy was a fellow sufferer" (Ashworth 1980, p.144; Axelrod p.87) | PASS | Verbatim on printed p.87 (confirmed via footer-page tracing): "...symbolized and strengthened, at one and the same time, both sentiments of fellow-feelings, and beliefs that the enemy was a fellow sufferer. (Ashworth 1980, p. 144)" — exact, and page attribution (Axelrod p.87, not p.86) is correct |
| 36 | High commands (British/French/German) hated it, tried to stamp it out, p.81 | PASS | p.81: "The high commands of the British, French, and German armies all wanted to put a stop to tacit truces" |
| 37 | Saxon apology quote, pp.84–85: "we are very sorry about that, we hope no one was hurt, it is not our fault, it is that damned Prussian artillery" | **FAIL** | Source (p.85, Rutter 1934, p.29): "**We** are very sorry about that**;** we hope no one was hurt**.** It is not our fault, it is that damned Prussian artillery." Draft changes the semicolon and period to commas, altering the quote's internal punctuation — beyond the acceptable lowercase-for-splicing convention. Fix: restore "We are very sorry about that; we hope no one was hurt. It is not our fault, it is that damned Prussian artillery." (page range pp.84–85 is correct — setup begins p.84, quote itself on p.85) |
| 38 | Raid mechanism: 10–200 men, kill/capture, produces unfakeable prisoners/bodies, p.82 | PASS | p.82: "the raid... involved from ten to two hundred men. Raiders were ordered to kill or capture the enemy... There was no effective way to pretend that a raid had been undertaken when it had not" — exact |
| 39 | Axelrod's conclusion: friendship not necessary for reciprocal cooperation, p.87 | PASS | p.87: "the live-and-let-live system... demonstrates that friendship is hardly necessary for cooperation based upon reciprocity to get started" |

## Nowak & Sigmund / other external claims

| # | Item | Verdict | Source |
|---|---|---|---|
| 40 | Nowak & Sigmund, generous TFT, 1992 | PASS | CrossRef: Nowak, M.A. & Sigmund, K., "Tit for tat in heterogeneous populations," *Nature* 355, 250–253 (1992) |
| 41 | Nowak & Sigmund, win-stay-lose-shift ("Pavlov"), 1993, can beat TFT | PASS | CrossRef: Nowak, M.A. & Sigmund, K., "A strategy of win-stay, lose-shift that outperforms tit-for-tat in the Prisoner's Dilemma game," *Nature* 364, 56–58 (1993) |
| 42 | "Courtroom workgroup" — real criminology term, matches draft's description | PASS | Established term from Eisenstein & Jacob (1977), *Felony Justice*; describes judges/prosecutors/defense counsel as a recurring informal working group — matches draft's use via Marisol almost exactly, including the "clears the docket vs. fair to the person passing through" tension the draft raises in the same breath |
| 43 | Christmas-truce-football claim explicitly declined, no truce/football asserted | PASS | Draft line: "A version of this story, with a Christmas football match in no-man's-land... isn't in Axelrod's account, so I'm leaving it out." Confirmed — no football/match content anywhere in Ch.4; only "extensive fraternization" at Christmas is mentioned (p.78), no football. Draft's non-claim is accurate. |
| 44 | "Stag hunt" description (trust-based coordination game, distinct engine) | PASS | Not from Axelrod (not cited to a page, correctly) — standard, accurately stated game-theory concept, general knowledge |
| 45 | JOSS echo-loop example, p.37 | PASS | p.36–37: JOSS defects probabilistically after cooperation; "the single defection of JOSS on the sixth move created an echo back and forth" — on printed p.37 |
| 46 | Shadow of the future mechanics, pp.124–126 | PASS | pp.124–128: discount parameter w, numeric example, "the future casts a large enough shadow" |
| 47 | Wedding example, p.129 | PASS | p.129: "a wedding is a public act designed to celebrate and promote the durability of a relationship" |
| 48 | Niceness definition, p.33 | PASS | p.33: "the property of being nice, which is to say never being the first to defect" |
| 49 | Retaliatory definition, p.44 | PASS | p.44: "A rule can be called retaliatory if it immediately defects after an 'uncalled for' defection from the other" |
| 50 | Forgiving definition + FRIEDMAN contrast, p.36 | PASS | p.36 (see #20 above) |

## Summary — FAILs requiring fixes

1. **Line ~64 (ANCHOR section):** "permanent retaliation loses... to almost everything, including strategies pettier than plain forgiveness" — factually wrong; FRIEDMAN beat half the field (7th of 15, score 473.4). Reword to the claim Axelrod's data actually supports: FRIEDMAN was the lowest-scoring of the *nice* rules, not a broad loser.
2. **Line 37:** "the historian Tony Ashworth" → should be "the **sociologist** Tony Ashworth" (Axelrod, p.74, calls him "a British sociologist").
3. **Line 37:** "a minority experience of the war rather than its rule, on Ashworth's own accounting" — not supported by Axelrod's text, which calls the system "endemic" and "not an isolated example," drawn from virtually all 57 British divisions. Drop the "minority" framing or the "on Ashworth's own accounting" attribution.
4. **Line 45:** Saxon-soldier quote punctuation altered from source (semicolon/period → commas). Restore exact punctuation: "We are very sorry about that; we hope no one was hurt. It is not our fault, it is that damned Prussian artillery."

## Notes (non-blocking)

- The p.54 "four properties" quote and the offset itself are solid — re-verified independently at PDF p.71/printed p.54, matching the packet's stated PDF−17 offset.
- Minor unsourced narrative color (punch cards, mainframe printout, "tobacco and handshakes" for fraternization) is plausible period detail but not literally in Axelrod's text — flagged as style, not fact-checking failures, since it's not presented as sourced/quoted material.
- "TIT FOR TAT... shortest by a wide margin" (item 12) slightly overstates a 2-line gap; cosmetic, author's call whether to soften.
