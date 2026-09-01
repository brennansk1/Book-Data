# The hardening loop — how to keep improving this system after the obvious work is done

## What actually worked, and why

Five passes ran over this framework in sequence: an internal strengthening pass, a rival audit, a
verdict battery, a welfare build-out, and a debate stress test. Each one found something the others
had missed, and the misses were not random:

| Pass | What only it found |
|---|---|
| Internal audit | POS-04 was asking one argument to do two jobs |
| Rival audit | the originality claim was unearned (Hare got there first) |
| Verdict battery | the ticking-bomb prohibition is contingent, not absolute |
| Welfare build-out | POS-06 was simply wrong — the framework is asymmetric |
| Debate stress test | leading with "the axiom is chosen" hands the room away |

**The lesson is not "try harder." It is that each pass applied a different KIND of pressure.** More
effort along one axis finds progressively less; a new axis finds something on its first attempt. So the
loop should be a *rotation of pressure types*, not a repetition of review.

## The rotation

Six lenses. Run one per cycle, in order, then start again. Never run the same lens twice in a row —
the second pass under the same pressure is where the yield collapses.

**1 · Internal audit.** Read the Registry's own `Known vulnerability` and `What would change my mind`
fields and try to close them. Cheapest, and it goes first because the system has already told you where
it is weak. *Yield so far: highest.*

**2 · Rival pressure.** Take one competing tradition in its strongest living form and ask where it beats
us. Rotate the tradition each cycle. The question is never "can we rebut it" but "what does it do better,
and can we take that." *This is where credit gets paid and originality claims get checked.*

**3 · Case pressure.** Run the machinery over cases and record verdicts. Alternate between the standard
battery (trolley, transplant, the murderer at the door) and cases with no settled intuition — novel
technology, novel institutions — where the framework cannot lean on agreement it hasn't earned.

**4 · Empirical audit.** *The one never yet run, and now overdue.* The framework rests on empirical bets:
that autonomy, competence and connection are load-bearing for sustained welfare; that the asymbolia
dissociation means what we say it means; that arbitrary exclusions carry higher maintenance costs. Each
is a claim about the world that could be false. Check whether the literature still supports them, and
whether anything has been overturned since it was cited.

**5 · Adversarial format.** Compress the system to a hostile live exchange. This is not a rhetoric
exercise — compression is a test. An argument that cannot survive being stated in thirty seconds usually
has a defect that the long version was concealing, and the debate pass proved it: the "chosen axiom"
problem was invisible in prose and fatal at speed.

**6 · Coherence sweep.** After every amendment, check that nothing published earlier now contradicts it.
This is the failure mode that nearly bit: the experience-machine verdict survived three commits after the
position it depended on had been rewritten. Now partly mechanical — `tools/canonlint.py`.

## Mechanise whatever a lens finds twice

The same principle that governs the prose pipeline governs this one. When a check keeps finding the same
class of defect, the check becomes a script and stops costing attention.

`tools/canonlint.py` is the first instalment. It verifies that every position states a vulnerability and
a falsification condition, that amendments aren't orphaned, that CANON §9's banned items haven't crept
back into frozen chapters, that every ruling names the chapters it affects, and that published verdicts
carry revision markers when the positions under them have moved. On its first run it found nine gaps
including the verdict-coherence failure above. Run it before every freeze.

**What it cannot do, and must never be mistaken for doing:** it does not evaluate an argument. It checks
that the system is keeping its own promises. That is a lesser thing, and it is the thing that fails first.

## Cadence

- **Coherence sweep + canonlint:** every chapter freeze. Minutes.
- **One rotating lens (1–5):** every Part boundary — five Parts, so most of a rotation across the book.
- **Full rotation:** before publication, and again before any second edition.

## The rule that matters most

**Log the defeat, not the fix.** Every pass here produced a Registry amendment *and* a stated cost:
Sidgwick's dualism is unclosed, the ticking-bomb prohibition is contingent, routing obligation through
institutions suits the comfortable, goods pluralism is an empirical bet that could fail. Those entries
are the asset. A framework whose registry only ever records improvements is not being audited; it is
being marketed, and the difference shows up the first time someone hostile reads it carefully.

The measure of a cycle is not how much stronger the system looks afterward. It is how much more precisely
it can now say where it is weak.
