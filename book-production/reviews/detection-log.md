# Detection Log

Patterns identified by red-team/detection passes that must feed back into VOICE/IDIOLECT. Frozen-chapter instances get reviewed at each Part's Gate 6 panel; unfrozen chapters must comply immediately.

**DL-1 (2026-08-06, ch-01 red team) — The confession-priming template.** Prologue ("the kind of thing a person is tempted to leave out"), ch-10 ("the admission, and it isn't a comfortable one"), ch-01 draft ("isn't a flattering admission") all announce the costly admission before making it. Rule: the announcement move may appear AT MOST ONCE per Part; other chapters enter the admission cold, mid-paragraph, or after the fact. Ch-01 must fix now (unfrozen). The prologue and ch-10 instances stand until the Part One Gate 6 panel; if flagged there, vary under freeze-change discipline.

**DL-2 (2026-08-06, ch-01 red team) — Negation-budget gaming.** Running the budgeted cluster twice on the same subjects (once affirmative "were reasonable," once negative "weren't being unreasonable") games the letter of the budget. Rule: the cluster's subjects get ONE treatment, in one polarity, per chapter.

**DL-3 (2026-08-06, ch-02 voice review) — Interlocutor-placement template.** Three chapters running (ch-01, ch-10, ch-02) have the named friend voice the central objection in the chapter's back third. Rule: vary the beat. Options — objection arrives FIRST and the chapter answers it (ch-03 candidate); objection distributed across the chapter as running interruptions; objection never quoted but paraphrased and steel-manned; the friend AGREES and the writer argues against their agreement. At most one late-objection chapter per Part going forward.

**DL-4 (2026-08-06, ch-02 red team) — Second-order tells: compliance narrated as content.** Three new rules: (a) never narrate a VOICE-checklist requirement while performing it ("I'm not going to get into X" is an omission; "I could be tidy but I'm choosing honesty" is a flourish — one per chapter maximum, zero preferred); (b) the word "flattering/unflattering" is BANNED book-wide (5 occurrences across ch-10/ch-02 made it a fingerprint); (c) plain-band quota may not be cashed with "thing" more than 4x/chapter; the idiolect's own words ("unreasonable," "climbing") count first. Named omissions: exactly ONE per chapter.

**DL-5 (2026-08-06, ch-02 red team) — Correspondent device template.** Profession + one quirky detail + one pushback quote is now a visible pattern (Priya, Marisol; Nate the outlier). Future correspondents must vary along at least two axes: relationship depth (family member, mentor, adversary), interaction mode (they write back; the letter reports an argument already lost; the correspondent is dead and the letter is unsendable), and what they contribute (a case the writer didn't have; a correction the writer accepts). No new correspondent may be introduced with profession+quirk in the same paragraph.

**DL-6 (2026-08-06, ch-03 red team) — The transit-anchor confession template.** Four units running stage the costly admission the same way: a solitary writer in transit or at rest (midnight kitchen / library carrel / airplane seat / late hallway) + one physical prop + fast-judgment-then-slow-correction arc. Rule: this staging is retired for the rest of the book. Admissions may arrive: mid-conversation (someone present, contradicting); in the act of being wrong in real time; retrospective without any scene; or discovered in the writer's own old files/notes. Also: hyper-precision on unfalsifiable details (seat numbers) with vagueness on checkable ones is itself a tell — invert it (name the checkable, drop the ornamental).

**DL-7 (2026-08-06, orchestrator) — The negation family is now machine-detectable.** Reviewers caught the
"negation-and-correct" gesture in five consecutive chapters, each time wearing a syntax the plain
`not X but Y` regex missed ("not X — it's Y", "X isn't Y. It's Z.", "wasn't being X"). `tools/lint.py`
now counts the whole family as `negate_correct` (target ≤4, hard fail >8), so the budget in
IDIOLECT.md is enforced at Gate 2 instead of being rediscovered at Gate 3 every chapter.
Retroactive measurement of the frozen set: ch-01 = 5 (warn), ch-02 = 4, ch-03 = 4, prologue = 4,
ch-10 = 1. Ch-01's excess is a soft warn on a frozen chapter — NOT reopened; flagged for the
Part One detection panel to judge alongside the human read.

**DL-8 (2026-08-06, ch-04 red team) — The anchor ARC, not just its staging.** DL-6 retired the transit
confession (kitchen/carrel/cabin + prop). Ch-04 complied on staging and kept the arc exactly:
fast judgment -> slower checking -> correction reported. That arc is IDIOLECT's named weakness, so it
is SUPPOSED to recur as a trait — but it must stop being the same STORY every time. Required
variation from here: at least half the remaining anchors must break the arc. Options: an admission
with no correction (the writer still hasn't fixed it); a correction that came from someone else and
stung; an admission of something the writer would do again; a cost paid with no lesson attached.
An anchor whose last beat is "and then I understood" is now the exception, not the default.

**DL-9 (2026-08-06, ch-04 red team) — Two verbatim fingerprints and an ending habit.**
(a) "than the [argument/chapter] strictly needs" appears in ch-01, ch-03 and ch-04 — retire the phrase.
(b) Ending on admitted uncertainty ("I don't know yet. I'm not sure anyone does.") is attested in
ch-03, ch-04 and ch-10. It is honest, and it is now a habit: at most one chapter per Part may end
that way, and Part One's allowance is spent. Other chapters end on the image, the case, the reader's
own position, or a flat declarative the chapter has earned.
(c) The disclosure-preempting reflex ("I should flag this, because you'd ask anyway") is DL-4a's
compliance-narration wearing a new coat: one per chapter, maximum.

**DL-10 (2026-08-06, ch-04 voice curator) — A quality metric manufactured a template.** Six of six
units close on the same construction: "I'm confident about X. I'm much less sure about Y." The cause
is structural, not lazy drafting — STYLE_BIBLE requires >=2 confidence modulations per chapter, and
the requirement could be satisfied entirely in the closing paragraph, so it was, every time. The
metric produced the tell it was meant to prevent.

Fix has two halves:
(a) MECHANICAL — lint.py now reports `conf_mods_in_tail_pct`, the share of modulations landing in the
final fifth (target <=60%). Retroactive measurement: prologue 100% (warn), ch-03 100% (warn),
ch-10 66.7% (warn), ch-01 50% (ok), ch-02 33.3% (ok).
(b) EDITORIAL — calibration belongs where the uncertainty actually lives in the argument, not banked
at the close as a signature. No chapter's final paragraph may carry a confidence modulation unless
the chapter's whole subject is uncertainty (ch-07).

The three frozen warns are NOT being reopened for a soft metric mid-run; they go to the Part One
detection panel with this note, where the same closing formula appearing in three of five frozen
units is the panel's most likely single finding.

**General lesson, worth carrying:** every hard requirement in STYLE_BIBLE is a candidate for this
failure. A metric that can be satisfied in one place will be satisfied in that place. When a
reviewer finds a repeated device, check first whether a rule is causing it.
