# Ch. 2 ("The Shadow of the Future") — Candidate Cases

Brief: opening case is locked — Axelrod's computer tournaments, told as a story with named
entrants, Anatol Rapoport's four-line TIT FOR TAT winning, then winning again when everyone
knew it was coming. Second illustration: the WWI Christmas truce / live-and-let-live system as
the case of iteration producing cooperation between people who are not "good" to each other by
any ordinary meaning of the word — enemies trying to kill each other.

Every quotation and page number below comes from a direct read this session of the primary
source: Robert Axelrod, *The Evolution of Cooperation*, Revised Edition (Basic Books). Page
numbers are the book's own printed pagination (confirmed against the table of contents and
cross-checked against multiple page markers — see method note at the end of `evidence.md`), not
PDF page numbers. See `evidence.md` for the full sourcing apparatus, confidence ratings, and the
later-scholarship caveats.

---

## PART ONE — The opening case, built out: the Computer Prisoner's Dilemma Tournaments

### The people

**Robert Axelrod** — political scientist, University of Michigan. Origin of the whole project:
"THIS PROJECT began with a simple question: When should a person cooperate, and when should a
person be selfish, in an ongoing interaction with another person?" (Preface, p. vii). He invited
"experts in game theory to submit programs for a Computer Prisoner's Dilemma
Tournament — much like a computer chess tournament" (Preface, p. vii).

**Anatol Rapoport** — the entrant who matters. Professor of Psychology, University of Toronto.
Submitted **TIT FOR TAT**, a four-line program, to *both* rounds of the tournament, and won
*both* times. Axelrod: "TIT FOR TAT, submitted by Professor Anatol Rapoport of the University of
Toronto, won the tournament. This was the simplest of all submitted programs and it turned out to
be the best!" (p. 31).

**The other thirteen first-round entrants** (named, ranked, with discipline and program length in
FORTRAN statements, from Appendix A, Table 2, p. 193 — Axelrod's own summary table):

| Rank | Name | Discipline | Program length | Score |
|---|---|---|---|---|
| 1 | Anatol Rapoport | Psychology | 4 | 504.5 |
| 2 | Nicholas Tideman & Paula Chieruzzi | Economics | 41 | 500.4 |
| 3 | Rudy Nydegger | Psychology | 23 | 485.5 |
| 4 | Bernard Grofman | Political Science | 8 | 481.9 |
| 5 | Martin Shubik | Economics | 16 | 480.7 |
| 6 | William Stein & Amnon Rapoport | Mathematics / Psychology | 50 | 477.8 |
| 7 | James W. Friedman | Economics | 13 | 473.4 |
| 8 | Morton Davis | Mathematics | 6 | 471.8 |
| 9 | James Graaskamp | (unlisted) | 63 | 400.7 |
| 10 | Leslie Downing | Psychology | 33 | 390.6 |
| 11 | Scott Feld | Sociology | 6 | 327.6 |
| 12 | Johann Joss | Mathematics | 5(?) | 304.4 |
| 13 | Gordon Tullock | Economics | 18 | 300.5 |
| 14 | *Name withheld* | (unlisted) | 77 | 282.2 |
| — | RANDOM (the control) | — | 5 | 276.3 |

Note the vivid detail for the chapter: **one of the fourteen entrants asked Axelrod to withhold
their name**, and their program — long, complicated, 77 statements — came in dead last among the
named entries, ahead of only the random-noise control. Axelrod does not explain why the name was
withheld (I found no further gloss on this in the chapters or appendix text read this session);
it's a fact worth the Drafter having in hand, not a mystery to over-read.

**Johann Joss** is a nice authenticating detail beyond the tournament itself: Axelrod notes that
in the Second World Computer Chess Championship the *least* complex program came in *last*
(Jennings 1978), and that program's author, Johann Joss of the Eidgenössische Technische
Hochschule Zürich, *also* entered the Prisoner's Dilemma tournament — with a slight modification
of TIT FOR TAT that only made it worse (p. 32). Useful contrast for the "in chess complexity wins,
here it didn't" beat, if the Drafter wants it — but a secondary character, not primary.

### How the first tournament was announced and run

Not a casual poll — Axelrod solicited it formally, from people already publishing on the subject:
"Wanting to find out what would happen, I invited professional game theorists to send in entries
to just such a computer tournament. It was structured as a round robin, meaning that each entry
was paired with each other entry. As announced in the rules of the tournament, each entry was also
paired with its own twin and with RANDOM" (p. 30). "The fourteen submitted entries came from five
disciplines: psychology, economics, political science, mathematics, and sociology" (p. 31).

Mechanically: "Each game consisted of exactly two hundred moves" (p. 30), the payoff was "3 points
for mutual cooperation, and 1 point for mutual defection. If one player defected while the other
player cooperated, the defecting player received 5 points and the cooperating player received 0
points" (pp. 30–31) — the classic Prisoner's Dilemma payoff. "The entire round robin tournament was
run five times to get a more stable estimate of the scores for each pair of players. In all, there
were 120,000 moves, making for 240,000 separate choices" (p. 31).

Richard Dawkins' foreword adds outside texture to the announcement itself — he was one of the
people invited and, notably, *didn't* enter: "In the late 1970s... I received out of the blue a
typescript from an American political scientist whom I didn't know: Robert Axelrod. It announced a
'computer tournament' to play the game of Iterated Prisoner's Dilemma and invited me to compete...
I'm afraid I didn't get around to sending in an entry" (Foreword, pp. xi–xii). This is a good,
almost self-deprecating aside if the Drafter wants texture on how informal and how widely the net
was cast — a leading evolutionary biologist got the invitation and let it sit.

### What won, and why — in Axelrod's own analytic language

"TIT FOR TAT, of course, starts with a cooperative choice, and thereafter does what the other
player did on the previous move" (p. 31). Four lines of logic; no memory of anything but the last
move; no modeling of the opponent; no cleverness.

The single property that separated winners from losers in round one: **niceness** — "never being
the first to defect" (p. 32). "Each of the eight top-ranking entries (or rules) is nice. None of the
other entries is" (p. 33).

The most sophisticated entry, **DOWNING** (based on Leslie Downing's "outcome maximization"
model), tried to build an actual model of the opponent and calculate the payoff-maximizing move —
and it lost, because its pessimistic starting assumption about the other player doomed it to defect
on the first two moves, which then got it punished (pp. 34–35). Axelrod's explicit lesson: "none of
the more complex programs submitted was able to perform as well as the original, simple TIT FOR
TAT" (p. 32).

Table 1 (p. 37) walks a full move-by-move game between TIT FOR TAT and **JOSS** (a "sneaky" rule
that defects 10% of the time after the other cooperates) — showing exactly how a single
unprovoked defection can set off an "echo" of mutual recrimination that locks both players into
defection for the rest of the 200-move game. This is the mechanism, in miniature, for how a single
betrayal can poison an otherwise-cooperative relationship — a strong concrete illustration if the
Drafter wants a compact within-tournament example rather than just naming the properties abstractly.

### The second tournament: everyone knew, and still couldn't beat it

The second round drew **sixty-two entries from six countries** — the United States, Canada, Great
Britain, Norway, Switzerland, and New Zealand (p. 41) — "from a ten-year-old computer hobbyist to
professors of computer science, physics, economics, psychology, mathematics, sociology, political
science, and evolutionary biology" (p. 41). Every entrant had access to the full published report
of round one, including the explicit finding that niceness and forgiveness were what mattered (p.
42).

The decisive detail for the chapter's argument: **"Even though an explicit tournament rule allowed
anyone to submit any program, even one authored by someone else, only one person submitted TIT FOR
TAT. This was Anatol Rapoport, who submitted it the first time"** (p. 42). Everyone knew the
winning program; nobody, having seen exactly what it was and how simple it was, chose to just copy
it — most tried to *beat* it instead. It won again anyway: "TIT FOR TAT was the simplest program
submitted in the first round, and it won the first round. It was the simplest submission in the
second round, and it won the second round. Even though all the entrants to the second round knew
that TIT FOR TAT had won the first round, no one was able to design an entry that did any better"
(p. 42).

Axelrod's own diagnosis of *why* the field, forewarned, still lost: two lessons circulated after
round one — "Lesson One was: 'Be nice and forgiving.' Lesson Two was more exploitative: 'If others
are going to be nice and forgiving, it pays to try to take advantage of them.'" The Lesson Two
players (**TESTER**, submitted by David Gladstein, and **TRANQUILIZER**, submitted by Craig
Feathers — both named, both real people, both worth using if the Drafter wants named antagonists
beyond Rapoport) built probing, exploitative strategies specifically to prey on generous rules like
TIT FOR TWO TATS. They picked off the suckers — but scored badly overall themselves, because
"in trying to exploit other rules, they often eventually got punished enough to make the whole game
less rewarding for both players than pure mutual cooperation would have been." TESTER finished
46th of 63; TRANQUILIZER 27th (pp. 44–47). Cleverness against a nice, retaliatory, forgiving,
clear strategy is a losing long game even for the clever.

Also worth noting for texture: TIT FOR TWO TATS (a *more* forgiving variant that only retaliates
after two consecutive defections) had actually been shown, after round one, to be a rule that would
have *beaten* TIT FOR TAT in round one's environment — and it was submitted in round two, by name,
by evolutionary biologist **John Maynard Smith** of the UK. It still only placed 24th (p. 47),
because in the more hostile, forewarned second-round field, its extra generosity got exploited by
TESTER. This is a genuinely useful nuance for the chapter if it wants to avoid oversimplifying "be
more forgiving, always win" — forgiveness has to be calibrated to the actual field of players, which
is itself the book's deeper point (robustness, not perfection, is what TIT FOR TAT offers).

### The ecological simulation — cooperation compounding over "generations"

Axelrod ran a third experiment: simulate what happens over many future "generations" of the
tournament if successful rules proliferate (more copies of themselves enter future rounds) and
unsuccessful ones die out — modeled directly on population biology (pp. 48–49). Result: "the
lowest-ranking eleven entries fall to half their initial size by the fifth generation... By the
fiftieth generation, the rules that ranked in the bottom third of the tournament have virtually
disappeared" (p. 50). The one non-nice rule that had cracked the top fifteen, **HARRINGTON**,
looked like a winner early — it was exploiting the suckers — but "by the two hundredth generation
or so... there were fewer and fewer prey for HARRINGTON to exploit. Soon HARRINGTON could not keep
up with the successful nice rules, and by the one thousandth generation HARRINGTON was as extinct
as the exploitable rules on which it preyed" (p. 52). This is the single best line for the chapter
if it wants a coda beyond the tournament proper: exploitation is not just morally worse, it is
*ecologically self-terminating* — it destroys the very population of suckers it depends on.

### The summary statement — the four properties, together, exact wording

The passage that essentially *is* the brief's "four properties" beat, verbatim, closing chapter 2:

> "What accounts for TIT FOR TAT's robust success is its combination of being nice, retaliatory,
> forgiving, and clear. Its niceness prevents it from getting into unnecessary trouble. Its
> retaliation discourages the other side from persisting whenever defection is tried. Its
> forgiveness helps restore mutual cooperation. And its clarity makes it intelligible to the other
> player, thereby eliciting long-term cooperation." (p. 54)

This is the natural closing line for the opening case, if the Drafter wants a locked quote to land
the section on. See `evidence.md` for each property's individual definition and page, plus the
exact wording of "the shadow of the future" and its page.

---

## PART TWO — Second worked example: the WWI live-and-let-live system, built out

### The source behind Axelrod's chapter

Axelrod's chapter 4 ("The Live-and-Let-Live System in Trench Warfare in World War I") is itself
explicitly a synthesis of one book: "Fortunately, a recent book-length study of the
live-and-let-live system is available. This excellent work by a British sociologist, Tony Ashworth
(1980), is based upon diaries, letters, and reminiscences of trench fighters. Material was found
from virtually every one of the fifty-seven British divisions, with an average of more than three
sources per division" (p. 74). Axelrod: "This chapter relies upon Ashworth's fine work for its
illustrative quotes and for its historical interpretation" (p. 75). **Every quotation below that
Axelrod attributes to a WWI-era diary/memoir source, he is in turn quoting out of Ashworth's 1980
book**, unless otherwise noted — the Drafter should treat this as secondhand sourcing (Axelrod →
Ashworth → the original soldier's diary), which is worth being honest about if the chapter cites
the original diarists by name, since this session did not independently pull Ashworth's own book.

**Citation:** Ashworth, Tony. *Trench Warfare, 1914–1918: The Live and Let Live System*. London:
Macmillan, 1980.

### The people / places / dates

- **Western Front**, France and Belgium, "the five-hundred-mile line" (p. 73), primarily the
  static trench-warfare period following the mobile opening phase of August 1914.
- **The battalion** — roughly 1,000 men, half in the front line at any time — is, per Axelrod, "the
  most typical player": large enough to be held accountable by its own high command for what
  happened in its sector, small enough that its officers could actually control what its men did
  (pp. 75–76).
- No single named protagonist the way Rapoport is named for the tournament — this is a structural,
  anonymous-mass phenomenon by design, which the Drafter should treat as a feature, not a gap: the
  point of the case is that it required no leadership and no shared values, only repeated contact.
  The quotations below are attributed only as Axelrod/Ashworth attribute them (rank, unit, or
  simply a cited memoir title).

### The opening detail — a British staff officer's astonishment

The single best cold-open quote for the chapter, verified exact from the primary text:

> "[I was] astonished to observe German soldiers walking about within rifle range behind their own
> line. Our men appeared to take no notice. I privately made up my mind to do away with that sort
> of thing when we took over; such things should not be allowed. ... These people evidently did not
> know there was a war on. Both sides apparently believed in the policy of 'live and let live.'"
> (Dugdale 1932, p. 94; quoted in Axelrod, pp. 73–74)

### How it started

Three separate, independently-arising mechanisms, each with a sourced example:

**1. Mealtime synchronization.** A noncommissioned officer, November 1914: "the quartermaster used
to bring the rations up ... each night after dark; they were laid out and parties used to come from
the front line to fetch them. I suppose the enemy were occupied in the same way; so things were
quiet at that hour for a couple of nights, and the ration parties became careless because of it, and
laughed and talked on their way back to their companies." (*The War the Infantry Knew*, 1938, p. 92;
Axelrod, pp. 77–78)

**2. Direct fraternization** — spread by shout or signal, quickly and deliberately suppressed by
headquarters. "By Christmas there was extensive fraternization, a practice which the headquarters
frowned upon" (p. 78). An eyewitness: "In one section the hour of 8 to 9 A.M. was regarded as
consecrated to 'private business,' and certain places indicated by a flag were regarded as out of
bounds by the snipers on both sides." (Morgan 1916, pp. 270–71; Axelrod, p. 78) Orders soon followed
making clear the men "were in France to fight and not to fraternize with the enemy" (Fifth
Battalion the Camaronians, 1936, p. 28); "several soldiers were courtmartialed and whole
battalions were punished" (p. 78) — direct, verbal truces were fragile precisely because headquarters
could detect and punish them.

**3. Weather truces.** "When the rains were bad enough, it was almost impossible to undertake major
aggressive action. Often ad hoc weather truces emerged in which the troops simply did not shoot at
each other. When the weather improved, the pattern of mutual restraint sometimes simply continued"
(p. 78).

The mechanism that actually lasted, per Axelrod, was **tacit coordination without words** — because
verbal/visible truces got soldiers court-martialed, but a pattern of "we won't shell your ration
wagons if you don't shell ours" required no communication and left no evidence for headquarters to
act on (pp. 78–79). Illustrative quote, summer 1915: "It would be child's play to shell the road
behind the enemy's trenches, crowded as it must be with ration wagons and water carts, into a
bloodstained wilderness ... but on the whole there is silence. After all, if you prevent your enemy
from drawing his rations, his remedy is simple: he will prevent you from drawing yours." (Hay 1916,
pp. 224–25; Axelrod, p. 79)

### The artillery-predictability rituals — verified, with exact texture

This is the strongest "costly, legible signal" material in the whole chapter and maps directly onto
the brief's "clear" property and "integrity as costly signal" theme.

**Demonstrating retaliatory capacity (so restraint reads as choice, not weakness):** "German snipers
showed their prowess to the British by aiming at spots on the walls of cottages and firing until
they had cut a hole" (*The War the Infantry Knew*, 1938, p. 98; Axelrod, p. 79). "Likewise the
artillery would often demonstrate with a few accurately aimed shots that they could do more damage
if they wished. These demonstrations of retaliatory capabilities helped police the system by showing
that restraint was not due to weakness, and that defection would be self-defeating" (p. 80).

**Predictable, ritualized artillery fire — the clearest verified example in the chapter of a
"clock-like" cooperative signal:**

> "So regular were they [the Germans] in their choice of targets, times of shooting, and number of
> rounds fired, that, after being in the line one or two days, Colonel Jones had discovered their
> system, and knew to a minute where the next shell would fall. His calculations were very accurate,
> and he was able to take what seemed to uninitiated Staff Officers big risks, knowing that the
> shelling would stop before he reached the place being shelled." (Hills 1919, p. 96; Axelrod, p. 86)

And the mirror-image British version — literally called "the evening gun," per a German soldier's
own account:

> "At seven it came — so regularly that you could set your watch by it. ... It always had the same
> objective, its range was accurate, it never varied laterally or went beyond or fell short of the
> mark. ... There were even some inquisitive fellows who crawled out ... a little before seven, in
> order to see it burst." (Köppen 1931, pp. 135–37; Axelrod, p. 86)

**Breakfast truces:** the German artillery man's account of infantry solicitousness toward artillery
observers who might disrupt the peace — "If they ever have any delicacies to spare, they make us a
present of them, partly of course because they feel we are protecting them" (Sulzbach 1973, p. 71;
Axelrod, p. 81) — and the informal exchange between infantry and a new forward observer: "I hope you
are not going to start trouble," to which the best answer was "Not unless you want" (Ashworth 1980,
p. 169; Axelrod, p. 81). I did **not** find a specific, named "breakfast truce" episode with that
exact label in the pages read this session — the brief's phrase "breakfast truces" is closest to
the general "private business" hour (8–9 A.M., cited above, p. 78) and the mealtime-synchronization
origin story (p. 77). Flag for the Drafter: don't invent a named "breakfast truce" scene that isn't
in Axelrod's text; use the "private business" hour and ration-party quotes instead, which are
verified.

**Two-for-one / three-for-one retaliation norms — the system's version of "retaliatory but not
disproportionate in a runaway way":**

> "We go out at night in front of the trenches. ... The German working parties are also out, so it
> is not considered etiquette to fire. The really nasty things are rifle grenades. ... They can kill
> as many as eight or nine men if they do fall into a trench. ... But we never use ours unless the
> Germans get particularly noisy, as on their system of retaliation three for every one of ours come
> back." (Greenwell 1972, pp. 16–17; Axelrod, p. 80)

### What destroyed it — the raid, ordered from headquarters

This is the clean causal ending the brief wants, and Axelrod states it explicitly and mechanically:

> "What finally destroyed the live-and-let-live system was the institution of a type of incessant
> aggression that the headquarters could monitor. This was the raid, a carefully prepared attack on
> enemy trenches which involved from ten to two hundred men. Raiders were ordered to kill or capture
> the enemy in his own trenches. If the raid was successful, prisoners would be taken; and if the
> raid was a failure, casualties would be proof of the attempt. There was no effective way to
> pretend that a raid had been undertaken when it had not." (p. 82)

Why this specific tactic, and not ordinary shelling, is what broke the system: headquarters could
not monitor whether ordinary firing was "shooting to kill" or "shooting to avoid retaliation" — but
a raid produced unfakeable proof (prisoners or casualties), so it was the one order that could be
verified and therefore enforced (p. 82). And the raid, once ordered and monitored from headquarters
rather than initiated by the men on the ground, couldn't be locally de-escalated the way an
ordinary skirmish could: "since raids could be ordered and monitored from headquarters, the
magnitude of the retaliatory raid could also be controlled, preventing a dampening of the process.
The battalions were forced to mount real attacks on the enemy, the retaliation was undampened, and
the process echoed out of control" (p. 82). Axelrod's own irony flag, worth keeping: the British
High Command's *initial* purpose in ordering raids was political — to show the French allies they
were pulling their weight — not a deliberate attempt to kill the truce system (p. 83). It destroyed
cooperation as a side effect of a policy aimed at something else entirely.

### The two things Axelrod says are new to the theory here: ethics and ritual

Worth flagging for the chapter because they go *beyond* pure game theory, which is useful if the
chapter wants to gesture — without collapsing into it — toward the idea that repeated cooperation
can generate something that looks like real regard, without yet claiming that's what morality *is*.

**The Saxon apology** — moral regret, not just strategic repair:

> "I was having tea with A Company when we heard a lot of shouting and went out to investigate. We
> found our men and the Germans standing on their respective parapets. Suddenly a salvo arrived but
> did no damage. Naturally both sides got down and our men started swearing at the Germans, when all
> at once a brave German got on to his parapet and shouted out 'We are very sorry about that; we
> hope no one was hurt. It is not our fault, it is that damned Prussian artillery.'" (Rutter 1934,
> p. 29; Axelrod, pp. 84–85)

Axelrod's own gloss: "This Saxon apology goes well beyond a merely instrumental effort to prevent
retaliation. It reflects moral regret for having violated a situation of trust" (p. 85).

**Ritual as dual-audience signaling** — Ashworth's own words, quoted by Axelrod:

> "In trench war, a structure of ritualised aggression was a ceremony where antagonists participated
> in regular, reciprocal discharges of missiles, that is, bombs, bullets and so forth, which
> symbolized and strengthened, at one and the same time, both sentiments of fellow-feelings, and
> beliefs that the enemy was a fellow sufferer." (Ashworth 1980, p. 144; Axelrod, p. 87)

### Axelrod's own closing line for the chapter — good candidate for the chapter's transition out

> "The live-and-let-live system that emerged in the bitter trench warfare of World War I
> demonstrates that friendship is hardly necessary for cooperation based upon reciprocity to get
> started. Under suitable circumstances, cooperation can develop even between antagonists." (p. 87)

This is close to a ready-made statement of the chapter's whole thesis and sits right at the
"must not reduce love/friendship to strategy" boundary — it says the *opposite*, that this
mechanism works precisely because friendship is absent, which is useful cover for the Drafter to
lean on when handling the interlocutor's "so morality is just self-interest with extra steps"
objection.

### What is NOT in Axelrod's account — flag for the Drafter

**No football match.** I searched the full text of both the tournament chapter and the trench-
warfare chapter (and the whole book) for "football" / "soccer" — zero hits describing a Christmas
Day match. **Axelrod's own chapter contains no football scene at all.** The popular "Christmas
truce football match" image comes from other WWI popular histories and media (and is itself
contested among historians — see `evidence.md`). If the Drafter wants that image, it is not
supportable by citing Axelrod, and should either be dropped or very carefully hedged and sourced
elsewhere with the contested status disclosed.

**No single named "protagonist."** Unlike the tournament (where Rapoport is a genuine named
character), the trench-warfare case is intentionally about anonymous, interchangeable small units.
If the Drafter wants a named human face for this section, the best-attested option in the text
above is the unnamed British staff officer's astonished remark (p. 73) as a cold open, or the
"brave German" who apologized (p. 84) as a mid-section beat — neither is a named individual in
Axelrod's text.

---

## PART THREE — Recommended second worked example beyond the truce, if the chapter wants one

The brief pairs the tournament with the Christmas truce specifically, and that pairing is strong
and sufficient — both are already fully built out above and both are richly sourced. If the Drafter
finds, in drafting, that a *third*, non-military example would help ground "shadow of the future"
in ordinary modern life (Axelrod's own chapter 7, "How to Promote Cooperation," gestures at exactly
this need), the strongest candidate surfaced this session, straight from Axelrod's own text, is:

**The "durability of a relationship" bridge Axelrod himself draws from trench warfare to
everyday life** — he explicitly generalizes from the trench-warfare case to ordinary institutions:
"The most direct way to encourage cooperation is to make the interactions more durable. For
example, a wedding is a public act designed to celebrate and promote the durability of a
relationship... A good way to increase the frequency of interactions between two given individuals
is to keep others away. For example, when birds establish a territory... This is one reason why
cooperation emerges more readily in small towns than in large cities" (pp. 129–130). This isn't a
third *case* so much as Axelrod's own bridge from the two cases to the "engineering" half of the
brief's thesis ("that expectation can be engineered") — I'd recommend using it as connective tissue
rather than a third full case, since the chapter is already carrying two well-developed narratives
at a 4,500-word budget. If a third full illustrative case is wanted anyway, this session did not
independently research one beyond Axelrod's text (e.g., a repeated-game business/reputation case
from later literature); flag as `[PENDING: third-case-research]` in `Context/OPEN_QUESTIONS.md` if
the Drafter decides they need it — my recommendation is that they won't.
