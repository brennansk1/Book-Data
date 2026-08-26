# Referee — Prologue draft-v2.md

Role per `spec/PRODUCTION_BIBLE.md` §2.7: hostile professional reviewer, instructed to be
unfair. The chapter must answer each objection below, concede it in text, or the Showrunner
overrules with a logged reason.

---

## 1. The thesis overclaims on the supply side — "nobody chose this" is false of the one
fact the whole piece rests on (STRONGEST OBJECTION)

> "A program can only train so many residents; seventy applications from one student don't
> create a seventy-first slot to fill." (¶9)
>
> "Nobody in this is doing anything unreasonable." (¶15)
>
> "how do you hold anyone responsible for a result that nobody chose and everybody produced
> together?" (¶48)

The number of funded residency positions is not a natural constant like clinic-hours or a
hospital's physical bed count. It is a number Congress set. The Balanced Budget Act of 1997
capped Medicare-funded GME positions at each hospital's 1996 resident count — a deliberate
policy choice, based on 1990s workforce projections (COGME) that anticipated a physician
*surplus* and turned out to be wrong — and that cap sat essentially frozen for a quarter
century, loosened only slightly by a 1,000-slot phase-in beginning FY2023 (Consolidated
Appropriations Act, 2020). Confirmed independently: JAMA ("US Residency Training Before and
After the 1997 Balanced Budget Act"), the Commonwealth Fund's contemporaneous analysis of the
Act, AHA fact sheets, and Modern Healthcare's reporting on the 2020 unfreezing. Meanwhile
U.S. medical school enrollment was *deliberately expanded* starting the mid-2000s (AAMC's own
30%-by-2015 growth initiative) — precisely because of a projected physician shortage — with no
matching expansion on the residency-slot side. The applicant flood colliding with a fixed
number of "chairs" is not two mysterious multipolar forces meeting by accident. One side of
that equation (the chairs) is a specific, nameable, twenty-five-year-old policy failure, and
the people who could fix it (Congress, acting on its own agencies' bad projections and then
slow to correct them) are exactly the kind of actor "nobody chose this" is designed to write
out of the story.

This doesn't wreck the *demand*-side argument — the application arms race among Kudrna,
Sarah, and their cohort is genuinely a coordination trap, and no one applicant can unilaterally
opt out of it. That part holds. But the prologue folds a real emergent trap (demand-side
behavior) and an ordinary, chooseable policy failure (supply-side scarcity) into one seamless
"everyone behaved reasonably, no one is to blame" narrative, and a health-policy-literate
reader — which this book will attract, given how heavily it leans on AAMC/NRMP data — will
catch the seam immediately. As written, the text either doesn't know the single most commonly
cited structural cause of the residency crunch, or knows it and is declining to mention it
because it complicates the "no villain" frame the ending needs. Neither looks good in a book
whose thesis is epistemic honesty.

**Fix (not concede, not cut):** one sentence, in voice, conceding that the number of seats
itself is not a natural fact — that it's been frozen by federal funding policy since 1997 and
grows far slower than applicant volume. This doesn't require turning the prologue into a
policy essay. It requires the text to stop treating "a program can only train so many
residents" as self-evident and start treating it as the specific, correctable choice it is.
Keep the demand-side "nobody's unreasonable" argument — it's the strongest material in the
piece — but stop letting it borrow credibility from a supply-side claim it hasn't earned.

---

## 2. AAMC supplies every human-voice quote in the piece and has an undisclosed financial
stake in the behavior it's quoted lamenting

Kudrna's and Harrison's quotes both come from *AAMC News*, AAMC's own institutional
publication, reporting on AAMC's own reform effort. `research/prologue/evidence.md` flags
this directly: "an interested party (AAMC runs ERAS) writing about its own reform effort,
which is worth noting for tone." The draft never notes it. AAMC charges per-application fees
through ERAS — even under the current tiered structure ($11/application up to 30, $30/each
beyond), more applications still means more AAMC revenue at the margin. Harrison's line, which
evidence.md calls "the single best line in the packet," is delivered by an institution whose
parent organization profits, checkbox by checkbox, from the exact arms race it is quoted
regretting.

This does not make the quote false, and AAMC is not obviously the piece's hidden villain —
its interest is much smaller than, say, a rent-seeking monopolist's. But ¶15's "nobody in this
is doing anything unreasonable" surveys the applicant, the programs, and the dean, and quietly
skips the one party in the chain with a direct financial stake in application volume staying
high — which also happens to be the party supplying the piece's most quotable material. A
hostile reader will notice that the villain-search in the Christmas anecdote (¶33: "Not Sarah.
Not Harrison. Not the programs.") never even considers AAMC by name, despite AAMC being the
one actor whose incentives are not purely aligned with fixing the problem.

**Fix:** one clause. Something as light as noting that even AAMC — which collects a fee on
every one of those checkboxes — is on record hating the outcome, doesn't resolve the tension,
it makes it explicit and lets the "no single villain, and yet—" theme absorb it instead of
being blindsided by it later. Omitting it reads like it wasn't considered; naming it and
setting it aside reads like it was.

---

## 3. Numbers delivered at higher confidence than the evidence packet supports — the exact
failure mode §7.2 forbids

PRODUCTION_BIBLE §7.2: "Never state a contested empirical claim at high confidence... Where
the literature is genuinely divided, the text says so." STYLE_BIBLE Rule 9: "Modulate
confidence audibly... The prior draft stated a bare axiom and a contested labour-economics
literature at identical pitch." That is exactly what happens here:

> "Applications did come down, in some specialties by close to half; dermatology alone went
> from around seventy applications per applicant to about forty in two years." (¶40)

`evidence.md` rates these exact percentages **REPORTED-BUT-SINGLE-SOURCE**, explicitly: "the
specific percentages... need a direct primary-source pull before they're printed as numbers
rather than as 'the AAMC reports a meaningful decline.'" The draft prints them as numbers,
flat, no hedge — in the same declarative register as the Carmody et al. 70-applications figure
two paragraphs earlier, which *is* peer-reviewed and SOLID. Same problem with "Neurosurgery
applicants report nearly thirty research activities each" and "program directors ranked
research as the second most important factor" (¶42) — both rated
REPORTED-BUT-SINGLE-SOURCE in the packet, both delivered here with zero audible hedge.

`reviews/prologue/decisions.md` already routes the single-source AAMC/NRMP figures to the
Verifier before Gate 4 — so the fact-checking is tracked. But confidence-modulation is a
drafting problem, not a fact-checking one: even if the Verifier confirms every digit, the
prose still owes the reader a difference in *pitch* between "peer-reviewed, decade-long trend"
and "one search-aggregated news estimate," per the book's own stated rule. Right now there
isn't one.

**Fix:** a light hedge clause on the reform-numbers sentence and the "nearly thirty research
activities" sentence — doesn't need to break voice, just needs to exist. Small lift, and it's
a rule the book has already committed to in writing.

---

## 4. The confession is a little too convenient — reads as performing honesty in the exact
place the piece should be practicing it

The `<!-- ANCHOR -->` passage (¶33-35) stages the narrator's arc — irritation, shame,
week-long search, coming up empty — as a live dramatization of the prologue's abstract thesis
(everyone's first instinct is to hunt for a villain; there isn't one). That's a legitimate
device. But it closes on a claim the text doesn't back up: "I came up empty, and not because I
didn't look hard enough." A real week of looking, on this exact question, is one search query
away from Findings 1 and 2 above — both are among the first things a health-policy journalist
would surface on residency-application inflation. Their absence from a search the narrator
swears was thorough is the tell. This is the difference between *performing* honesty (telling
the reader "I looked hard") and *practicing* it (showing the reader what a hard look actually
turned up, including the parts that complicate the ending). Compounding this: per
`reviews/prologue/decisions.md`, the "niece Sarah" thread anchoring this entire passage is a
flagged, unresolved fabrication ("NOT true biography... Showrunner must confirm a true
equivalent... PDF ships watermarked DRAFT until resolved"). That flag is already logged and is
not this review's discovery, but it bears directly on this piece's central honesty claim and
is still open as of this draft, so it belongs on this record too.

**Fix, pick one:** (a) let the narrator's search actually surface the GME-cap and AAMC-fee
findings above and explain, on the page, why they don't change the verdict — a stronger,
harder-to-refute version of the same ending; or (b) soften "not because I didn't look hard
enough" to a claim the text can support. Separately, and not new to this review: resolve the
Sarah fabrication per the existing decisions.md flag before this leaves DRAFT status.

---

## 5. Note, not a new finding — "who do you forgive?"

`reviews/prologue/cold-read.md` already caught that "forgive" presupposes a wrong to pardon,
which sits oddly against "nobody is being unreasonable," and `decisions.md` records that this
was considered and deliberately kept as productive friction. I won't relitigate a decision
already made on the record. But Finding 1 sharpens the stakes: if the supply side has an
identifiable, in-principle-blameable actor (a 1997 Congress acting on bad projections, and
every subsequent Congress slow to fix it), then "who do you forgive" isn't purely open-ended —
it has at least a partial real-world answer the book is choosing not to hand the reader yet.
That's fine for a prologue provided the book actually returns to policy-level actors later and
this isn't the only place that thread gets pulled. Flag for the Showrunner to confirm later
chapters pick this up — otherwise the ending question will read, in retrospect, as having
quietly assumed its own conclusion.

---

## What holds

The demand-side arms-race argument itself is sound and well-evidenced: the Carmody et al.
figures are used at the confidence they support, the "one program's number, not a national
one" caveat on the $3,736 figure is preserved correctly (evidence.md flagged exactly this
risk), Trujillo/delivery-app material was correctly left out per the Case 2 framing risk, and
the "Ya Siam" do-not-use quote does not appear anywhere in the draft. The core mechanism —
individually rational actors producing a collectively hated, individually inescapable result —
is real, named accurately, and not oversold as more novel than it is (¶46 resists the urge to
claim the shape doesn't have existing names). The objections above are about where the piece's
"no one is to blame" frame reaches further than the facts in its own evidence packet actually
go, not about whether the core case is real.
