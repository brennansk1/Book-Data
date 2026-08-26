# Phase 3: Cross-Chapter Consistency and Terminology Audit

**Date:** 2026-04-05
**Scope:** All 47 chapter drafts in Book/Drafts/ (CH-01 through CH-48; CH-16, CH-26, CH-29, CH-30, CH-31, CH-32, CH-33, CH-34, CH-35, CH-37, CH-40, CH-41, CH-43, CH-44 also present)
**Method:** Systematic grep across all chapter files, close reading of six chapters for tone, and cross-referencing against POSITION_REGISTRY.md

---

## 3A. Terminology Glossary and Consistency Audit

### Foundational Terms

#### "Valence"
- **First defined:** CH-03 (line 38): "Valence is not an emotion. It is not happiness. It is not preference satisfaction. It is the qualitative character of conscious experience along the suffering-to-flourishing spectrum."
- **Used in:** CH-01, CH-02, CH-03, CH-04, CH-05, CH-06, CH-08, CH-09, CH-11, CH-13, CH-15, CH-16, CH-22, CH-28, CH-30, CH-31, CH-32, CH-33, CH-34, CH-37, CH-38, CH-39, CH-42, CH-43, CH-44, CH-45, CH-46, CH-48
- **Consistency:** GOOD. Two related terms are used: "valence axiom" (the normative claim that suffering matters; used in ~25 chapters) and "valence realism" (the metaethical position that suffering/joy are objective physical states; used in CH-44, CH-45, CH-46, CH-47). These two terms are distinct and their usage is consistent, but the relationship between them could be made more explicit. The Registry lists POS-M02 as "Valence Realism" (the metaphysical claim) and the axiom itself is embedded in POS-M02's description. The term "valence axiom" is the more commonly used term in the chapters (~25+ occurrences) while "valence realism" appears in only ~6 places.
- **FLAG [LOW SEVERITY]:** The distinction between "valence realism" (metaethical position: suffering/joy are objective physical states) and "valence axiom" (normative commitment: suffering matters) is never explicitly drawn in a single passage. A reader could conflate them. Consider adding a brief clarification in CH-03 or CH-46.

#### "Constructivist Realism"
- **First defined:** CH-01 (line 51): "which we call Constructivist Realism as a working name" and (line 57): "values are constructed by conscious agents but constrained by objective features of reality."
- **Used in:** CH-01, CH-05, CH-37, CH-46
- **Consistency:** GOOD. The definition is stable across all uses. CH-37 correctly describes it as "closer to some forms of constructivism than to strict realism." CH-46 restates it faithfully.
- **FLAG [LOW SEVERITY]:** Used in only 4 chapters. For the system's foundational metaethical position, this is surprisingly sparse. Many chapters that do metaethical work (CH-03, CH-04, CH-36, CH-38, CH-44) never use the term, relying instead on "valence axiom" or "the framework's position." This is not an inconsistency but may leave the reader unsure whether "constructivist realism" is still operative by mid-book.

#### "Complex Value Vector"
- **First defined:** CH-03 (implicit, expanded in CH-13, CH-15). CH-15 (line 82) gives the fullest enumeration: "hedonic tone, autonomy, competence, connection, understanding, meaning."
- **Used in:** CH-05, CH-13, CH-15, CH-38, CH-39, CH-42, CH-44, CH-45, CH-46
- **Consistency:** GOOD. The content is stable. CH-44 lists the same dimensions. CH-38 uses it correctly to counter the utility monster objection. CH-46 references it as a foundational element.
- **FLAG [LOW SEVERITY]:** The full enumeration (all six dimensions) appears only in CH-15, CH-38, CH-44, and CH-45. Other chapters reference the "complex value vector" without listing the components. A reader encountering the term in CH-39 or CH-42 without having read CH-15 recently might not recall the specific dimensions. Not a contradiction, but an accessibility issue.

#### "Epistemic Duty"
- **First defined:** CH-02 (line 24): "truth-seeking is not merely an intellectual preference but a prerequisite for ethical action."
- **Used in:** CH-02, CH-04, CH-11, CH-24, CH-42, CH-44, CH-45, CH-46, CH-47, CH-48
- **Consistency:** EXCELLENT. Every usage refers to the same concept (truth-seeking as moral obligation). No variant definitions. CH-48 restates it faithfully. CH-44 correctly identifies it as one of the framework's two starting points alongside the valence axiom.

#### "Performative Incoherence"
- **First defined:** CH-01 (line 95, briefly) and CH-03 (line 64, fully): "The denial of valence's moral significance cannot be sincerely lived. It can only be asserted from the safety of an armchair."
- **Used in:** CH-01, CH-02, CH-03, CH-05, CH-37, CH-44, CH-46
- **Consistency:** GOOD. All uses refer to the same concept. CH-37 extends it to nihilism ("the act of taking any action is incompatible with the belief that nothing matters"), which is a legitimate extension. CH-44 applies it to natural law engagement.
- **FLAG [LOW SEVERITY]:** The term is sometimes "performative incoherence" (noun) and sometimes "performatively incoherent" (adjective). Both are standard. No issue.

---

### Diagnostic Terms

#### "Moloch"
- **First defined:** CH-06 (line 28): "Moloch is the name we give to the phenomenon in which individually rational choices combine to produce collectively irrational outcomes."
- **Used in:** CH-01, CH-05, CH-06, CH-07, CH-08, CH-09, CH-13, CH-17, CH-23, CH-30, CH-32, CH-33, CH-46
- **Consistency:** EXCELLENT. Every usage is faithful to the CH-06 definition. CH-32 applies it to AI development correctly. CH-30 applies it to fiscal politics correctly. CH-46 restates it faithfully. The metaphor is never misused or diluted.

#### "Coordination Failure"
- **First defined:** CH-06 (line 1, title) with technical definition via Nash equilibria and Prisoner's Dilemma.
- **Used in:** CH-01, CH-05, CH-06, CH-08, CH-17, CH-24, CH-37, CH-46
- **Consistency:** EXCELLENT. Always used in the game-theoretic sense established in CH-06.

#### "Shadow of the Future"
- **First defined:** CH-06 (line 143, attributed to Axelrod): "the possibility that the person you're interacting with now will interact with you again tomorrow."
- **Used in:** CH-06, CH-07, CH-08, CH-14, CH-17, CH-23, CH-46
- **Consistency:** EXCELLENT. CH-07 gives the fullest treatment. CH-14 applies it to relationships correctly. All uses refer to the same game-theoretic concept.

#### "Nash Equilibrium"
- **First defined:** CH-06 (line 38): "a situation in which no player can improve their outcome by unilaterally changing their strategy, given what the other players are doing."
- **Used in:** CH-06, CH-07, CH-08, CH-46
- **Consistency:** EXCELLENT. Technical usage is correct throughout.

#### "Schelling Point"
- **First defined:** CH-07 (line 199ff) in the context of rules as focal points; CH-09 (line 98) gives a concise definition: "a solution that stands out as obvious, allowing multiple agents to converge on it without explicit communication."
- **Used in:** CH-07, CH-09, CH-19, CH-46
- **Consistency:** GOOD. CH-19 uses it for rights ("rights are coordination equilibria -- Schelling points") which is a legitimate extension. CH-46 preserves this.
- **FLAG [LOW SEVERITY]:** The concept is introduced in CH-07 but its definition is somewhat buried in context. CH-09 gives the cleaner standalone definition. Not a contradiction, but the reader's first encounter (CH-07) lacks the crispness of the CH-09 definition.

#### "Mechanism Design"
- **First defined:** CH-06 (line 168): "the engineering project we call 'mechanism design.'" CH-08 (title chapter) gives the full treatment: "given that people will respond to incentives, how should we structure the incentives so that what they will do is also what they should do?"
- **Used in:** CH-06, CH-07, CH-08, CH-17, CH-20, CH-23, CH-24, CH-25, CH-27, CH-30, CH-33, CH-34, CH-35, CH-41, CH-43, CH-46, CH-47
- **Consistency:** EXCELLENT. This is one of the most consistently used terms in the book. Every chapter applies it in the same sense.

---

### Architectural Terms

#### "Mode A" / "Mode B"
- **First defined:** CH-09 (Mode A: rule-following default) and CH-10 (Mode B: consequentialist override with five conditions).
- **Used in:** CH-01, CH-07, CH-09, CH-10, CH-11, CH-12, CH-13, CH-14, CH-16, CH-19, CH-38, CH-39, CH-42, CH-44, CH-45, CH-46, CH-48
- **Consistency:** EXCELLENT. This is the most critical term in the book and it is used with remarkable consistency across all chapters. Mode A is always "rule-following default"; Mode B is always "consequentialist override requiring all five conditions." The five conditions are consistently stated: (1) catastrophic irreversible harm, (2) attributable to the rule, (3) last resort, (4) articulable to skeptical third party, (5) self-interest absent.
- **No chapter uses Mode B in a looser or more permissive sense than CH-10 defines it.** This is a significant achievement given how many chapters invoke the concept.
- CH-19 adds a sixth condition for rights specifically (supermajority agreement), which is flagged as an addition, not a redefinition.

#### "Chesterton Fence"
- **First defined:** CH-09 (title concept): "requires understanding before modification. Tear down the fence once you know why it was built."
- **Used in:** CH-09, CH-11, CH-46, CH-47
- **Consistency:** GOOD. Sparse usage but faithful.

#### "Dual-Process"
- **First defined:** CH-02 (line 44) introduces the cognitive science concept (System 1 / System 2). CH-09 (line 26) and CH-10 apply it to ethics as Mode A / Mode B.
- **Used in:** CH-01, CH-02, CH-07, CH-08, CH-09, CH-10, CH-11, CH-12, CH-16, CH-38, CH-39, CH-42, CH-44, CH-45, CH-46, CH-48
- **Consistency:** GOOD. The cognitive science usage (CH-02) and the ethical architecture usage (CH-09+) are related but distinct. CH-02 discusses Kahneman's System 1/2; Books III+ use "dual-process" to mean Mode A/B. The book draws the connection explicitly (Mode A = heuristic/fast; Mode B = deliberative/slow), which prevents confusion.
- **FLAG [LOW SEVERITY]:** A reader familiar with cognitive science might expect "dual-process ethics" to map precisely onto System 1/System 2. The book's Mode A/B is related but different -- Mode A includes deliberate rule-selection, not just intuitive snap judgment. CH-09 partially addresses this but the distinction could be sharper.

#### "Twelve Virtues"
- **First defined:** CH-02 (line 212, introduced) and CH-11 (line 46, fully grounded). The list: curiosity, relinquishment, lightness, evenness, argument/steel-manning, empiricism, simplicity, humility (epistemic) plus perfectionism/tsuyoku naritai, precision, scholarship, the void (instrumental).
- **Used in:** CH-02, CH-10, CH-11, CH-42, CH-46
- **Consistency:** GOOD. CH-46 correctly summarizes them as "eight epistemic virtues... and four instrumental virtues." CH-42 references them in the virtue ethics debate.
- **FLAG [MEDIUM SEVERITY]:** The twelve virtues are explicitly attributed to Yudkowsky in CH-11 (line 48: "inherited from Eliezer Yudkowsky's writings"). However, the book's chapter on virtue ethics (CH-42) refers to "the framework's twelve virtues" without noting the attribution. This could create confusion about whether these are the book's original contribution or borrowed. More importantly, the twelve virtues are all epistemic/instrumental -- there are no explicitly *moral* virtues (courage, justice, temperance, compassion) in the list. CH-42 discusses Aristotelian moral virtues at length but never reconciles why the framework's virtue list omits them. This is a gap rather than an inconsistency, but it weakens the virtue ethics engagement.

#### "Informed Automaticity"
- **First defined:** CH-12 (concept of Stage 3 moral development: instinct -> reflection -> habit). CH-46 (line 105) gives the term explicitly: "informed automaticity, where reflection has been completed and its conclusions have become second nature."
- **Used in:** CH-45 (line 134), CH-46 (line 105)
- **Consistency:** GOOD but very sparse. Only 2 explicit uses of the term. The underlying concept (Stage 3 development) appears more widely.

---

### Political/Economic Terms

#### "Subsidiarity"
- **First defined:** CH-17 (line 92): "decisions should be made at the lowest level of governance competent to handle them."
- **Used in:** CH-17, CH-23, CH-24, CH-35, CH-46
- **Consistency:** EXCELLENT. Every usage matches the CH-17 definition. CH-24 applies it correctly in all its policy case studies.

#### "Error-Correction Primacy"
- **First defined:** CH-18 (line 18): "The best political system is not the one that produces the best outcomes directly, but the one that corrects errors fastest."
- **Used in:** CH-18, CH-24, CH-43, CH-44, CH-46
- **Consistency:** EXCELLENT. Stable across all uses. CH-43 correctly applies it to argue against revolutionary replacement.

#### "Hayekian Knowledge Test"
- **First defined:** CH-24 (line 234): a test asking whether the policy-maker has the knowledge needed to implement the policy effectively.
- **Used in:** CH-24, CH-46, CH-47, CH-48
- **Consistency:** GOOD. Sparse but faithful. Only fully explained in CH-24.

#### "Pigovian" (taxes, correction, fit test)
- **First defined:** CH-08 (line 40): "a Pigovian tax... internalize the externality."
- **Used in:** CH-08, CH-17, CH-24, CH-27, CH-30, CH-45, CH-46, CH-48
- **Consistency:** EXCELLENT. CH-27 is the full treatment chapter. All other uses are faithful to the core concept. The "Pigovian fit test" (CH-24) is a named extension that is consistently referenced.

#### "Capability Approach"
- **First defined:** CH-28 develops the concept via Sen. The term "capability floor" is the book's specific formulation.
- **Used in:** CH-28, CH-30, CH-47
- **Consistency:** GOOD. CH-30 correctly references it alongside the mechanism design framework.
- **FLAG [LOW SEVERITY]:** The term "capability approach" is used in CH-28 and CH-30, but the underlying concept (capability floor, real freedoms) appears in more chapters without the formal name. Not an inconsistency, but the formal terminology could be used more consistently when the concept is invoked.

---

### Position Labels

#### POS-M01 (Constructivist Realism)
- Referenced explicitly in: CH-46 (line 30)
- Content chapters: CH-01 (defines it), CH-37 (defends it against anti-realism)
- **Consistency:** The POS-M01 label itself is rarely used in the text. The substance is consistent.

#### POS-A01 (Dual-Process Decision Making)
- Referenced explicitly in: CH-46 (line 83)
- Content chapters: CH-09, CH-10 (define it), numerous others use it
- **Consistency:** EXCELLENT. See Mode A/B analysis above.

#### POS-P06 (Justice as Restitution + Deterrence)
- Referenced explicitly in: CH-22 (lines 14, 193), CH-45 (line 166), CH-46 (line 124)
- **Consistency:** See Section 3B below for detailed analysis.

#### POS-P07 (Rights as Coordination Equilibria)
- Referenced explicitly in: CH-46 (line 125)
- Content chapters: CH-19 (defines it)
- **Consistency:** See Section 3B below for detailed analysis.

#### POS-EC03 (Safety Net as Insurance + Capability Floor)
- Referenced explicitly in: CH-28 (line 16), CH-46 (line 133)
- **Consistency:** See Section 3B below for detailed analysis.

---

## 3B. Position Consistency: HIGH-Vulnerability Positions

### POS-A01: Dual-Process Decision Making (Vulnerability: MEDIUM, per Registry)

**Registry definition:** "Default to pre-computed heuristics (rules/virtues) for 99% of decisions. Switch to explicit consequentialist calculation only when rule-following would cause irreversible catastrophic harm AND you can justify the override to a skeptical third party."

**Chapter usage audit:**
- CH-09 and CH-10: Define and defend the position in full detail. Five conditions specified. CONSISTENT.
- CH-13: Applies Mode A/B in daily life scenarios. Uses the five conditions correctly. CONSISTENT.
- CH-19: Extends to rights (adds sixth condition: supermajority). Flagged as extension, not deviation. CONSISTENT.
- CH-38: Uses dual-process to distinguish framework from pure utilitarianism. CONSISTENT.
- CH-39: Uses it to distinguish framework from pure deontology. CONSISTENT.
- CH-42: Uses it to provide decision procedures virtue ethics lacks. CONSISTENT.
- CH-44: Notes overlap with natural law absolutes. CONSISTENT.
- CH-48: Restates as oath clause. CONSISTENT.

**Verdict: NO CONTRADICTIONS FOUND.** This is the book's most consistently applied position.

### POS-P06: Justice as Restitution + Deterrence (Vulnerability: HIGH)

**Registry definition:** "The purpose of the justice system is (1) to make victims whole (restitution), (2) to deter future offenses (deterrence), and (3) to incapacitate those who cannot be deterred. Retribution for its own sake is a vestigial instinct to be overcome."

**Chapter usage audit:**
- CH-22: Defines and defends the position. Calls retribution "not a foundational goal" but "recognized as a real human intuition that must be acknowledged and sometimes accommodated." This is MORE NUANCED than the Registry's characterization of retribution as "a vestigial instinct to be overcome."
- CH-45 (line 150): References Buddhist teaching that "retaliation perpetuates cycles of harm" and says the framework's treatment "de-emphasizes retribution."
- CH-45 (line 166): Says Ubuntu-influenced restorative justice "aligns with the framework's position on justice (Chapter 22, POS-P06)."

**FLAG [MEDIUM SEVERITY]:** There is a tension between the Registry's description (retribution is "a vestigial instinct to be overcome") and CH-22's actual treatment (retribution is "a real human intuition that must be acknowledged and sometimes accommodated" -- "the justice system should produce outcomes that satisfy retributive intuitions when those intuitions track real features of the situation"). CH-22 is substantially more sympathetic to retribution than the Registry suggests. The Registry should be updated to match CH-22's more nuanced position.

### POS-P07: Rights as Coordination Equilibria (Vulnerability: HIGH)

**Registry definition:** "Rights are not natural or God-given. They are Schelling points -- coordination equilibria that rational agents converge on because respecting them produces better outcomes than violating them."

**Registry's best objection:** "If rights are merely instrumental, they can be overridden whenever the calculus changes. This is exactly what rights are supposed to prevent."

**Chapter usage audit:**
- CH-19: Defines and defends the position. Engages the Dworkinian objection directly. Provides three-part response: (1) Mode A/B protection, (2) extra-strict override conditions for rights (sixth condition), (3) practical equivalence with "lexically prior" theories. CONSISTENT WITH BUT STRONGER THAN REGISTRY.
- CH-41 (line 180): "Agreement with Rawls that these take priority and cannot be traded off against aggregate welfare, though we ground them in coordination considerations." CONSISTENT.
- CH-45 (line 82): "Basic liberties are not subject to aggregate welfare trade-offs." CONSISTENT.
- CH-48 (line 54): Rights as "near-inviolable default." CONSISTENT.

**FLAG [LOW SEVERITY]:** The Registry says the rebuttal "NEEDS SIGNIFICANT DEVELOPMENT," but CH-19 actually provides substantial development (the three-part response to Dworkin). The Registry is out of date relative to the chapter. Should be updated.

### POS-EC05: Fiscal Conservatism with Social Investment (Vulnerability: HIGH)

**Registry definition:** "Government spending should be constrained by cost-benefit analysis with strong presumption against debt financing. However, investments with demonstrable long-term returns (education, infrastructure, R&D, public health) clear this bar."

**Chapter usage audit:**
- CH-30: Develops fiscal principles in detail. Distinguishes investment spending (debt-financeable) from consumption spending (current-financed). Discusses taxation principles (tax externalities first, then progressive income). CONSISTENT.
- CH-24: Policy evaluation framework applies cost-benefit analysis systematically. CONSISTENT.
- CH-46 (line 135): "Investment-level spending debt-financeable; consumption-level spending current-financed." CONSISTENT.

**FLAG [LOW SEVERITY]:** The Registry says the rebuttal "NEEDS DEVELOPMENT" regarding methodology of cost-benefit analysis. CH-30 partially addresses this (discussing discount rates, intergenerational considerations) but does not address the CBA methodology critique head-on. The Registry's vulnerability assessment remains accurate.

### POS-F03: Consciousness-Based Moral Circle (Vulnerability: HIGH)

**Registry definition:** "Moral patienthood extends to all systems with conscious experience. This potentially includes some animals and could include future AIs. The boundary is consciousness, not species membership."

**Chapter usage audit:**
- CH-03 (line 211): Acknowledges this as "a provisional position (POS-F03 in the Registry, rated HIGH vulnerability)" and admits "without a test for consciousness, how do we apply these principles in practice?" CONSISTENT.
- CH-34: Applies the position to environmental ethics. Ranks animals by likelihood of consciousness (vertebrates > cephalopods > insects > plants). CONSISTENT.
- CH-32 (line 131): "If (when) AI systems become genuinely conscious, they acquire moral status... The valence axiom does not distinguish by substrate." CONSISTENT.
- CH-38 (line 52): Credits Singer for the expanding moral circle. CONSISTENT.
- CH-45 (line 34): Credits Singer again. CONSISTENT.

**Verdict: NO CONTRADICTIONS FOUND.** The position is consistently applied, and its acknowledged weakness (no test for consciousness) is honestly flagged in every chapter that invokes it.

---

## 3C. Argument Contradiction Analysis

### Test 1: "We are not utilitarian" vs. utilitarian-style reasoning

**Anti-utilitarian claims:**
- CH-45 (line 24): "The framework is not utilitarian."
- CH-38 (entire chapter): "Against Pure Utilitarianism" -- rejects scalar welfare, aggregation across persons, pure consequentialism, and maximization.
- CH-09/CH-10: Mode A/B architecture explicitly designed to prevent case-by-case consequentialist calculation.

**Utilitarian-adjacent reasoning:**
- CH-24: Policy evaluation uses cost-benefit analysis systematically.
- CH-27: Pigovian taxes justified by welfare calculus.
- CH-30: Fiscal policy uses cost-benefit analysis with intergenerational welfare weighting.
- CH-28: Safety net justified partly by aggregate welfare gains.
- CH-34: Animal welfare arguments use scale-of-suffering reasoning ("tens of billions of farmed animals").
- CH-45 (line 32): Explicitly praises "utilitarianism's willingness to make empirical claims about welfare" and adopts "cost-benefit discipline."

**Verdict: NO CONTRADICTION, but a tension that needs monitoring.**

The framework is explicitly clear about what it rejects from utilitarianism (scalar aggregation, pure consequentialism, maximization, rejection of deontic constraints) and what it accepts (welfare matters, consequences matter, scale matters, empirical evaluation of policies). Mode B is consequentialist calculation under strict constraints. The policy chapters (CH-24, CH-27, CH-30) use cost-benefit analysis as a tool within the framework, not as the framework itself -- they always check CBA results against rights, subsidiarity, and error-correction (Step 6 in CH-24).

**FLAG [MEDIUM SEVERITY]:** The risk is that applied chapters (especially CH-24, CH-27, CH-30) read as more straightforwardly utilitarian than the foundational chapters (CH-09, CH-10, CH-38) would endorse. A reader who encounters CH-24's cost-benefit apparatus first might reasonably conclude this is a utilitarian framework. The distinction between "using CBA as one tool among several" and "being utilitarian" could be drawn more sharply in the economic chapters. Consider adding a brief reminder in CH-24's introduction that CBA is constrained by the Mode A/B architecture and the rights framework.

### Test 2: Rights as strong vs. easily overridable

**Rights as strong:**
- CH-19 (line 38): "Rights are strong. Within their scope, they are supposed to resist ordinary political pressures."
- CH-19 (line 32): Rights as "trumps" (Dworkin).
- CH-19 (line 191): "Rights function as Mode A defaults -- strong presumptions against interference."
- CH-41 (line 62): "Basic liberties are not subject to aggregate welfare trade-offs."
- CH-45 (line 82): Same claim.
- CH-48 (line 54): "near-inviolable default."

**Rights as overridable:**
- CH-19 (line 74-78): The three-part response to Dworkin admits rights are not lexically prior, but argues the override conditions are so strict as to be practically equivalent.
- CH-19 (line 123): "Rights are not absolute in the sense of being unlimited in scope. Every right has limits."
- CH-19 (line 133): Rights conflicts resolved via Mode B conditions.
- CH-19 (line 151): "Positive rights have a ceiling."

**Verdict: NO CONTRADICTION.** The framework has a clear, consistent position: rights are extremely strong defaults that function as near-absolutes, but they are not metaphysically absolute. They can be overridden only under extraordinarily strict conditions (all five Mode B conditions plus the supermajority sixth condition). This position is maintained across every chapter that discusses rights. The framework explicitly acknowledges the tension (CH-19 line 78: "the distinction between 'rights as lexically prior' and 'rights as extremely strong defaults' is more rhetorical than practical") and argues for its resolution.

### Test 3: Veil of ignorance -- accepted or rejected?

**Accepted:**
- CH-28 (line 32): "This is Rawls's 'original position' with a veil of ignorance, and the framework accepts the insight without accepting all of Rawls's specific conclusions."
- CH-45 (line 80): "The veil of ignorance as a clarifying device. The framework uses this move explicitly in the insurance argument for welfare."
- CH-40 (line 218): Refers to "insurance arguments, veil of ignorance" as absorbed insights.

**Qualified/rejected:**
- CH-41 (line 96): Section titled "The Veil of Ignorance Is Too Thick."
- CH-41 (line 104): "The veil of ignorance is a useful heuristic but not a decision procedure."
- CH-45 (line 88): "What we do not take: the strict maximin reasoning behind the veil."

**Verdict: NO CONTRADICTION.** The framework has a nuanced, consistent position: the veil of ignorance is accepted as a "clarifying device" and "useful heuristic" that strips self-interest from reasoning, but rejected as a "decision procedure" that generates specific principles (especially maximin). This position is stated identically in CH-28, CH-41, and CH-45.

### Test 4: Mode B usage across chapters

**Mode B definition (CH-10):** Consequentialist override requiring ALL FIVE conditions: (1) catastrophic irreversible harm, (2) attributable to the rule, (3) last resort, (4) articulable to skeptical third party, (5) self-interest absent.

**Cross-chapter audit:**
- CH-09: Introduces Mode A/B threshold. CONSISTENT.
- CH-10: Full definition. Five conditions. Test cases (Nazi at door: yes. Ticking bomb: NO. Civil disobedience: yes. Whistleblowing: yes). CONSISTENT.
- CH-13: Applied to daily life. Correctly strict ("most claimed Mode B cases fail at condition 4 or 5"). CONSISTENT.
- CH-19: Adds sixth condition for rights (supermajority). CONSISTENT extension.
- CH-38: Uses Mode B to differentiate from pure utilitarianism. CONSISTENT.
- CH-39: Uses Mode B to differentiate from pure deontology. CONSISTENT.
- CH-42: Mode B requires judgment, which virtue ethics provides. CONSISTENT.
- CH-44: Mode A/B reaches same conclusions as natural law absolutes in practice. CONSISTENT.
- CH-48: Oath clause restates Mode A discipline. CONSISTENT.

**Verdict: NO CONTRADICTION.** Mode B is the single most consistently applied concept in the entire book. No chapter uses it more loosely than CH-10 defines it. No chapter expands the conditions. This is a major strength of the manuscript.

---

## 3D. Tone Audit

### CH-01: "The Third Way -- Why We Need a New Moral System"

**Tone:** Confident, ambitious, rhetorically strong. Opens with a sweeping narrative ("We are heirs to a catastrophe") that sets stakes high.
- **Jargon without payoff:** None. Technical terms (Nash equilibrium, game theory) are introduced with plain-language explanations.
- **False modesty:** None. The chapter is refreshingly direct about its ambition ("we are trying to build the best available moral system").
- **Contempt for rivals:** NONE. The treatment of theism is notably respectful ("Its track record includes hospitals, universities, abolitionist movements... Anyone who dismisses it as mere superstition hasn't studied it"). Nihilism is also treated seriously.
- **Emotional appeals without argument:** The opening narrative is emotionally engaging but serves an argumentative purpose (motivating the seven specifications). ACCEPTABLE.
- **Overall:** Strong opening chapter. Tone is appropriate.

### CH-24: "Policy Evaluation -- How to Think About Political and Economic Issues"

**Tone:** Methodical, practical, deliberately non-partisan.
- **Jargon without payoff:** LOW RISK. Introduces "Hayekian knowledge test" and "Pigovian fit test" as named concepts, but explains both thoroughly.
- **False modesty:** None. The chapter is confident about its method while explicitly building in humility (Step 7: "Decide with humility").
- **Contempt for rivals:** None detected. Both left and right policy positions are treated with equal analytical rigor in the case studies.
- **Emotional appeals without argument:** None. This is the most analytical chapter in the book.
- **FLAG [LOW SEVERITY]:** The Sowell epigraph ("The first lesson of politics is to disregard the first lesson of economics") could read as signaling a libertarian lean. The chapter content is balanced, but the epigraph choice may prime some readers.

### CH-36: "Against Divine Command Theory"

**Tone:** Respectful but firm. This is a critical test for "contempt for rivals being steel-manned."
- **Steel-manning quality:** EXCELLENT. The chapter devotes 7 full paragraphs to the strongest DCT arguments, including Adams's Modified DCT, the argument from moral knowledge, the argument from moral motivation, the historical argument, and the argument from ultimate meaning. Each is presented in its most sophisticated form.
- **Contempt for rivals:** NONE. Explicit anti-contempt language: "These are serious arguments. A dismissive response is unworthy of them." Also: "The chapter's conclusion is not that DCT is unintelligible or that its adherents are foolish."
- **Jargon without payoff:** None. The Euthyphro dilemma is explained from scratch.
- **Emotional appeals without argument:** None detected. Every critique is argued.
- **Overall:** Model chapter for adversarial engagement. Sets the standard for Book VIII.

### CH-42: "Against Virtue Ethics (Without Telos)"

**Tone:** Collegial, more sympathetic than adversarial.
- **Steel-manning quality:** EXCELLENT. Aristotle's ergon argument, the six key claims, MacIntyre's contemporary revival -- all presented with substantial direct quotation and genuine appreciation.
- **Contempt for rivals:** NONE. The chapter opens by acknowledging "the framework has absorbed significant elements of virtue ethics" and lists seven specific debts.
- **Jargon without payoff:** LOW RISK. Uses "ergon," "eudaimonia," "phronesis," "phronimos" -- all explained.
- **Emotional appeals without argument:** None.
- **FLAG [LOW SEVERITY]:** The chapter title "Against Virtue Ethics (Without Telos)" is slightly misleading. The chapter is more "engagement with and partial absorption of" than "against." The content is honest; the title undersells the synthesis.

### CH-45: "The Synthesis -- What We Take From Each"

**Tone:** Generous, integrative, intellectually humble.
- **Jargon without payoff:** LOW. The chapter uses many tradition-specific terms (eudaimonia, phronesis, junzi, dukkha, ubuntu, li, ren) but explains each.
- **False modesty:** BORDERLINE. The chapter's framing ("a framework claiming to be the 'best possible moral system' must actually absorb the best available insights from everywhere") is honest rather than falsely modest, but the sheer volume of debts acknowledged could read to some as excessive hedging. This is a judgment call.
- **Contempt for rivals:** NONE. This is the chapter where rivals are most generously treated.
- **Emotional appeals without argument:** None.
- **FLAG [LOW SEVERITY]:** The chapter is long and may read as an inventory rather than an argument. Each "debt" section follows the same structure (numbered insights, then "what we do not take"). The repetitive format serves clarity but may fatigue the reader.

### CH-48: "The Oath of the Rational Agent"

**Tone:** Solemn, personal, deliberately elevated.
- **Jargon without payoff:** NONE. Every technical term (epistemic duty, valence axiom, Mode A/B, etc.) is explained in plain language in the "In practice" sections.
- **False modesty:** None. The oath is direct and specific.
- **Contempt for rivals:** Not applicable (not an adversarial chapter).
- **Emotional appeals without argument:** BORDERLINE. The oath format is inherently emotional/performative rather than argumentative, but each clause explicitly references its grounding chapter. The Blake epigraph ("He who would do good to another must do it in Minute Particulars") is well chosen.
- **FLAG [MEDIUM SEVERITY]:** The oath structure risks seeming cultish or self-important to a skeptical reader. The chapter partially addresses this ("The oath is not a loyalty pledge. It does not require the reader to agree with every argument in the book."), but the twelve-clause structure with Roman numerals could still trigger this reaction. Consider whether a brief additional paragraph acknowledging this concern would help.

---

## Summary of Findings

### Severity Counts
- **HIGH SEVERITY:** 0
- **MEDIUM SEVERITY:** 3
  1. The twelve virtues list omits explicitly moral virtues (courage, justice, compassion), creating a gap in the virtue ethics engagement (3A)
  2. POS-P06 Registry description ("vestigial instinct to overcome") is more dismissive of retribution than CH-22's actual treatment (3B)
  3. Applied economic chapters (CH-24, CH-27, CH-30) read as more utilitarian than the foundational architecture warrants -- distinction between "CBA as tool" and "being utilitarian" could be sharper (3C)
- **LOW SEVERITY:** 10 (various terminological sparseness and minor accessibility issues; see individual flags above)

### Overall Assessment

The manuscript demonstrates **exceptionally strong terminological and positional consistency** across 47 chapters. The core architectural concepts (Mode A/B, valence axiom, Moloch, mechanism design, coordination failure) are used with near-perfect fidelity throughout. No genuine argument contradictions were found. The four potential contradiction vectors tested (utilitarian reasoning, rights strength, veil of ignorance, Mode B consistency) all resolved into nuanced-but-coherent positions rather than actual contradictions.

The three medium-severity findings are all addressable through targeted revisions:
1. Update POSITION_REGISTRY.md entry for POS-P06 to match CH-22's more nuanced treatment of retribution.
2. Add a brief note in CH-24 (or CH-25) explicitly situating cost-benefit analysis within the Mode A/B and rights framework, to prevent misreading the economic chapters as purely utilitarian.
3. Consider whether the twelve virtues list (CH-11) should be expanded to include moral (not just epistemic/instrumental) virtues, or whether the book should explicitly address why it does not.

The tone audit found no instances of contempt for steel-manned rivals, no significant jargon-without-payoff problems, and no emotional appeals substituting for argument. The overall tone is serious, honest, and appropriately confident.
