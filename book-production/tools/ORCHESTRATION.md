# Who runs what

The per-chapter loop is proceduralized enough to be run by a Sonnet orchestrator (the "line
producer"). Opus is reserved for a short, defined list of judgment calls. This is a cost decision
grounded in what actually caught defects during Part One: every substantive catch came from Sonnet
subagents — the referee, the verifier, the red team. Opus earned its keep on rulings and patterns,
not on running the loop.

## The line producer (Sonnet) — runs the whole cycle

Per `tools/RUNBOOK.md`, for each unit in order:
1. Dispatch the researcher; log the Gate 1 pick using the packet's own ranking **unless an
   escalation trigger fires** (see below).
2. Dispatch Pass A, Pass B, Pass C. Confirm `claims.tsv` exists and every unsourced claim is marked
   CONJECTURE.
3. Run `lint.py`; fix hard fails directly with edits — never spawn an agent for a regex fix.
4. Dispatch Referee + Craft in parallel.
5. Dispatch one consolidated revision with a prioritized work order.
6. Dispatch the verifier against `claims.tsv`; apply the fixes it specifies.
7. Freeze, log `decisions.md`, update `concept-index.md`, rebuild the PDF, commit and push.
8. Run `mkaudio.py`; leave the `.todo.txt` for the batched audio pass at the end.

It also owns: the detection log (appending new DL rules when a reviewer names a repeated device), the
concept index, and keeping `spec/BRIEF.md` current when a DL rule is added.

## Escalate to Opus — do not decide these alone

1. **Any question about what the framework claims.** New canon rulings, or any conflict between a
   brief, the canon, and a chapter. These become `CANON_KEEPER_LOG` entries. (Precedent: CK-8, the
   answer to Street's pain-specific dilemma, needed a position taken, not a lookup.)
2. **Case selection where a wrong call would embed a factual or ethical error.** Specifically: a case
   whose underlying facts are contested (Anna Pou), a person whose misconduct would be laundered by
   sympathetic framing (Wakefield), a case commonly described backwards (Arkhipov was enforcing a
   rule, not breaking one), or a case involving a recently deceased or private individual.
3. **Any FAIL from the verifier that cannot be fixed by cutting or hedging** — i.e. where fixing it
   changes what the chapter argues.
4. **A reviewer finding that contradicts another reviewer**, or that would require reopening a frozen
   chapter.
5. **A repeated device found in three or more chapters.** These are usually caused by a rule rather
   than by lazy drafting, and the fix is often to change the rule (precedent: DL-10 — the style
   bible's confidence-modulation requirement was manufacturing the identical closing formula in six
   consecutive units).
6. **Anything that would alter the book's structure**: a chapter that won't fit its brief, a concept
   owed to a chapter that can't carry it, a Part that doesn't cohere.
7. **The Part-boundary detection panel result**, if any paragraph is flagged by three or more judges.

## Rule of thumb
If the decision is "which of these does the runbook say to do", it is the line producer's.
If the decision is "the runbook doesn't cover this" or "this changes what the book says", escalate.
When genuinely unsure, escalate — a wrong canon call propagates into every later chapter, while an
unnecessary escalation costs one short exchange.

## Showrunner (human) — unchanged
Anchors in his own voice, ratification of provisional freezes, the invented-correspondent decisions,
Ch. 7 and the Coda, and anything in `reviews/DEVIATIONS.md`.
