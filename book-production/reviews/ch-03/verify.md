# Ch-3 Verification — draft-v3.md

Verifier pass, independent re-check against `Files/ostrom_1990.pdf` (primary), not the Researcher's
packet. Offset re-derived at a control point before use: PDF page (1-indexed) − 14 = printed page,
confirmed at printed p.1 (PDF idx 14) and printed p.71 (PDF idx 84), both showing the correct printed
folio number and matching text. Table 5.2 (p.180) was additionally confirmed by rendering the page to
a 400dpi image and reading the grid visually, not just via `pdftotext`-style extraction, because OCR
noise on tabular data is exactly where linear text extraction is least trustworthy.

**Web-tool caveat, logged up front:** this session's WebSearch allowance was already exhausted (200/200)
and WebFetch hit its session cap before any live check could run. The four web-sourced claims the brief
asked me to re-verify via web (1321 Jaume II charter, 1960 millennial celebration, UNESCO 2009 listing
exact title/date, "noon"/"smock" current-practice details) could **not** be independently re-fetched this
session. They are marked NOTE below, not PASS — they still rest on the Researcher's own web pass, which
the task instructions told me not to trust blindly. Recommend a follow-up Verifier pass once tools reset.

| # | Item | Verdict | Source |
|---|---|---|---|
| 1 | Thursday noon, Apostles' Gate/Door | NOTE | Ostrom p.71 says "Thursday mornings," "Apostles' Door" (confirmed in PDF). "Noon"/"Gate" rest on the packet's web pass, not independently re-fetched this session (tool budget exhausted). Already authorized as binding by Gate 1 (decisions.md) — not blocking, but not independently re-confirmed either. |
| 2 | Eight syndics, present-day | PASS | Consistent with Ostrom's own "eight major canals" (p.71) and the Gate‑1‑authorized modern figure; chapter never contradicts this with a stray "seven" for canals. |
| 3 | Black smocks, "dignity of a magistrate's" | NOTE | Real per packet's web pass (Tribunal's own site); not independently re-fetched this session. |
| 4 | Oral proceedings / recorded judgments, Ostrom p.72 formulation | PASS-WITH-NOTE | Confirmed verbatim, PDF p.72 (idx 85): "The final decisions of the court are recorded, but not the proceedings." Draft's "the decisions themselves are written down, and always have been" slightly overclaims antiquity — the earliest *surviving* judgment record the packet's web pass found is 19th-century; Ostrom's sentence describes an enduring practice but doesn't date its start. Minor; consider "and have been for as long as anyone can document" instead of "always." |
| 5 | 1321 Jaume II charter | NOTE — UNVERIFIED THIS SESSION | Not in Ostrom's primary text at all (confirmed absent from pp.69–81, read in full). Rests entirely on the Researcher's web pass. Could not be independently re-fetched (WebSearch/WebFetch both exhausted). Flag for a dedicated re-verification pass before print. |
| 6 | 1435 articles (84 irrigators, monastery of St. Francis) | PASS | Confirmed verbatim, PDF p.69 (idx 82): "On May 29, 1435... 84 irrigators served by the Benàcher and Faitanar canals in Valencia gathered at the monastery of St. Francis..." Exact match, including "at least 550 years... probably close to 1,000 years" hedge language, which the draft correctly preserves as a hedge rather than a flat claim. |
| 7 | 1960 millennial celebration | NOTE — UNVERIFIED THIS SESSION | Outside Ostrom (published 1990, referring to a 1960 civic event, but not mentioned in her book). Rests on the packet's web pass only. Not independently re-fetched. |
| 8 | UNESCO 2009 listing | NOTE — UNVERIFIED THIS SESSION | Outside Ostrom. Rests on the packet's web pass only. Not independently re-fetched, though the 2009/joint-with-Murcia claim is consistent with general background knowledge at moderate-to-high confidence. |
| 9 | **Seven/eight principle count (ORCHESTRATOR FLAG)** | **FAIL** | See full writeup below. Table 3.1 (actually printed p.90, not p.89 as the packet cites — verified directly) lists all eight principles; "eight working parts in her own catalog" (line 31) is accurate. But "two of her seven working principles" (Mawelle scorecard, line 69) is wrong on two counts — see below. |
| 10 | "Neither the state nor the market" quote | PASS | Confirmed verbatim, PDF p.1 (idx 14). Exact match, word for word. |
| 11 | Glick's "a few pennies" quote | PASS | Confirmed verbatim, PDF p.75 (idx 88): "were very low (a few pennies at the most) and also variable, depending on the gravity of the offense..." (Glick 1970, p.56, quoted by Ostrom). Draft's attribution to Glick directly is correct — Ostrom is quoting him. |
| 12 | Castellón figures (441/499, two-thirds) | PASS | Confirmed verbatim, PDF p.74 (idx 87): "In 1443 there were 441 fines assessed; in 1486 there were 499 fines." Two-thirds/one-third syndic/accuser split confirmed p.75. All three draft occurrences (main mention, the anchor, and the "eighteen times" fractious-farmer beat) correctly attribute to Castellón, never to Valencia's own records. |
| 13 | 1933 cap of 32 | PASS | PDF p.153 (idx 166): "Thirty-two nets were registered in 1933." |
| 14 | 71 nets mid-1940s | PASS | PDF p.153: "By 1945, 71 nets were in operation." |
| 15 | Beach supports 20–30 | PASS | PDF p.150 (idx 163): "If the Mawelle fishers owned only 20 to 30 nets, they could make optimal use of most of their nets." |
| 16 | Petitions 1940/1942/1945 fail, 1946 succeeds | PASS | PDF p.154 (idx 167): petitions "in 1940, 1942, and 1945," accepted in 1946, capped at "the 77 nets then registered." |
| 17 | **"Enforcement lapsed... the same arithmetic... kept building, quietly, for most of two more decades"** | **FAIL** | See writeup below — this reverses the documented rate of net-adding. |
| 18 | 84 by 1964 | PASS | Consistent with PDF p.154–155: 77 (1946) + 7 nets added over the next two decades = 84, and Mahattea's entry is dated 1964. |
| 19 | Brawl in 1966, boats capsized | PASS-WITH-NOTE | PDF p.155 (idx 168): "The boat carrying net 1 overturned" — **singular**. Draft's "Boats capsized" (plural) overstates. Minor fix: "A boat capsized." |
| 20 | "Three jeeps of riot police" | PASS-WITH-NOTE | Ostrom says "three jeep-loads of armed police... prevented a riot" (p.155) — not literally "riot police." Minor, defensible compression, but "armed police" is the precise term. |
| 21 | Frozen at 108 | PASS | PDF p.155: "The national government then issued regulations freezing the number of nets at 108." |
| 22 | Fish prices quadrupling 1938–41 | PASS | PDF p.153: "Prices for fish increased fourfold between 1938 and 1941." |
| 23 | Road/ice factory | PASS | PDF p.153: "the construction of a new road linking Mawelle to marketing centers, the construction of an ice factory nearby..." |
| 24 | **Mahattea's sequence — "went around the local official who'd already turned him down, straight to his own MP"** | **FAIL** | See writeup below — reverses Ostrom's documented order of events. |
| 25 | Paul Alexander as source anthropologist | PASS | PDF p.149 (idx 162): "the fishing village of Mawelle, as described by Paul Alexander (1977, 1982)." Two years in-village, madelia name, three murders/seventeen assaults — all confirmed pp.149–152. |
| 26 | "Two of her [seven] principles" per Table 5.2 | **FAIL** | Same finding as #9 — see writeup below. |
| 27 | Margaret Levi / "quasi-voluntary compliance" attribution | PASS | Confirmed verbatim, PDF p.94 (idx 107): "...the term 'quasi-voluntary compliance' can be useful, as applied by Margaret Levi (1988a, ch. 3)..." |
| 28 | "First woman to win the Nobel in economics, 2009" | PASS (background knowledge; not independently re-fetched live this session) | Well-established fact (Ostrom shared the 2009 Sveriges Riksbank Prize with Oliver Williamson and was the first woman to receive it). Also confirms decisions.md's Gate 4 flag is resolved: the riskier "only political scientist ever to win a Nobel" claim is **not** present in draft-v3 — the safe formulation was used. |
| 29 | Stag hunt characterization (assurance game, two equilibria) | PASS | Standard, correct game-theory description; no source-check issue. |
| 30 | Swiss meadows/Filipino canals/California groundwater as other cases | PASS | Confirmed via Table 5.2 (p.180): Törbel (Switzerland), Bacarra-Vintar (Philippines), Raymond/West/Central basins (Southern California) are all genuine Ostrom cases. Draft doesn't cite specific pages for these, so no further check needed. |
| 31 | **Guards "elected... could vote them out at the next gathering"** | **FAIL** | See writeup below. |
| 32 | Boundary principle (regadiu/secano/extremales) + "closing the boundary isn't sufficient... but necessary" | PASS | Confirmed verbatim, PDF p.71 and p.105 (idx 118 — table language continues past the p.90 table statement): "Making this attribute one of seven, rather than a unique attribute, puts its importance in a more realistic perspective. Simply closing the boundaries is not enough." |
| 33 | Nested-enterprises / "doesn't scale" answer (p.101–102) | PASS | Confirmed verbatim: "irrigators are organized on the basis of three or four nested levels... Establishing rules at one level, without rules at the other levels, will produce an incomplete system that may not endure over the long run." |

---

## Full writeup — the four FAILs

### FAIL 1 (the ORCHESTRATOR FLAG, items #9/#26): "eight working parts" vs. "two of her seven working principles"

**"Eight working parts in her own catalog" (line 31) is correct.** Table 3.1 (printed p.90 — the packet's
own evidence.md cites this as p.89; that citation is off by one page, confirmed directly) lists all eight
design principles, and Ostrom's own lead-in sentence (also p.90) frames it as "a set of seven design
principles that characterize all of these robust CPR institutions, plus an eighth principle used in the
larger, more complex cases." Both framings — "eight total" and "seven-plus-an-eighth" — are hers.

**"Two of her seven working principles" (line 69, the Mawelle scorecard) is wrong, on two counts,**
confirmed by rendering Table 5.2 (printed p.180) as a 400dpi image and reading the grid directly rather
than trusting linear OCR text (table extraction is exactly where that goes wrong):

1. **The denominator is wrong.** Ostrom's Table 5.2 scores Mawelle against all **eight** columns,
   including "Nested units" — and Mawelle's entry there is **"no,"** not "NR" (not relevant). Compare
   Törbel and the Japanese mountain villages, whose "Nested units" cells are explicitly marked "NR" —
   those are the cases where nesting is excluded from scoring. Mawelle's is actively scored and marked a
   failure. So "seven" — treating nesting as excluded for a non-nested village — is not what Ostrom's own
   table does for this specific case.
2. **The count is wrong even before that.** Ostrom's own prose (p.179) says: "two characterized the
   Mawelle fishery after 1938... (congruent rules and monitoring)." But her own Table 5.2 row for
   Mawelle reads: Clear boundaries=no, Congruent rules=**yes**, Collective-choice arenas=no,
   Monitoring=**yes**, Graduated sanctions=**yes**, Conflict-resolution=no, Recognized rights to
   organize=no, Nested units=no → **failure**. That's three "yes" marks (congruent rules, monitoring,
   *and* graduated sanctions), not two — her own table contradicts her own summary sentence. This is a
   genuine inconsistency inside Ostrom's primary text, not an extraction artifact (confirmed visually at
   400dpi) and not something the chapter is responsible for silently reconciling — but it also means
   "seven" isn't a defensible number to have inherited from either version of her own account.

**Exact fix:** in line 69, change "two of her seven working principles" to **"two of her eight design
principles"** — this preserves the "two" figure, which matches Ostrom's own explicit diagnostic sentence
(the one a "by Ostrom's own scorecard" claim should be citing), and fixes the denominator to the number
her own table actually uses for Mawelle. If the Showrunner wants full precision rather than inheriting
Ostrom's own prose/table mismatch silently, an endnote can note that Table 5.2 itself marks a third
principle (graduated sanctions) "yes" for Mawelle — three, not two — which would make the village's
near-miss even more sympathetic than the current sentence states, not less.

### FAIL 2 (item #17): "enforcement lapsed... the same arithmetic... kept building, quietly, for most of two more decades"

Ostrom's text (p.153–154) doesn't support this. The 1946 petition's enforcement "substantially slowed,
but did not completely stop" the growth: only **seven** new nets were added in the two decades following
1946 (77 → 84 by 1964), compared with **39** nets added in the roughly twelve years before it (32 → 71
by 1945). That's close to an eight-fold slowdown in the rate of net-adding, not "the same arithmetic...
kept building." The 1946 enforcement mostly held — imperfectly, via occasional bribery ("entrepreneurs
who offered sufficient inducements to government authorities were able to add a new net from time to
time") — until Mahattea broke it decisively in 1964–66.

**Exact fix:** replace "Then that lapsed too, and the same arithmetic that built the first thirty-nine
extra nets kept building, quietly, for most of two more decades" with something like: "Enforcement never
fully lapsed — it just got porous. Only seven new nets slipped through in the next two decades, against
thirty-nine in the twelve years before 1946. The cap was mostly holding, badly bruised but still there,
right up until Mahattea found the one gap it couldn't close." This is actually a *stronger* point for the
chapter's own argument (the state layer worked reasonably well for eighteen years; political capture,
not ordinary decay, is what actually broke it) than the current sentence, which undersells it.

### FAIL 3 (item #24): Mahattea's sequencing

Draft: "he went around the local official who'd already turned him down, straight to his own Member of
Parliament." Ostrom's text (p.154) has the order reversed: Mahattea, unable to buy shares, **went to the
MP first** ("Finding it difficult to buy shares in current nets, Mahattea approached the local member of
parliament"). The MP then asked the district revenue officer to consider the proposal, and *that* officer
"refused at first, arguing there were too many nets" — before eventually relenting after conflict in the
village. There is no local-official refusal preceding Mahattea's approach to the MP; the local official
only enters the story after the MP brings him in.

**Exact fix:** replace "he went around the local official who'd already turned him down, straight to his
own Member of Parliament, and got permission to register new nets anyway" with something like: "he went
straight to his own Member of Parliament, who leaned on the district revenue officer to approve it. The
officer balked at first — too many nets already — but caved after the village erupted in conflict." This
is actually the sharper version for the chapter's thesis: Mahattea didn't escalate after being properly
refused, he skipped the normal channel entirely and imported outside political leverage from the start.

### FAIL 4 (item #31): guards "elected... could vote them out"

Draft (line 53): "the same farmers who paid the guards also elected them, watched them, and could vote
them out at the next gathering." Ostrom's text (p.72) is explicit that the **syndic** is what the hereters
elect ("the farmers... meet every second or third year to elect the syndic and several other officials
for their canal"), while the **ditch-riders and guards are appointed by the syndic**: "The syndic usually
has a small staff of ditch-riders and guards whom he appoints to help him carry out these assignments."
Guards are described (p.96) as "accountable to the appropriators" in the sense that they "can be fired
easily if discovered slacking off," and the syndic himself can "lose respect — and his job" (p.74) — but
nowhere does Ostrom describe a direct farmer election, or a "vote them out at the next gathering"
mechanism, for the guards specifically. The draft conflates the syndic's election with the guards'
accountability.

**Exact fix:** replace "the same farmers who paid the guards also elected them, watched them, and could
vote them out at the next gathering" with something like: "the same farmers who paid the guards also
elected the syndic who appointed them, watched the guards work, and could get them fired for slacking."
This keeps the design-principle-4 point (monitors are accountable to appropriators, not a captured
bureaucracy) fully intact — it's still true and still Ostrom's own point — while matching the actual
appointment chain rather than inventing a guard election.

---

## Minor notes bundled for completeness (not blocking)

- Table 3.1's exact wording is on printed **p.90**, not p.89 as `research/ch-03/evidence.md` states
  throughout. Same off-by-one recurs for the "particularly fractious individual" quote and the Oliver
  1980 quote, both of which are actually on printed **p.76**, not p.88/p.90 as the packet variously
  states. None of this reached the manuscript's prose (no page numbers are quoted in-text), but if
  endnotes cite Ostrom page numbers directly, they should be re-derived from this session's findings, not
  copied from the packet.
- "Never once, in living memory, closed its doors" (line 3) is an unsourced superlative — vivid but not
  attributable to Ostrom or to anything in the packet's web pass. Low-stakes scene-setting; flag only if
  the chapter wants zero unverifiable absolutes in the cold open.
- "The historian who dug up those books, an American named Thomas Glick" — Glick's American nationality
  is not stated in Ostrom's text and was not independently re-verified this session; commonly known
  (Harvard-trained historian) but technically another web-tool-exhaustion gap.
