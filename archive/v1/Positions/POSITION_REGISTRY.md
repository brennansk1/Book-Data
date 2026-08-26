# Position Registry — The Swappable Stance System

This is the **living inventory** of every substantive position the moral system takes. Each position is versioned, rated, and linked to the chapter(s) that argue for it. When a better position is found, the old one is deprecated and the new one is installed — with a full audit trail.

**This file is what makes the system self-correcting, not just self-documenting.**

---

## How It Works

1. Every claim the system makes that could be otherwise gets registered here
2. Each position has a **confidence rating** (how sure we are) and **vulnerability rating** (how strong the best objection is)
3. Each position now includes:
   - A **falsification condition**: what evidence or argument, if presented, would require revising or abandoning this position
   - A **last reviewed** date: when the position was last stress-tested against the best available objections
   - A **revision history**: major changes tracked by version number
4. When research or debate reveals a superior position, we **swap it in**:
   - Log the swap in `Context/DECISIONS.md`
   - Update this registry
   - Revise the relevant chapter(s)
   - Update `BOOK_BIBLE.md`
5. Deprecated positions are moved to the archive at the bottom — they're not deleted, because understanding *why* we changed is part of the system's strength

**The falsification conditions are the system's strongest claim to intellectual honesty.** Any position that cannot specify what would change it is not a position — it is a dogma. The Registry makes every position's conditions for revision explicit and public.

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
**Version:** 1.0 | **Confidence:** AXIOM | **Vulnerability:** MEDIUM | **Last Reviewed:** 2026-04-07
**Chapter(s):** CH-01
**Position:** Moral values are constructed by conscious agents but constrained by objective features of reality (biology, game theory, physics). Neither invented wholesale nor discovered as mind-independent facts.
**Best Objection:** Collapses into either realism or constructivism under pressure — what exactly does "constrained by reality" add beyond saying "some moral systems work better than others"?
**Current Rebuttal:** The constraint is empirical and testable. Bridge-building is also "constructed" but constrained by physics — you can't build any bridge you want. Same logic applies to moral systems.
**Falsification Condition:** Show that the "constrained by reality" claim adds no predictive or explanatory power beyond pure constructivism, OR show that moral facts are mind-independent in a way that makes the constructivist element unnecessary.
**Revision History:** v1.0 (2026-03-26) — initial formulation.

### POS-M02: Valence Realism
**Version:** 2.0 | **Confidence:** STRONG | **Vulnerability:** LOW
**Chapter(s):** CH-03
**Position:** Suffering and joy are objective physical states of conscious systems. They provide the factual grounding that bridges the is-ought gap. The minimal axiom — "conscious suffering matters" — is where the system's normativity enters.
**Best Objection:** Still requires at least one normative axiom ("suffering matters"), which means the system isn't purely derived from facts. Error theorists (Mackie, Joyce) can accept that humans *act* as if suffering matters while denying it is objectively normative.
**Current Rebuttal:** CH-03 now deploys a three-layered grounding strategy: (1) Reflective equilibrium — the axiom is the most stable node in the most coherent web of moral and empirical commitments; removing it causes the greatest loss of coherence across independent moral traditions, considered judgments, and functional requirements for stable cooperation. (2) Performative incoherence — the denial cannot be lived, though this is explicitly acknowledged as a pragmatic argument, not a logical proof. (3) Inference to best explanation — "suffering matters" is the best available explanation for universal harm-avoidance norms, the direction of moral progress, the causal efficacy of pain states, and the failure of all competing explanations to account for these facts. A critic must defeat all three layers simultaneously. Vulnerability downgraded from MEDIUM to LOW because the distributed justificatory burden eliminates the single-point-of-failure that the original one-argument defense had.
**Falsification Condition:** (a) Demonstrate a coherent moral web that excludes the valence axiom and is more stable than ours, OR (b) show that the convergence of independent moral traditions on harm-avoidance is explained by something other than the reality of valence, OR (c) demonstrate that something functionally analogous to suffering does not exist.
**Revision History:** v1.0 (2026-03-26) — initial formulation, single performative incoherence argument. v2.0 (2026-04-07) — three-layered grounding added; vulnerability MEDIUM → LOW.

### POS-M03: The Separation of Origins
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** LOW | **Last Reviewed:** 2026-04-07
**Chapter(s):** CH-04
**Position:** The evolutionary origin of a moral intuition is irrelevant to its validity. We evaluate inherited instincts by our chosen criteria, keeping what serves flourishing and discarding what doesn't.
**Best Objection:** How do you evaluate intuitions without relying on other intuitions? Risk of infinite regress.
**Current Rebuttal:** The regress terminates at the valence axiom (POS-M02) and epistemic duty (POS-E01). These are chosen, not derived — and explicitly acknowledged as such.
**Falsification Condition:** Show that the valence axiom and epistemic duty are themselves evolutionary products that cannot serve as independent evaluation criteria — i.e., that the regress does not actually terminate.
**Revision History:** v1.0 (2026-03-26).

---

## II. Epistemic Positions

### POS-E01: Epistemic Duty
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** LOW | **Last Reviewed:** 2026-04-07
**Chapter(s):** CH-02
**Position:** Truth-seeking is a moral obligation, not merely an intellectual preference. You cannot act morally with a false model of reality. Epistemic rationality is therefore a prerequisite for ethical rationality.
**Best Objection:** Some truths cause harm (e.g., a depressed person learning they're statistically likely to remain depressed). Is truth-seeking always a duty?
**Current Rebuttal:** The duty is to *seek* truth, not to *weaponize* it. Communication of truth is governed by the moral architecture (Mode A/B). The duty is against self-deception, not against tact.
**Falsification Condition:** Demonstrate a case where systematic self-deception reliably produces better moral outcomes than truth-seeking, across a population and over time.
**Revision History:** v1.0 (2026-03-26).

### POS-E02: Bayesian Updating as Epistemic Method
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** LOW | **Last Reviewed:** 2026-04-07
**Chapter(s):** CH-02
**Position:** Beliefs should be held as probability distributions and updated on evidence. This is the formal implementation of epistemic duty.
**Best Objection:** Bayesianism requires prior probabilities, which can be subjective and biased.
**Current Rebuttal:** Acknowledged — but Bayesian reasoning is self-correcting over time. Bad priors wash out with sufficient evidence. No alternative method has this convergence property.
**Falsification Condition:** Demonstrate an alternative epistemic method that converges on truth faster and more reliably than Bayesian updating across a representative range of domains.
**Revision History:** v1.0 (2026-03-26).

---

## III. Ethical Architecture Positions

### POS-A01: Dual-Process Decision Making
**Version:** 2.0 | **Confidence:** STRONG | **Vulnerability:** LOW
**Chapter(s):** CH-09, CH-10
**Position:** Default to pre-computed heuristics (rules/virtues) for 99% of decisions. Switch to explicit consequentialist calculation only when rule-following would cause irreversible catastrophic harm AND you can justify the override to a skeptical third party AND the procedural gating protocol is satisfied.
**Best Objection:** The threshold for switching is vague and gameable. Every consequentialist thinks their case is the special exception. Who decides when the conditions are met? (Mode-switching regress.)
**Current Rebuttal:** CH-10 now provides a two-layer architecture: (A) Three procedural gates that must be passed *before* the five conditions are even consulted — (i) bright-line trigger identification (imminent loss of life, irreversible systemic damage, or institutional capture), (ii) mandatory deliberation period (24h personal, longer institutional; exempt only for imminent physical danger), (iii) mandatory post-hoc review commitment. (B) Five substantive conditions: catastrophic irreversible harm, attributable to rule, last resort, articulable to a Reasonable Reviewer (Yudkowsky), self-interest absent. Historical test cases show correct answers. The ticking-bomb case is explicitly rejected. The mode-switching regress is resolved: the procedural gates are bright-line and verifiable, not dependent on the agent's self-assessment. The "who decides?" question is answered: the gates decide whether Mode B consideration is available; the five conditions decide whether the override is warranted; the post-hoc review provides accountability. Vulnerability downgraded from MEDIUM to LOW.
**Falsification Condition:** (a) Demonstrate a historical case where Mode B correctly applied produces a worse outcome than pure rule-following, across a population of such cases (not one-off moral luck), OR (b) show that the gating protocol fails to reduce the false-positive override rate compared to the ungated system, OR (c) present a superior dual-process architecture that resolves the mode-switching regress more effectively.
**Revision History:** v1.0 (2026-03-26) — initial. v1.1 (2026-04-05) — five conditions detailed, test cases added. v2.0 (2026-04-07) — Gating Protocol added; vulnerability MEDIUM → LOW.

### POS-A02: Morality as Coordination Technology (Bounded)
**Version:** 2.0 | **Confidence:** STRONG | **Vulnerability:** LOW
**Chapter(s):** CH-05, CH-06
**Position:** Morality *primarily* exists to solve coordination problems. Game theory is the primary analytical tool for understanding the vast majority of unnecessary suffering at institutional and political scale. However, game theory is explicitly *bounded*: three categories of moral phenomena operate outside the game-theoretic frame — (1) care and dependency (asymmetric relationships where one party cannot play the game), (2) supererogation (acts beyond what any strategic analysis can generate), and (3) expressive rationality (action aimed at expressing values, not producing outcomes). The full moral system requires game theory for coordination, care ethics for dependency, the virtue framework for supererogation, and expressive rationality for meaning.
**Best Objection:** Reduces morality to instrumental rationality. What about moral duties that don't serve coordination?
**Current Rebuttal:** CH-06 now explicitly addresses this through the "What Moloch Cannot Explain" section. The three non-coordination categories are named, developed, and integrated. Care is the substrate on which coordination operates (you need caring agents before cooperating agents). Supererogation is explained by the virtue layer. Expressive rationality is acknowledged as a distinct mode. The claim is bounded honestly: game theory handles coordination; other tools handle what coordination cannot reach. Vulnerability downgraded from MEDIUM to LOW because the overreach that previously made this position vulnerable has been corrected.
**Falsification Condition:** (a) Identify a major category of unnecessary suffering at scale that is NOT a coordination failure and that the framework has no adequate tool to address, OR (b) show that the three non-coordination categories (care, supererogation, expressive rationality) are actually coordination phenomena that game theory can model.
**Revision History:** v1.0 (2026-03-26) — initial. v2.0 (2026-04-07) — bounded with three non-coordination categories; vulnerability MEDIUM → LOW.

---

## IV. Political Positions

### POS-P01: Error-Correction Primacy
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** LOW | **Last Reviewed:** 2026-04-07
**Chapter(s):** CH-18
**Position:** The best political system is not the one that produces the best outcomes directly, but the one that corrects errors fastest. Optimize for feedback loops, not for specific policies.
**Best Objection:** Some errors are irreversible (existential risks). Error-correction is too slow for catastrophic threats.
**Current Rebuttal:** This is why existential risk gets special treatment (CH-31). Error-correction is the default; existential risk is the exception that warrants more direct intervention.
**Falsification Condition:** Demonstrate a political system that reliably produces better long-term outcomes by optimizing for specific policies rather than for error-correction speed — across multiple domains and over decades.
**Revision History:** v1.0 (2026-03-26).

### POS-P02: Institutional Mechanism Design over Ideology
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** MEDIUM
**Chapter(s):** CH-08, CH-17, CH-18
**Position:** Political problems are engineering problems. Design institutions to align individual incentives with collective welfare rather than relying on the virtue of leaders or citizens.
**Best Objection:** "Engineering" framing ignores power dynamics, historical injustice, and the fact that mechanism designers have their own interests.
**Current Rebuttal:** Mechanism design explicitly accounts for self-interest — that's the whole point. Historical injustice is a real input to the design problem, not something the framework ignores. But this needs more development.
**Falsification Condition:** Show that a non-mechanism-design approach (virtue-based leadership, ideological commitment, religious authority) reliably produces better institutional outcomes than incentive-aligned design across a representative range of governance problems.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

### POS-P03: Strong Free Speech Default
**Version:** 1.0 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-21
**Position:** Free expression is the epistemic immune system of a society. Censorship destroys the feedback loop. The default should be maximal speech protection with narrow, well-defined exceptions.
**Best Objection:** Unregulated speech can itself destroy epistemic commons (disinformation, coordinated harassment, stochastic terrorism). The "marketplace of ideas" may be a market failure.
**Current Rebuttal:** [NEEDS DEVELOPMENT] — Need to distinguish between speech and coordination-for-harm. The system's own game theory may require more nuance here than the framework suggests.
**Falsification Condition:** Demonstrate a speech-restriction regime that improves epistemic quality of public discourse over time without being captured by power interests — i.e., a censorship mechanism that reliably targets falsehood rather than dissent.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

### POS-P04: Constrained Democracy
**Version:** 1.0 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-20
**Position:** Democracy is the best available error-correction mechanism but must be constrained by constitutional rights, separation of powers, and federalism to prevent tyranny of the majority and rational irrationality of voters.
**Best Objection:** Constitutional constraints are anti-democratic and often serve entrenched interests rather than protecting genuine rights.
**Current Rebuttal:** The constraint is *on* the democratic process, not *against* it — like guardrails on a highway. The question is which constraints are legitimate, which requires a theory of rights (CH-19).
**Falsification Condition:** Show that unconstrained democracy produces better outcomes for minorities and long-term welfare than constitutionally constrained democracy, across a representative sample of countries and time periods.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

### POS-P05: Subsidiarity
**Version:** 1.0 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-17
**Position:** Decisions should be made at the lowest level of governance competent to handle them. Local knowledge (metis) is destroyed by centralization.
**Best Objection:** Some problems (climate, pandemics, AI) are inherently global and cannot be solved locally. Subsidiarity can also mean local tyranny.
**Current Rebuttal:** Subsidiarity is a default, not an absolute. Problems with genuine externalities that cross jurisdictional boundaries escalate upward. The framework handles this via internalization of externalities.
**Falsification Condition:** Demonstrate that centralized decision-making reliably outperforms local decision-making even for problems without cross-jurisdictional externalities — i.e., that metis destruction is worth the coordination gains.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

### POS-P06: Justice as Restitution + Deterrence (with Desert Reconstructed)
**Version:** 1.1 | **Confidence:** PROVISIONAL | **Vulnerability:** HIGH
**Chapter(s):** CH-22
**Position:** The purpose of the justice system is (1) to make victims whole (restitution), (2) to deter future offenses (deterrence), and (3) to incapacitate those who cannot be deterred. Pure retribution — punishment solely for its own sake — is not endorsed, but the intuition behind desert may be partially reconstructable as a coordination device: communities that are seen to hold wrongdoers accountable sustain higher trust than those that do not. CH-22 develops this more nuanced treatment.
**Best Objection:** Purely consequentialist justice can justify punishing the innocent if it deters effectively. Also, many people have deep moral intuitions about desert that may be load-bearing.
**Current Rebuttal:** The framework's Mode A rights architecture blocks punishing the innocent (rights are strong defaults, not tradeable). The desert intuition is taken seriously in CH-22 as potentially load-bearing for coordination, not dismissed as mere vestige. But the full reconstruction of desert within the framework remains incomplete. This is still one of the system's weakest areas — rated PROVISIONAL with HIGH vulnerability honestly.
**Falsification Condition:** (a) Show that a purely consequentialist justice system (no desert element) sustains higher social trust than one that incorporates desert, OR (b) reconstruct desert within the framework in a way that is more compelling than the current partial reconstruction — which would upgrade, not falsify, the position.
**Revision History:** v1.0 (2026-03-26). v1.1 (2026-04-05) — desert reconstruction added. | **Last Reviewed:** 2026-04-07

### POS-P07: Rights as Coordination Equilibria
**Version:** 1.0 | **Confidence:** PROVISIONAL | **Vulnerability:** HIGH
**Chapter(s):** CH-19
**Position:** Rights are not natural or God-given. They are Schelling points — coordination equilibria that rational agents converge on because respecting them produces better outcomes than violating them.
**Best Objection:** If rights are merely instrumental, they can be overridden whenever the calculus changes. This is exactly what rights are supposed to prevent.
**Current Rebuttal:** [NEEDS SIGNIFICANT DEVELOPMENT] — The Mode A/B architecture may help here (rights are Mode A defaults that require extreme justification to override), but this needs rigorous treatment.
**Falsification Condition:** Show that rights grounded in non-instrumental foundations (Dworkin's "trumps," natural rights, divine command) produce more stable protection of individual interests than coordination-equilibrium rights, across a representative range of political systems.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

---

## V. Economic Positions

### POS-EC01: Markets as Information Systems
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** LOW
**Chapter(s):** CH-25
**Position:** Markets are primarily information-processing systems (Hayek). Prices aggregate dispersed knowledge that no central planner could collect. Market failure is real but is the exception, not the rule.
**Best Objection:** Markets also transmit and amplify power asymmetries, not just information. The "information" framing obscures distributional questions.
**Current Rebuttal:** Power asymmetries are a real market failure to be addressed via mechanism design, not a refutation of the informational function.
**Falsification Condition:** Demonstrate a non-market information-aggregation mechanism that outperforms prices in coordinating production and consumption across a complex economy at scale.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

### POS-EC02: Pigovian Correction of Externalities
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** MEDIUM
**Chapter(s):** CH-27
**Position:** When private costs diverge from social costs (externalities), the correct intervention is to realign them via taxes/subsidies (Pigovian), not to ban or mandate. Make the selfish move identical to the social move.
**Best Objection:** Pigovian taxes require accurate measurement of externalities, which is often impossible. Also, they can be regressive.
**Current Rebuttal:** Measurement difficulty is an engineering problem, not a conceptual one. Regressivity can be addressed via revenue recycling (carbon dividend, etc.).
**Falsification Condition:** Show that command-and-control regulation reliably produces better outcomes than Pigovian correction for the same class of externality, controlling for measurement accuracy and political capture.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

### POS-EC03: Safety Net as Insurance + Capability Floor
**Version:** 1.1 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-28
**Position:** The welfare state is justified on two grounds: (1) social insurance (rational agents behind a veil of uncertainty would buy insurance against catastrophic outcomes), AND (2) a capability floor (all persons deserve the real freedoms needed to live lives they have reason to value, per Sen's capability approach). The insurance framing handles uncertain risks; the capability framing handles predictable disadvantage.
**Best Objection:** The insurance framing excludes people who are *predictably* disadvantaged (born into poverty, systemic discrimination). Insurance is for *uncertain* risks, not *known* inequalities.
**Current Rebuttal:** The capability-floor extension (developed in CH-28 with Sen's *Development as Freedom*) explicitly addresses this gap. CH-24's distributional analysis test now embeds the capability frame into the policy method. CH-41's engagement with Rawls confirms the overlap between the framework's position and Rawls's difference principle while maintaining distinct justification. The position has been strengthened from PROVISIONAL to MODERATE; vulnerability downgraded from HIGH to MEDIUM because the capability extension directly addresses the original best objection.
**Falsification Condition:** (a) Show that a purely insurance-based safety net (without capability floor) produces equivalent welfare outcomes, OR (b) show that a purely capabilities-based system (without insurance framing) produces better outcomes at lower cost, OR (c) identify a category of predictable disadvantage that the capability floor does not adequately address.
**Revision History:** v1.0 (2026-03-26). v1.1 (2026-04-05) — capability floor added; PROVISIONAL → MODERATE. | **Last Reviewed:** 2026-04-07

### POS-EC04: Prediction Markets as Epistemic Infrastructure
**Version:** 1.0 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-08, CH-20
**Position:** Prediction markets are the highest-fidelity mechanism for aggregating beliefs about future states. They should be legalized and expanded as a tool for policy evaluation.
**Best Objection:** Thin markets are easily manipulated. Prediction markets can also create perverse incentives (betting on assassinations, terrorist attacks).
**Current Rebuttal:** Manipulation risk decreases with market depth. Perverse incentive problems are solvable through market design (conditional markets, exclusion of beneficiaries).
**Falsification Condition:** Demonstrate that an alternative belief-aggregation mechanism (expert panels, deliberative polls, AI forecasting) consistently outperforms prediction markets in calibration and resolution across a representative range of policy-relevant questions.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

### POS-EC05: Fiscal Conservatism with Social Investment
**Version:** 1.0 | **Confidence:** PROVISIONAL | **Vulnerability:** HIGH
**Chapter(s):** CH-30
**Position:** Government spending should be constrained by cost-benefit analysis with strong presumption against debt financing. However, investments with demonstrable long-term returns (education, infrastructure, R&D, public health) clear this bar.
**Best Objection:** "Cost-benefit analysis" can be rigged to justify anything depending on discount rates, how you value non-market goods, and whose costs/benefits count.
**Current Rebuttal:** [NEEDS DEVELOPMENT] — Need to address the methodology of public cost-benefit analysis honestly, including its known failure modes.
**Falsification Condition:** Show that unconstrained deficit spending produces better long-term outcomes (growth, stability, intergenerational equity) than cost-benefit-constrained fiscal policy, across a representative sample of countries.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

---

## VI. Frontier Positions

### POS-F01: Existential Risk as Moral Priority
**Version:** 1.0 | **Confidence:** STRONG | **Vulnerability:** MEDIUM
**Chapter(s):** CH-31
**Position:** Preventing human extinction (and other existential catastrophes) is a moral priority that outweighs most other concerns, because the expected value of the future is astronomically large.
**Best Objection:** "Astronomical value of the future" arguments can be used to justify almost anything (torturing one person to save trillions of future people). Also, heavy discounting of future value undermines the argument.
**Current Rebuttal:** The Mode A/B architecture constrains this — you cannot violate fundamental rights even for existential risk reduction, except under extreme and specifically defined conditions. The discounting objection needs engagement.
**Falsification Condition:** (a) Show that heavy temporal discounting is rationally required (not merely psychologically natural), making the astronomical value of the future collapse, OR (b) show that the Mode A constraints are insufficient to prevent existential risk logic from licensing atrocities.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

### POS-F02: Cautious AI Development
**Version:** 1.0 | **Confidence:** MODERATE | **Vulnerability:** MEDIUM
**Chapter(s):** CH-32
**Position:** AI development is the most important coordination problem humanity faces. The rational stance is cautious development with strong alignment research, not acceleration or moratorium.
**Best Objection:** "Cautious development" is vague and may be unstable — competitive pressures (Moloch) push toward acceleration regardless of what any individual actor wants.
**Current Rebuttal:** This is precisely the Moloch problem the system is designed to solve. The question is what coordination mechanisms can actually work. [NEEDS DEVELOPMENT]
**Falsification Condition:** (a) Demonstrate that full acceleration produces better alignment outcomes than cautious development (e.g., racing to capability leads to racing to alignment), OR (b) demonstrate that moratorium is achievable and stable under competitive international dynamics.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

### POS-F03: Consciousness-Based Moral Circle
**Version:** 1.0 | **Confidence:** PROVISIONAL | **Vulnerability:** HIGH
**Chapter(s):** CH-05, CH-34
**Position:** Moral patienthood extends to all systems with conscious experience. This potentially includes some animals and could include future AIs. The boundary is consciousness, not species membership.
**Best Objection:** We have no reliable test for consciousness. Basing moral patienthood on an undetectable property is practically useless.
**Current Rebuttal:** [NEEDS SIGNIFICANT DEVELOPMENT] — Need to engage with the hard problem of consciousness and develop practical heuristics even under uncertainty.
**Falsification Condition:** (a) Solve the hard problem of consciousness in a way that shows valence does not extend beyond humans, OR (b) show that a species-membership-based moral circle produces better moral outcomes than a consciousness-based one, OR (c) develop a reliable consciousness test that contradicts the framework's current inclusion heuristics.
**Revision History:** v1.0 (2026-03-26). | **Last Reviewed:** 2026-04-07

---

## Archive — Deprecated Positions

*No positions deprecated yet. When a position is replaced, move it here with a note explaining what replaced it and why.*

<!-- TEMPLATE:
### [DEPRECATED] POS-XXX: [Name]
**Replaced By:** POS-YYY
**Date Deprecated:** YYYY-MM-DD
**Reason:** [Why the new position is superior]
-->
