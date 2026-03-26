# Position Registry — The Swappable Stance System

This is the **living inventory** of every substantive position the moral system takes. Each position is versioned, rated, and linked to the chapter(s) that argue for it. When a better position is found, the old one is deprecated and the new one is installed — with a full audit trail.

**This file is what makes the system self-correcting, not just self-documenting.**

---

## How It Works

1. Every claim the system makes that could be otherwise gets registered here
2. Each position has a **confidence rating** (how sure we are) and **vulnerability rating** (how strong the best objection is)
3. When research or debate reveals a superior position, we **swap it in**:
   - Log the swap in `Context/DECISIONS.md`
   - Update this registry
   - Revise the relevant chapter(s)
   - Update `BOOK_BIBLE.md`
4. Deprecated positions are moved to the archive at the bottom — they're not deleted, because understanding *why* we changed is part of the system's strength

## Rating Scales

**Confidence** (how well-supported):
- `AXIOM` — Foundational assumption; not proven but explicitly chosen and defended
- `STRONG` — Multiple independent arguments support this; survives steel-manned objections
- `MODERATE` — Good arguments exist but significant objections remain partially answered
- `PROVISIONAL` — Best available position; actively looking for something better
- `EXPLORATORY` — Early-stage thinking; included for completeness but may change substantially

**Vulnerability** (strength of best known objection):
- `LOW` — No serious objection has survived analysis
- `MEDIUM` — Known objections exist; current rebuttals are adequate but not airtight
- `HIGH` — A serious objection exists that we haven't fully answered yet
- `CRITICAL` — An objection that could break this position; resolution is urgent

---

## I. Metaphysical Positions

### POS-M01: Constructivist Realism
**Version:** 1.0 | **Confidence:** AXIOM | **Vulnerability:** MEDIUM
**Chapter(s):** CH-01
**Position:** Moral values are constructed by conscious agents but constrained by objective features of reality (biology, game theory, physics). Neither invented wholesale nor discovered as mind-independent facts.
**Best Objection:** Collapses into either realism or constructivism under pressure — what exactly does "constrained by reality" add beyond saying "some moral systems work better than others"?
**Current Rebuttal:** The constraint is empirical and testable. Bridge-building is also "constructed" but constrained by physics — you can't build any bridge you want. Same logic applies to moral systems.

### POS-M02: Valence Realism
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** MEDIUM
**Chapter(s):** CH-03
**Position:** Suffering and joy are objective physical states of conscious systems. They provide the factual grounding that bridges the is-ought gap. The minimal axiom — "conscious suffering matters" — is where the system's normativity enters.
**Best Objection:** Still requires at least one normative axiom ("suffering matters"), which means the system isn't purely derived from facts.
**Current Rebuttal:** Every system requires at least one axiom. Ours is the most minimal and hardest to deny — denying it is performatively incoherent (you'd have to not care about your own suffering to sincerely assert it).

### POS-M03: The Separation of Origins
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** LOW
**Chapter(s):** CH-04
**Position:** The evolutionary origin of a moral intuition is irrelevant to its validity. We evaluate inherited instincts by our chosen criteria, keeping what serves flourishing and discarding what doesn't.
**Best Objection:** How do you evaluate intuitions without relying on other intuitions? Risk of infinite regress.
**Current Rebuttal:** The regress terminates at the valence axiom (POS-M02) and epistemic duty (POS-E01). These are chosen, not derived — and explicitly acknowledged as such.

---

## II. Epistemic Positions

### POS-E01: Epistemic Duty
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** LOW
**Chapter(s):** CH-02
**Position:** Truth-seeking is a moral obligation, not merely an intellectual preference. You cannot act morally with a false model of reality. Epistemic rationality is therefore a prerequisite for ethical rationality.
**Best Objection:** Some truths cause harm (e.g., a depressed person learning they're statistically likely to remain depressed). Is truth-seeking always a duty?
**Current Rebuttal:** The duty is to *seek* truth, not to *weaponize* it. Communication of truth is governed by the moral architecture (Mode A/B). The duty is against self-deception, not against tact.

### POS-E02: Bayesian Updating as Epistemic Method
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** LOW
**Chapter(s):** CH-02
**Position:** Beliefs should be held as probability distributions and updated on evidence. This is the formal implementation of epistemic duty.
**Best Objection:** Bayesianism requires prior probabilities, which can be subjective and biased.
**Current Rebuttal:** Acknowledged — but Bayesian reasoning is self-correcting over time. Bad priors wash out with sufficient evidence. No alternative method has this convergence property.

---

## III. Ethical Architecture Positions

### POS-A01: Dual-Process Decision Making
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** HIGH
**Chapter(s):** CH-07, CH-08
**Position:** Default to pre-computed heuristics (rules/virtues) for 99% of decisions. Switch to explicit consequentialist calculation only when rule-following would cause irreversible catastrophic harm AND you can justify the override to a skeptical third party.
**Best Objection:** The threshold for switching is vague and gameable. Every consequentialist thinks their case is the special exception.
**Current Rebuttal:** The "skeptical third party" test is the anti-gaming mechanism. If you cannot articulate why this specific case warrants override to someone who disagrees, you haven't met the threshold. [NEEDS STRENGTHENING]

### POS-A02: Morality as Coordination Technology
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** MEDIUM
**Chapter(s):** CH-05, CH-06
**Position:** Morality exists to solve coordination problems. "Good" is the successful implementation of mechanisms that escape bad Nash equilibria. This is not a metaphor — it's the literal function.
**Best Objection:** Reduces morality to instrumental rationality. What about moral duties that don't serve coordination (e.g., duties to the dead, aesthetic duties, duties of gratitude)?
**Current Rebuttal:** [NEEDS DEVELOPMENT] — These may be Chesterton Fences (rules that look non-instrumental but actually serve coordination in non-obvious ways), or they may be genuinely non-coordination moral facts we need to account for.

---

## IV. Political Positions

### POS-P01: Error-Correction Primacy
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** LOW
**Chapter(s):** CH-11
**Position:** The best political system is not the one that produces the best outcomes directly, but the one that corrects errors fastest. Optimize for feedback loops, not for specific policies.
**Best Objection:** Some errors are irreversible (existential risks). Error-correction is too slow for catastrophic threats.
**Current Rebuttal:** This is why existential risk gets special treatment (CH-20). Error-correction is the default; existential risk is the exception that warrants more direct intervention.

### POS-P02: Institutional Mechanism Design over Ideology
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** MEDIUM
**Chapter(s):** CH-12
**Position:** Political problems are engineering problems. Design institutions to align individual incentives with collective welfare rather than relying on the virtue of leaders or citizens.
**Best Objection:** "Engineering" framing ignores power dynamics, historical injustice, and the fact that mechanism designers have their own interests.
**Current Rebuttal:** Mechanism design explicitly accounts for self-interest — that's the whole point. Historical injustice is a real input to the design problem, not something the framework ignores. But this needs more development.

### POS-P03: Strong Free Speech Default
**Version:** 1.0 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-14
**Position:** Free expression is the epistemic immune system of a society. Censorship destroys the feedback loop. The default should be maximal speech protection with narrow, well-defined exceptions.
**Best Objection:** Unregulated speech can itself destroy epistemic commons (disinformation, coordinated harassment, stochastic terrorism). The "marketplace of ideas" may be a market failure.
**Current Rebuttal:** [NEEDS DEVELOPMENT] — Need to distinguish between speech and coordination-for-harm. The system's own game theory may require more nuance here than the framework suggests.

### POS-P04: Constrained Democracy
**Version:** 1.0 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-13
**Position:** Democracy is the best available error-correction mechanism but must be constrained by constitutional rights, separation of powers, and federalism to prevent tyranny of the majority and rational irrationality of voters.
**Best Objection:** Constitutional constraints are anti-democratic and often serve entrenched interests rather than protecting genuine rights.
**Current Rebuttal:** The constraint is *on* the democratic process, not *against* it — like guardrails on a highway. The question is which constraints are legitimate, which requires a theory of rights (CH-15).

### POS-P05: Subsidiarity
**Version:** 1.0 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-13
**Position:** Decisions should be made at the lowest level of governance competent to handle them. Local knowledge (metis) is destroyed by centralization.
**Best Objection:** Some problems (climate, pandemics, AI) are inherently global and cannot be solved locally. Subsidiarity can also mean local tyranny.
**Current Rebuttal:** Subsidiarity is a default, not an absolute. Problems with genuine externalities that cross jurisdictional boundaries escalate upward. The framework handles this via internalization of externalities.

### POS-P06: Justice as Restitution + Deterrence
**Version:** 1.0 | **Confidence:** PROVISIONAL | **Vulnerability:** HIGH
**Chapter(s):** CH-16
**Position:** The purpose of the justice system is (1) to make victims whole (restitution), (2) to deter future offenses (deterrence), and (3) to incapacitate those who cannot be deterred. Retribution for its own sake is a vestigial instinct to be overcome.
**Best Objection:** Purely consequentialist justice can justify punishing the innocent if it deters effectively. Also, many people have deep moral intuitions about desert that may be load-bearing.
**Current Rebuttal:** [NEEDS SIGNIFICANT DEVELOPMENT] — This is one of the system's weakest areas. Need to either defend dropping retribution or find a way to reconstruct "desert" within the framework.

### POS-P07: Rights as Coordination Equilibria
**Version:** 1.0 | **Confidence:** PROVISIONAL | **Vulnerability:** HIGH
**Chapter(s):** CH-15
**Position:** Rights are not natural or God-given. They are Schelling points — coordination equilibria that rational agents converge on because respecting them produces better outcomes than violating them.
**Best Objection:** If rights are merely instrumental, they can be overridden whenever the calculus changes. This is exactly what rights are supposed to prevent.
**Current Rebuttal:** [NEEDS SIGNIFICANT DEVELOPMENT] — The Mode A/B architecture may help here (rights are Mode A defaults that require extreme justification to override), but this needs rigorous treatment.

---

## V. Economic Positions

### POS-EC01: Markets as Information Systems
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** LOW
**Chapter(s):** CH-17
**Position:** Markets are primarily information-processing systems (Hayek). Prices aggregate dispersed knowledge that no central planner could collect. Market failure is real but is the exception, not the rule.
**Best Objection:** Markets also transmit and amplify power asymmetries, not just information. The "information" framing obscures distributional questions.
**Current Rebuttal:** Power asymmetries are a real market failure to be addressed via mechanism design, not a refutation of the informational function.

### POS-EC02: Pigovian Correction of Externalities
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** MEDIUM
**Chapter(s):** CH-18
**Position:** When private costs diverge from social costs (externalities), the correct intervention is to realign them via taxes/subsidies (Pigovian), not to ban or mandate. Make the selfish move identical to the social move.
**Best Objection:** Pigovian taxes require accurate measurement of externalities, which is often impossible. Also, they can be regressive.
**Current Rebuttal:** Measurement difficulty is an engineering problem, not a conceptual one. Regressivity can be addressed via revenue recycling (carbon dividend, etc.).

### POS-EC03: Safety Net as Insurance, Not Redistribution
**Version:** 1.0 | **Confidence:** PROVISIONAL | **Vulnerability:** HIGH
**Chapter(s):** CH-19
**Position:** The welfare state is best justified not as redistribution for its own sake, but as social insurance — rational agents behind a veil of uncertainty would buy insurance against catastrophic outcomes (disability, unemployment, bad luck).
**Best Objection:** The insurance framing excludes people who are *predictably* disadvantaged (born into poverty, systemic discrimination). Insurance is for *uncertain* risks, not *known* inequalities.
**Current Rebuttal:** [NEEDS SIGNIFICANT DEVELOPMENT] — May need to expand beyond pure insurance framing to include capability-based or floor-based arguments. This is a key area where the framework may need to go beyond its libertarian-leaning starting point.

### POS-EC04: Prediction Markets as Epistemic Infrastructure
**Version:** 1.0 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-18
**Position:** Prediction markets are the highest-fidelity mechanism for aggregating beliefs about future states. They should be legalized and expanded as a tool for policy evaluation.
**Best Objection:** Thin markets are easily manipulated. Prediction markets can also create perverse incentives (betting on assassinations, terrorist attacks).
**Current Rebuttal:** Manipulation risk decreases with market depth. Perverse incentive problems are solvable through market design (conditional markets, exclusion of beneficiaries).

### POS-EC05: Fiscal Conservatism with Social Investment
**Version:** 1.0 | **Confidence:** PROVISIONAL | **Vulnerability:** HIGH
**Chapter(s):** CH-19, CH-20
**Position:** Government spending should be constrained by cost-benefit analysis with strong presumption against debt financing. However, investments with demonstrable long-term returns (education, infrastructure, R&D, public health) clear this bar.
**Best Objection:** "Cost-benefit analysis" can be rigged to justify anything depending on discount rates, how you value non-market goods, and whose costs/benefits count.
**Current Rebuttal:** [NEEDS DEVELOPMENT] — Need to address the methodology of public cost-benefit analysis honestly, including its known failure modes.

---

## VI. Frontier Positions

### POS-F01: Existential Risk as Moral Priority
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** MEDIUM
**Chapter(s):** CH-20
**Position:** Preventing human extinction (and other existential catastrophes) is a moral priority that outweighs most other concerns, because the expected value of the future is astronomically large.
**Best Objection:** "Astronomical value of the future" arguments can be used to justify almost anything (torturing one person to save trillions of future people). Also, heavy discounting of future value undermines the argument.
**Current Rebuttal:** The Mode A/B architecture constrains this — you cannot violate fundamental rights even for existential risk reduction, except under extreme and specifically defined conditions. The discounting objection needs engagement.

### POS-F02: Cautious AI Development
**Version:** 1.0 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-21
**Position:** AI development is the most important coordination problem humanity faces. The rational stance is cautious development with strong alignment research, not acceleration or moratorium.
**Best Objection:** "Cautious development" is vague and may be unstable — competitive pressures (Moloch) push toward acceleration regardless of what any individual actor wants.
**Current Rebuttal:** This is precisely the Moloch problem the system is designed to solve. The question is what coordination mechanisms can actually work. [NEEDS DEVELOPMENT]

### POS-F03: Consciousness-Based Moral Circle
**Version:** 1.0 | **Confidence:** PROVISIONAL | **Vulnerability:** HIGH
**Chapter(s):** CH-22
**Position:** Moral patienthood extends to all systems with conscious experience. This potentially includes some animals and could include future AIs. The boundary is consciousness, not species membership.
**Best Objection:** We have no reliable test for consciousness. Basing moral patienthood on an undetectable property is practically useless.
**Current Rebuttal:** [NEEDS SIGNIFICANT DEVELOPMENT] — Need to engage with the hard problem of consciousness and develop practical heuristics even under uncertainty.

---

## Archive — Deprecated Positions

*No positions deprecated yet. When a position is replaced, move it here with a note explaining what replaced it and why.*

<!-- TEMPLATE:
### [DEPRECATED] POS-XXX: [Name]
**Replaced By:** POS-YYY
**Date Deprecated:** YYYY-MM-DD
**Reason:** [Why the new position is superior]
-->
