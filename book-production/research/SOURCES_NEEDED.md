# Source Requests for the Showrunner

The Researcher/Verifier roles work from `Files/` first, then the open web. These are
the gaps where a real copy would materially raise chapter quality. Ranked.

## Tier 1 — blocking or near-blocking (a chapter leans on it; we have secondary access only)

| Work | Chapter | Why it's needed |
|---|---|---|
| Appiah, *The Honor Code* (2010) | Ch. 4 | The duel-collapse mechanism is the chapter's spine, currently paraphrased from reviews and one excerpt. No direct quotation is safe without the book. |
| Grahek, *Feeling Pain and Being in Pain* (2007) | Ch. 5 | The asymbolia interpretation the chapter's engine runs on. We have Klein's rebuttal via a peer-reviewed paper but not Grahek's own text. |
| Sinhababu, *Humean Nature* (2017) | Ch. 5 | The phenomenal-introspection argument closest to the framework's own claim; only two phrases verified. |
| Kahane, "Pain, Dislike and Experience," *Utilitas* 21(3), 2009 | Ch. 5 | Confirmed **ally**, not just background — but the body is paywalled; we have the abstract only. |
| Binmore, *Natural Justice* (2005) | Ch. 6 | Named in the brief as the machinery behind the coordination derivation of impartiality. Thin secondary summary only. |
| Parfit, *On What Matters* vol. 1 (2011) | Ch. 6 | Same. (*Reasons and Persons* IS in Files/ and is in use.) |
| Blackburn, *Ruling Passions* or *Spreading the Word* | Ch. 7 | Tier 3 of the degradation structure is quasi-realism; characterized from the SEP entry, so no quotation is safe. |

## Tier 2 — would remove a standing "secondhand" disclosure

| Work | Chapter | Why |
|---|---|---|
| Ashworth, *Trench Warfare 1914–1918* (1980) | Ch. 2 | The frozen text discloses in-line that the account reaches us *through* Axelrod. A copy lets the chapter cite the historian directly. |
| Vaughan, *The Challenger Launch Decision* (1996) | Ch. 10 | Normalization of deviance is load-bearing in the flagship chapter; verified via secondary sources only. |
| Jackall, *Moral Mazes* (1988) | Ch. 10 | One quote in the frozen chapter, attributed by description rather than page. |
| Edwards & Ogilvie, Maghribi papers (2008–2012) | Ch. 4 | We know the critique only through Greif's own summary of it — a one-sided chain the packet flags. |
| Alexander, *Sri Lankan Fishermen* (1982) | Ch. 3 | Mawelle's numbers come via Ostrom; the recausalized passage would be firmer from the ethnography. |
| Boehm, *Hierarchy in the Forest* (1999) | Ch. 4 | Only the 1993 *Current Anthropology* paper is accessible; book claims are currently avoided. |

## Tier 3 — the voice seed corpus (VOICE §3 calls this the highest-leverage input in the pipeline)

`voice/seed/models/` holds an **interim** corpus (Haidt, Galef, Dawkins) standing in for
the six books the spec actually names. Supplying these lets the burstiness reference and
the register targets be rebuilt against the real thing:

- Sandel, *Justice* — case-first chapter openings
- Blackburn, *Being Good* — compression without condescension
- Glover, *Humanity* — moral weight via historical particularity
- Williams, *Ethics and the Limits of Philosophy* — conceding hard, staying persuasive
- Appiah, *The Honor Code* — narrative and argument braided (doubles as Tier 1)
- Nagel — sentence-level clarity on hard material

## Tier 4 — later chapters, not yet drafted

Frank, *Passions Within Reason* (Ch. 13) · Annas, *Intelligent Virtue* and Doris on
situationism (Ch. 11) · Held or Noddings on care ethics (Ch. 13). Already in `Files/`
and needing nothing: Sen, *Development as Freedom* (Ch. 17); Scott, *Seeing Like a
State* (Ch. 16); Ostrom (Ch. 3); Axelrod (Ch. 2); Singer, Parfit, Kant, Aristotle.

## Format notes

PDF or EPUB both work. Drop them in `Files/` with any filename — the Researcher greps
the directory. `Files/` is gitignored, so nothing copyrighted is published.
