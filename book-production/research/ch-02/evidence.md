# Ch. 2 ("The Shadow of the Future") — Evidence Packet

Per `CHAPTER_BRIEFS.md`: Axelrod, *The Evolution of Cooperation*; Rapoport; the Christmas truce of
1914. Per `cases.md`, the opening case is the two Computer Prisoner's Dilemma Tournaments and the
second worked example is the WWI live-and-let-live system.

**Primary source used this session:** the actual PDF in the project —
`Files/The_Evolution_of_Cooperation_Revised_z_library_sk,_1lib_sk,_1773177483514_0.pdf` — Robert
Axelrod, *The Evolution of Cooperation*, Revised Edition, Basic Books. I extracted the full text
(`pdftotext -layout`) and read it directly this session, not from memory and not from a secondary
summary. Page numbers below are the book's own printed page numbers (front matter in lowercase
roman, main text in arabic), confirmed by a direct offset check against the table of contents
(chapter openings on pp. 1, 27, 55, 71, 88, 109, 124, 145, 169 all landed exactly where the PDF
text shows a chapter heading — see method note at the end of this file).

Confidence key, matching the convention used in `research/ch-01/evidence.md`: **SOLID** (verified
against direct read of the primary source this session) / **REPORTED-BUT-SINGLE-SOURCE**
(secondary characterization, not independently cross-checked) / **CONTESTED** (the literature
itself disagrees, or a popular claim outruns the sourcing).

---

## 1. The tournaments — core claims

### 1a. The first tournament: structure, entrants, winner

**Confidence: SOLID.** Direct read, Axelrod pp. 30–33, and Appendix A Table 2, p. 193.

- Fourteen entries plus a RANDOM control, round-robin, each pairing run five times, 200 moves per
  game, standard PD payoffs (3/1/5/0). "In all, there were 120,000 moves, making for 240,000
  separate choices." (p. 31)
- "The fourteen submitted entries came from five disciplines: psychology, economics, political
  science, mathematics, and sociology." (p. 31)
- Winner: TIT FOR TAT, submitted by Anatol Rapoport, University of Toronto — "the simplest of all
  submitted programs and it turned out to be the best!" (p. 31)
- Full named-entrant table with discipline, program length, and score: Appendix A, Table 2, p. 193
  (reproduced in full in `cases.md`).

### 1b. The second tournament: scale, and Rapoport re-submitting TIT FOR TAT

**Confidence: SOLID.** Direct read, pp. 41–43.

- "There was a total of sixty-two entries from six countries." (p. 41) Countries named: United
  States, Canada, Great Britain, Norway, Switzerland, New Zealand (p. 41).
- Key quote for the brief's "everyone knew and still couldn't beat it" beat: **"Even though an
  explicit tournament rule allowed anyone to submit any program, even one authored by someone
  else, only one person submitted TIT FOR TAT. This was Anatol Rapoport, who submitted it the
  first time."** (p. 42)
- "TIT FOR TAT was the simplest program submitted in the first round, and it won the first round.
  It was the simplest submission in the second round, and it won the second round. Even though all
  the entrants to the second round knew that TIT FOR TAT had won the first round, no one was able
  to design an entry that did any better." (p. 42)

### 1c. The ecological simulation

**Confidence: SOLID.** Direct read, pp. 48–53.

- Method: successful rules get proportionally more "offspring" (copies) in each simulated future
  generation, unsuccessful rules fewer, modeled on population biology (pp. 48–49).
- "By the fiftieth generation, the rules that ranked in the bottom third of the tournament have
  virtually disappeared." (p. 50)
- HARRINGTON (the one non-nice rule in the top 15) initially thrived by exploiting weak rules, then
  went extinct once its prey died out: "by the one thousandth generation HARRINGTON was as extinct
  as the exploitable rules on which it preyed." (p. 52)

---

## 2. The four properties — exact wording and pages

**Confidence: SOLID** on all four — each is Axelrod's own defined term, in his own words, verified
by direct read.

**Nice** (p. 32–33): "there is a single property which distinguishes the relatively high-scoring
entries from the relatively low-scoring entries. This is the property of being nice, which is to
say never being the first to defect." (p. 33)

**Forgiving** (p. 35–36): "A key concept in this regard is the forgiveness of a decision rule.
Forgiveness of a rule can be informally described as its propensity to cooperate in the moves after
the other player has defected." (p. 36) Contrast case given immediately after: FRIEDMAN, "a totally
unforgiving rule that employs permanent retaliation... In contrast, the winner, TIT FOR TAT, is
unforgiving for one move, but thereafter is totally forgiving of that defection. After one
punishment, it lets bygones be bygones." (p. 36)

**Retaliatory** (p. 44): "A property that distinguishes well among the nice rules themselves is how
promptly and how reliably they responded to a challenge by the other player. A rule can be called
retaliatory if it immediately defects after an 'uncalled for' defection from the other." (p. 44)

**Clear** (pp. 53–54): stated as three conditions under which TIT FOR TAT "benefits from its own
nonexploitability": "1. The possibility of encountering TIT FOR TAT is salient. 2. Once
encountered, TIT FOR TAT is easy to recognize. 3. Once recognized, TIT FOR TAT's nonexploitability
is easy to appreciate. ... Thus TIT FOR TAT benefits from its own clarity." (pp. 53–54)

**The combined statement, exact wording, chapter's closing line (p. 54):**

> "What accounts for TIT FOR TAT's robust success is its combination of being nice, retaliatory,
> forgiving, and clear. Its niceness prevents it from getting into unnecessary trouble. Its
> retaliation discourages the other side from persisting whenever defection is tried. Its
> forgiveness helps restore mutual cooperation. And its clarity makes it intelligible to the other
> player, thereby eliciting long-term cooperation."

This is the cleanest single quotable "thesis paragraph" for the four properties and should very
likely be used near-verbatim (as a block quote or close paraphrase with citation) rather than
re-derived, per the project's general preference (seen in the ch-1 packet) for using an author's own
compressed statement of a mechanism rather than re-deriving it in prose.

---

## 3. "The shadow of the future" — Axelrod's own phrase, exact wording and page

**Confidence: SOLID.** Direct read. This is Axelrod's own coined/adopted phrase, used as a section
heading and repeatedly through the book (I found it at pp. 124, 126, 128, 129, 141, 161, 170, 173,
181, and 185 across chapters 6, 7, 8, and 9 — it is a running term of art, not a one-off).

**First and cleanest use, chapter 7 opening ("How to Promote Cooperation"):**

> "This chapter, on the other hand, does not take the strategic setting as given. Instead it asks
> how one can promote cooperation by transforming the strategic setting itself — for example, by
> enlarging the shadow of the future." (p. 124)

**The section header that names it as a lever, with the mechanism spelled out (pp. 126–129):**

> "1. Enlarge the shadow of the future. Mutual cooperation can be stable if the future is
> sufficiently important relative to the present. This is because the players can each use an
> implicit threat of retaliation against the other's defection — if the interaction will last long
> enough to make the threat effective." (p. 126)

> "The situation changes when the shadow of the future is not so great... as the shadow of the
> future becomes smaller, it stops paying to be cooperative with another player — even if the other
> player will reciprocate your cooperation." (p. 128)

**The explicit link to the trench-warfare case (useful bridge for the Drafter, showing Axelrod
himself treats the truce as *the* illustration of "enlarging the shadow of the future" through
durability of contact):**

> "The most direct way to encourage cooperation is to make the interactions more durable. For
> example, a wedding is a public act designed to celebrate and promote the durability of a
> relationship. Durability of an interaction can help not only lovers, but enemies. The most
> striking illustration of this point was the way the live-and-let-live system developed during the
> trench warfare of World War I." (p. 129)

**Mechanism note for the Drafter:** Axelrod's formal machinery behind "the shadow of the future" is
a discount parameter, w (the weight of the next move's payoff relative to the current move's),
worked through with a numerical example at w = .9 (cooperation pays, 30 points) vs. w = .3
(defection pays, 5.4–6.2 points vs. 4.3) on pp. 126–128. The chapter brief says "no payoff
matrices," so this arithmetic almost certainly should NOT appear in the manuscript prose — but the
Drafter should understand it as the formal content standing behind the metaphor, in case a
skeptical reader/interlocutor beat needs the underlying logic gestured at without the math.

---

## 4. Costly signaling / "integrity as costly signal" — honest note on sourcing

**Confidence: the brief's framing ("integrity as costly signal") is the chapter's own synthesis,
not a phrase Axelrod uses.** I searched the full text for "costly," "signal," and "handicap" and
found no passage where Axelrod himself frames retaliatory-capability demonstrations as "costly
signaling" in so many words. What Axelrod does say, and what the concept should be built on:

> "Likewise the artillery would often demonstrate with a few accurately aimed shots that they could
> do more damage if they wished. These demonstrations of retaliatory capabilities helped police the
> system by showing that restraint was not due to weakness, and that defection would be
> self-defeating." (p. 80)

This — spending real ammunition and real risk to *prove* you could hurt the other side, precisely
so that your ongoing restraint reads as choice rather than incapacity — **is** a costly signal in
the standard game-theoretic/biological sense (a signal that is credible because it would not be
worth faking), even though Axelrod doesn't use that vocabulary. Axelrod does cite Michael Spence's
market-signaling framework once, in an endnote to chapter 8, characterizing a related mechanism as
"an index" in Spence's terminology (Notes to pages 147–63, note 1, referencing Spence, *Market
Signalling*, Harvard University Press, 1974) — but this is a passing footnote, not developed in the
main text, and is about a different specific mechanism (turnover/accountability), not the artillery
demonstrations.

**Recommendation for the Drafter:** ground the "integrity as costly signal" framing on the artillery
/ sniper demonstration-of-capability material (p. 80, quoted in full in `cases.md`), cited as
Axelrod's own account of the mechanism, without attributing the phrase "costly signal" to Axelrod
himself. If the chapter wants a citation for the costly-signaling concept as a named theoretical
frame, the standard references are outside this book: Amotz Zahavi's handicap principle
(biology) or Michael Spence's signaling theory (economics, and the one Axelrod himself cites) —
neither was independently pulled and verified this session; flag as `[PENDING: costly-signaling
theory sourcing]` in `Context/OPEN_QUESTIONS.md` if the Drafter wants a direct citation rather than
just the Axelrod mechanism.

---

## 5. The WWI live-and-let-live system — core claims

All quotations below are Axelrod quoting Ashworth's 1980 book (or Ashworth quoting original
trench-era diaries/memoirs); see the sourcing note in `cases.md` Part Two. Ashworth's book itself
was **not** independently pulled and read this session — only Axelrod's chapter, which explicitly
states it "relies upon Ashworth's fine work for its illustrative quotes and for its historical
interpretation" (p. 75). Confidence below is rated for "this is what Axelrod's book says,"
verified directly; treat as **REPORTED-BUT-SINGLE-SOURCE relative to the original WWI diarists**
(Axelrod → Ashworth → diary), and flag for the Verifier to pull Ashworth's *Trench Warfare
1914–1918* directly before print if the chapter leans heavily on any single quotation's precise
wording.

**Citation for Ashworth:** Ashworth, Tony. *Trench Warfare, 1914–1918: The Live and Let Live
System*. London: Macmillan, 1980.

**Confidence: SOLID** (as Axelrod's own reporting, direct read) on the following claims:

- The live-and-let-live system was widespread and durable despite active opposition from all three
  high commands (British, French, German), who "all wanted to put a stop to tacit truces" (p. 81).
- It arose independently via at least three mechanisms: meal-time synchronization (p. 77),
  short-lived direct/verbal fraternization that was quickly suppressed by court-martial (p. 78),
  and ad hoc weather truces (p. 78).
- It was sustained by demonstrated, credible retaliatory capacity (pp. 79–80) and by
  troop-rotation "socialization" in which outgoing units briefed incoming units on the local tacit
  understandings (pp. 80–81).
- It was destroyed specifically by the headquarters-ordered **raid**, because raids were the one
  form of aggression headquarters could verifiably monitor (unfakeable via prisoners or
  casualties), unlike ordinary "shoot to miss" trench fire (p. 82).
- Axelrod frames the whole case explicitly as an iterated Prisoner's Dilemma between small units
  (battalions), with the formal payoff ordering T>R>P>S derived from the tactical logic, and states
  this is "a case of cooperation emerging despite great antagonism between the players" (pp. 73,
  75).

**Confidence: SOLID**, Axelrod's own two "additions to the theory" from this case, useful for the
chapter if it wants to gesture just slightly beyond pure game theory without collapsing into the
"morality is just strategy" reduction the brief prohibits:

- **Ethics**: the Saxon soldier's apology (Rutter 1934, p. 29, quoted in `cases.md`) — Axelrod's own
  gloss: "This Saxon apology goes well beyond a merely instrumental effort to prevent retaliation.
  It reflects moral regret for having violated a situation of trust" (p. 85).
- **Ritual**: Ashworth's own phrase, quoted by Axelrod, on ritualized/predictable aggression as
  serving "at one and the same time, both sentiments of fellow-feelings, and beliefs that the enemy
  was a fellow sufferer" (Ashworth 1980, p. 144; Axelrod p. 87).

**On the interlocutor objection ("so morality is just self-interest with extra steps"):** Axelrod's
own closing sentence for the chapter is nearly a ready-made answer, and importantly argues the
opposite direction from a full reduction — that the mechanism working *without* friendship is the
finding, not that friendship (or morality) *reduces to* the mechanism: "The live-and-let-live system
that emerged in the bitter trench warfare of World War I demonstrates that friendship is hardly
necessary for cooperation based upon reciprocity to get started. Under suitable circumstances,
cooperation can develop even between antagonists." (p. 87) This supports the brief's instruction to
answer the interlocutor honestly rather than dodge: game theory explains stability of cooperative
dispositions among people who have every reason to hate each other; it does not, on its own, tell
you those dispositions are *right* to have. That's the brief's own line for Part Two, not something
this packet is inventing.

---

## 6. Contested / needs-care items — flagged honestly

### 6a. The "Christmas truce football match"

**Confidence: CONTESTED — and NOT sourceable to Axelrod at all.**

I searched the full text of *The Evolution of Cooperation* for "football" and "soccer." There is
no football match anywhere in Axelrod's account of the trench-warfare case. His chapter 4 does not
mention it. If the chapter wants a football-match beat, it cannot be cited to this source, full
stop.

Independent of Axelrod, current historical scholarship (per web sources checked this session, not
primary-source verified) treats the football match itself as **contested but not fabricated**: there
is evidence of scattered informal kickabouts in no-man's-land in December 1914, but whether an
organized match with sides and a score took place, versus scattered informal games and rumors of
games "elsewhere down the line," is disputed among historians, and the popular image (organized
match, final score, etc.) is generally regarded as an embellishment that grew across a century of
retelling. Tony Ashworth's own scholarly framing (again, per secondary characterization, not this
session's direct read of his book) treats the truce broadly as a pragmatic extension of the
pre-existing live-and-let-live system rather than a singular, spontaneous outbreak of Christmas
spirit — which is consistent with, and supportive of, the brief's actual argument (iteration, not
goodwill, produced the cooperation) and argues *against* leaning on the football anecdote at all,
since the football story tends to be told in service of the sentimental "Christmas magic" framing
the brief explicitly wants to avoid.

**Recommendation: do not use the football match.** Everything the chapter needs is already in
Axelrod's own verified material (the artillery rituals, the ration-truce, the raid that ended it),
which is both stronger evidence and free of the contested-sourcing problem.

### 6b. TIT FOR TAT's sensitivity to noise — later scholarship, honest caveat

**Confidence: SOLID** that this later literature exists and says what follows (verified via web
search this session, not a from-memory recollection; primary papers were not independently pulled
and read in full this session — flag for Verifier if exact wording is needed).

Axelrod's 1984 tournaments were run in a **noise-free** environment — no possibility of a
miscommunicated or accidental defection. Subsequent research (chiefly Martin Nowak and Karl
Sigmund, in the early-to-mid 1990s) showed that in an environment with even a small error rate
(a move accidentally recorded/executed as the wrong choice), plain TIT FOR TAT is fragile: a single
mistaken defection can trigger the same "echo" effect Axelrod himself describes in the JOSS
example (p. 37 — see `cases.md`), except now the echo starts by accident rather than by strategy,
and can lock two otherwise-cooperative players into indefinite mutual defection. Their proposed
fixes:

- **Nowak, M. A., & Sigmund, K. (1992). "Tit for tat in heterogeneous populations." *Nature*, 355
  (6357), 250–253.** Introduces **Generous Tit-for-Tat (GTFT)**: cooperate after the other player
  cooperates; after a defection, cooperate anyway with some fixed positive probability rather than
  automatically retaliating. Shown to be more robust to noise and to be favored by evolutionary
  dynamics over strict TIT FOR TAT in a heterogeneous, error-prone population.
- **Nowak, M. A., & Sigmund, K. (1993). "A strategy of win-stay, lose-shift that outperforms
  tit-for-tat in the Prisoner's Dilemma game." *Nature*, 364, 56–58.** Shows a different rule
  ("Pavlov" / win-stay-lose-shift — repeat your last move if it did well, switch if it did poorly)
  can outperform both TIT FOR TAT and generous TIT FOR TAT under certain conditions, in part because
  it can recover from an accidental mutual-defection spiral in a way plain TIT FOR TAT cannot.

**Recommendation for the chapter:** the four-properties story is still true and still the right
opening case — it's Axelrod's actual, historically real result, not a simplification. But if the
chapter (or the Referee, at Gate 4/5) wants intellectual honesty about the state of the art beyond
1984, the accurate caveat is: *plain* TIT FOR TAT is not the last word even within its own
paradigm — it's excellent in a noise-free world and fragile in a noisy one, and the field's own
answer to that fragility (generosity, calibrated rather than absolute forgiveness) is arguably even
more supportive of the brief's "forgiving" property than the original result was, not a
contradiction of it. This is a "the brief doesn't overstate this, but a smart opponent could push
here" note, not a "the brief is wrong" note — worth one honest sentence in the chapter, not a
derailing detour.

### 6c. The trench-warfare quotations are Axelrod-via-Ashworth, not independently re-verified against original diaries

**Confidence: flagged, not a defect, but should be disclosed.** As noted in section 5 above, this
session verified that Axelrod's book contains these exact quotations at these exact pages. It did
not independently pull Ashworth's *Trench Warfare, 1914–1918* or the original cited memoirs (e.g.,
Dugdale 1932, Hay 1916, Rutter 1934, Sulzbach 1973) to confirm Axelrod/Ashworth transcribed them
correctly. This is a second-order sourcing chain (diarist → Ashworth → Axelrod → this packet), which
is the normal and expected way to use Axelrod's book as a source, but the Verifier should treat the
exact wording of any single trench-diary quotation as **REPORTED-BUT-SINGLE-SOURCE** rather than
independently confirmed, per the project's stated standard that every quotation be exact.

---

## Method note: page-number verification

Book pagination was recovered from the OCR'd PDF (`pdftotext -layout`) by locating the printed folio
number at the bottom of each page in the extracted text and cross-checking the offset against the
table of contents (p. 6–7 of the printed book), which lists chapter start pages (1, 27, 55, 71, 88,
109, 124, 145, 169, plus Appendix A at 192 and Appendix B at 206). I confirmed the offset
(PDF-page-number minus 17 = printed-book-page-number) empirically at more than a dozen points across
the book, including at every chapter opening used in this packet, and the chapter-opening pages in
the extracted text matched the table of contents exactly in every case checked. OCR did introduce
minor character-level errors in a few places (e.g., "if" for "of" in some running heads, "J" for "1"
in a couple of numerals, "7J" for "71" in the table of contents) — none of these affected any of the
quotations reproduced above, which were checked against their surrounding sentence context for
sense in every case.

---

## What still needs a live human/Verifier check before print

1. Independently pull Ashworth 1980 (or at minimum verify the cited diary sources) for the trench-
   warfare quotations, per the project's standing "exact quotation" bar (section 6c above).
2. If the chapter uses the Dawkins foreword anecdote (he was invited, didn't enter), verify against
   the specific edition of the foreword — this session read the "Foreword to the New Edition" bound
   into this particular Revised Edition PDF, dated by internal reference to Dawkins' visit to
   Michigan and to a 2006 Oxford dateline (p. xvii: "RICHARD DAWKINS, Oxford, June 2006") — confirm
   this matches whatever edition the Style/Production team intends to cite formally in the
   bibliography.
3. If the Drafter wants a direct citation for "costly signaling" as a named theoretical frame
   (section 4 above), pull Zahavi's handicap principle or Spence 1974 directly — neither was
   independently verified this session beyond the passing Axelrod footnote.
4. If the chapter cites the Nowak/Sigmund noise material directly (section 6b), pull the two Nature
   papers directly for exact wording rather than relying on this session's secondary
   characterization via web search.
