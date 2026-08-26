# The Introduction Volume + Audiobook: A Co-Design Spec

**Premise:** this is not Volume I of the professional set. This is the book that makes someone *want* the framework — the on-ramp. Target ~80,000 words, ~300 print pages, ~9.5 hours of audio, 18 chapters.

**The governing constraint, stated first:** Miso TTS has no SSML layer. It is a CSM-style neural model conditioned on text plus prior audio; there is no markup to control emphasis, pause, or pitch. Prosody comes from two places only — **how the sentence is written**, and **what audio you feed back as context**. That collapses "write the book" and "design the audiobook" into a single job. You are not writing prose and then narrating it. You are writing prosody directly.

Everything below follows from that.

---

# Part I — The Book

## 1. Structural inversion: lead with the trap, not the ground

The current manuscript runs foundations → diagnosis → architecture → applications. That is the systematizer's order, and it is the worst available order for a reader who does not yet care. Chapter 2 of a general-audience ethics book cannot be Bayesian epistemology.

Lead with **Moloch**. It is the most vivid material you have, it requires zero metaethical commitment to accept, and it reframes something every reader has personally experienced: *everyone hates this, everyone keeps doing it, nobody chose it.* That earns the credit you then spend on "why does suffering matter," which is the harder sell and which the reader will now be asking on their own.

Sandel's *Justice* does exactly this. So does Glover's *Humanity*. The problem comes first; the machinery arrives when the reader has felt the need for it.

## 2. The arc

**Prologue — "The Thing Nobody Chose"** (~2,000 words)
A single concrete case, small and real, where the reader knows something is wrong and cannot say why. Not a philosophical thought experiment. Something with a name, a place, and a date. End on the question the book will answer.

**Part One — The Trap** (4 chapters, ~18,000 words)
1. *Everyone Hates This* — the commons, the arms race, the race to the bottom. Coordination failure as the thing that produces suffering nobody intends.
2. *The Shadow of the Future* — Axelrod, the four properties, why cooperation is possible without anyone being good.
3. *Eight Rules from a Spanish Water Court* — Ostrom, Valencia, mechanism design. What actually works.
4. *Morality as Technology* — the payoff. Rules, reputation, punishment, and honor are not arbitrary cultural residue; they are engineering.

**Part Two — The Ground** (3 chapters, ~14,000 words)
By now the reader is asking: fine, but why should I care about the harm my defection causes? Now, and only now, the metaethics.
5. *The Dentist's Drill* — the axiom, argued as phenomenal value realism. What it is like to be in pain, and why the badness is not a coat of paint on the sensation.
6. *Whose Suffering* — impartiality derived from the iterated game, not asserted from the axiom. The unstable-Schelling-point argument for the expanding circle.
7. *What I Don't Know* — consciousness, free will, our own blindness. The degradation tiers, written in plain language: here is what survives if I am wrong about the metaphysics.

**Part Three — The Architecture** (4 chapters, ~18,000 words)
8. *The Fence in the Field* — why rules beat calculation for agents like us.
9. *The Nazi at the Door* — the override, and why "the stakes are high" is not enough.
10. *Three Gates* — the procedural safeguards. **This chapter carries your single most original contribution and should be the best-written chapter in the book.**
11. *Firmware* — the virtues, and why humility is load-bearing.

**Part Four — The Life** (4 chapters, ~18,000 words)
12. *Tuesday Morning* — the daily algorithm, rendered as a day rather than a flowchart.
13. *Love Is an Iterated Game (And That's Not an Insult)*
14. *Building Purpose Without a Script*
15. *Suffering, Death, and What the Stoics Got Right*

**Part Five — The Scale** (2 chapters, ~10,000 words)
16. *Institutions That Can Be Wrong* — error-correction primacy, separation of powers, subsidiarity. One chapter, not eight.
17. *Prices Are Sentences* — Hayek, Pigou, Ostrom, the capability floor. One chapter, not six.

**Coda — What This Doesn't Solve** (~3,000 words)
Population ethics. The no-self problem. Where the author's own priors probably distorted the argument. The last thing the reader hears should be the thing that earns the most trust.

Eighteen chapters at ~4,300 words averages 30 minutes of audio each — close to ideal audiobook chapter length, and it means every chapter is one commute.

**Everything cut** — the eight political chapters, six economic chapters, nine rival-system chapters, the syllabus, the Oath — goes to Volume II and Volume III. The introduction does not defeat rivals. It makes the reader want to see the rivals defeated, and tells them where that happens.

## 3. Title

*The Manual of Harmonious Rationality* is working against you three ways. "Manual" promises a reference document, which is exactly the register that damaged the current prose. "Harmonious" reads as spiritual-adjacent. And the whole phrase describes the author's project rather than the reader's problem.

Naming rule: a general-audience ethics title should name **the reader's problem or the book's central image**, not the system. *Justice*. *Being Good*. *The Righteous Mind*. *What We Owe to Each Other*. *Humanity*.

Candidates worth testing: *The Thing Nobody Chose*. *Everyone Hates This*. *The Physics of Trust*. *Three Gates*. Subtitle carries the system name — "…: an honest moral framework for people who don't believe in cosmic authority" or similar.

## 4. Prose specification

The current draft is written in what I'd call **framework-document register**. It is competent and it is not a book. Specific symptoms, all present:

- Section headers every ~500 words
- "Summary" and "What This Chapter Established" closers
- Nested bullets and numbered conditions carrying the primary exposition
- The institutional "we"
- Quotations dropped in as authority-decoration, attributed after the fact
- Almost no scenes: no named individuals doing things in places at times
- Uniform high confidence across claims of wildly different strength
- Persistent tricolon rhythm and "not X, but Y" construction
- Signposting sentences ("Let us be precise about what we are trying to build")
- Abstract nouns as sentence subjects, throughout

### The rules

**Open every chapter with a case, never a thesis.** A person, a decision, a specific difficulty. The argument emerges from the case.

**One argument per chapter**, statable in a single sentence you could say out loud. If you can't, the chapter is two chapters.

**Voice objections as people, not as headers.** Not "Objection 1: the egoist reply." Instead: a named interlocutor who says the thing, and gets a fair hearing, and is answered. This is what steel-manning looks like in prose rather than in outline.

**Delete every summary section.** All of them. If an argument requires a recap, it was built wrong. In audio they are actively harmful — the listener hears the same content twice in ten minutes and starts skipping.

**One list per chapter maximum. Zero is better.** This is the hardest rule and the most important. The five Mode B conditions and the three gates **must be converted to prose.** A listener cannot hold a nested five-item list; a reader skims it. Prose forces you to explain why each condition follows from the last, which is information the list currently hides.

**First person singular for judgment calls.** "I think the fourth condition is the one doing the real work, and I'm less sure about the fifth" is stronger and more credible than "the framework holds." The institutional "we" is evasive, and readers hear it as evasive.

**Concrete particularity quota:** every chapter contains at least one real person, named, doing something, somewhere, at a stated time. Elinor Ostrom in Valencia. Axelrod's tournament and the people who submitted entries. Chesterton's fence in an actual field.

**Modulate confidence audibly.** The draft states the axiom, the Mode B conditions, and the minimum-wage literature at identical pitch. Real ethics prose varies: *I'm confident about this. I'm much less sure here. I don't know, and neither does anyone.*

**Break the rhythm habits.** The tricolon is everywhere in the draft. In print it reads as slightly overwrought. In TTS it becomes an audible tic within twenty minutes, because the model will render the same cadence every time.

### Models to study, and what to take from each

| Book | Take |
|---|---|
| Sandel, *Justice* | Case-first chapter openings; how to make a dilemma feel urgent in two pages |
| Blackburn, *Being Good* | Compression — a whole metaethics in 150 pages without condescension |
| Glover, *Humanity* | Moral weight through historical particularity rather than assertion |
| Williams, *Ethics and the Limits of Philosophy* | How to concede hard and stay persuasive |
| Nagel, *The View from Nowhere* | Sentence-level clarity on genuinely difficult material |
| Appiah, *The Honor Code* | Narrative and argument braided rather than alternating |
| Parfit, *Reasons and Persons* | Numbered cases done right, when you must use them |

---

# Part II — The Audiobook

## 5. What Miso actually gives you, and what it doesn't

From the model card and repo:

- 8B parameters, Sesame CSM-style: Llama 3.2-ish backbone plus an autoregressive audio decoder
- Mimi tokenizer, 32 codebooks, **max sequence length 2,048**
- Conditions on prior audio via `Segment(speaker, text, audio)` context
- One-shot voice cloning from a prompt sample
- `max_audio_length_ms` per call
- bfloat16 default, CUDA-oriented reference implementation
- SilentCipher watermarking on by default
- English-focused

Three consequences dominate the design:

**No SSML.** Covered above. The text is the score.

**Short generations.** 2,048 positions are shared across text tokens, context, and audio frames. You are rendering **sentences and short paragraphs**, roughly 10–25 seconds each — not chapters. Plan the pipeline around thousands of small calls.

**Audio conditioning is the continuity mechanism, and it is the whole game.** This is the feature that separates a listenable synthetic audiobook from an unlistenable one. See §7.

## 6. Voice design

**Record the anchor yourself.** A book whose thesis is intellectual honesty should be narrated in the author's voice, even synthetically. It is also the better product — a cloned real voice with real idiosyncrasy beats a generic sample.

Anchor prompt requirements:
- 45–60 seconds, read from the actual manuscript at the actual target pace
- Same microphone, same room, no compression, no EQ, no noise reduction
- Register matched to output: read it the way you want the book to sound, because the model copies register, not just timbre
- Slightly slower than conversational. Audiobook pace is ~150 wpm; conversation is ~180

**Record three anchors, not one:**
1. **Narration** — the default voice, ~90% of the book
2. **Quotation** — marginally slower, marginally lower. Every block quote from Chesterton, Rawls, Dawkins, Ostrom renders in this voice. This solves the "where does the quote end" ambiguity that ruins most TTS nonfiction.
3. **Part opening** — slower, more deliberate, for part titles and the prologue

Assign distinct `speaker` IDs and keep separate anchor segments per voice.

## 7. The rendering pipeline

The single most important design decision:

**Rolling audio context with a fixed anchor.** Every generation call receives a context list of:
- position 0: the original anchor segment (never changes)
- positions 1–3: the last two or three segments you just generated

The anchor prevents slow timbre drift over ten hours. The rolling window preserves pitch, pace, and breath continuity across chunk boundaries — without it you get an audible seam every fifteen seconds, which is the classic failure mode of synthetic audiobooks and the reason most of them are unlistenable.

**Reset the rolling window at every chapter boundary.** Keep the anchor; drop the accumulated recent context. This stops drift compounding across the whole book.

**Chunking rule:** split on sentence boundaries, then merge adjacent sentences up to a ~200-character / ~15-second budget, never merging across a paragraph break. Paragraph breaks are structural and should be seams by design.

**Assembly:**

| Boundary | Silence |
|---|---|
| Sentence within paragraph | 350 ms |
| Paragraph | 700 ms |
| Section break | 1.2 s |
| Chapter end | 2.5 s |

**Master to:** −18 to −20 LUFS integrated, true peak ≤ −3 dBTP, 44.1 kHz. (ACX-style spec; verify against whichever distributor you actually use.)

**Add a room-tone bed at roughly −60 dBFS.** Neural TTS output is unnaturally clean, and over nine hours the absolute silence between phrases becomes fatiguing in a way listeners feel but can't name. A near-inaudible noise floor fixes it.

## 8. The audio script is a separate manuscript

Do not pipe print text into the renderer. Maintain a parallel audio edition. Differences:

- **Numbers spelled in spoken form.** "Nineteen seventy-one," not "1971." "Chapter nine," not "Ch. 9."
- **No footnotes, no cross-references, no parenthetical citations.** All of it moves to a companion PDF the listener can download. Say "as I argued earlier" — never "see Chapter 12."
- **Restate antecedents.** A listener cannot glance back. "Ostrom's third principle — the one about who gets to write the rules —" rather than "her third principle."
- **Lists converted to prose.** Already required by §4; here it is mandatory rather than merely advisable.
- **Chapter handoffs at the start of the next chapter**, one sentence, never as end-of-chapter summaries.
- **Homograph disambiguation** by rewording (see §9).
- **Pronunciation respellings** substituted in the render text only (see §9).

Version the two manuscripts together so a print edit never silently diverges from the audio.

## 9. The two failure classes that will actually bite you

**Proper nouns.** With no phoneme markup, your only lever is respelling the render text. This manuscript is a minefield: Moloch, Hayek, Nozick, Rawls, Ostrom, Schelling, Nietzsche, Kahneman, Taleb, Axelrod, MacIntyre, Nussbaum, Sen, Coase, Gauthier, Scanlon, Korsgaard, Sidgwick, Parfit, Frankish, Dancy, Dworkin, Sowell, Caplan, Pigovian, Euthyphro, Thomistic, Chesterton, *ren*, *anātman*, Ubuntu, *tsuyoku naritai*, Tribunal de las Aguas.

Process: render each term in isolation first, listen, build a respelling table (print form → render form), apply as a substitution pass. Keep the table in version control — it is a real asset and it will be wrong the first three times.

**Homographs.** The top failure class in every TTS audiobook. Auto-scan the audio script for: *lead, read, live, wound, bow, close, present, object, subject, contract, refuse, minute, tear, sow, use, house, abuse, separate, moderate, deliberate, invalid, resume, content, conduct, entrance, desert.*

Note that *deliberate*, *moderate*, *separate*, and *object* appear constantly in this manuscript — the deliberation period, moderate confidence, separateness of persons, treating persons as objects. Every instance needs checking. Where a respelling sounds wrong, reword the sentence instead.

## 10. QC: build the ASR diff before you render anything

Nine and a half hours of audio is roughly fifteen hours of human QC with rewinds, and autoregressive TTS drops and hallucinates words at a low but nonzero rate that a tired listener will miss.

**Run Whisper over every rendered segment and diff the transcript against the source text.** Flag any mismatch above a small edit-distance threshold for human review. This catches dropped words, hallucinated words, number misreadings, and most homograph errors automatically, and it cuts QC from fifteen hours to two or three.

This is the highest-value engineering step in the entire project. Build it first, before you render a single chapter.

Then do a human listen-through anyway, at 1.0x, on headphones, for the things ASR can't catch: prosodic seams, wrong emotional register, a quotation that doesn't sound like a quotation, and the tricolon tic.

## 11. Compute

Miso 8B in bf16 is roughly 16.4 GB of weights before activations, and the reference implementation is CUDA-first. Your M4 Pro's 24 GB unified memory is borderline at best and the MPS path is unproven.

Recommended split:
- **Local (Mac):** script preparation, chunking, the substitution tables, assembly, mastering, QC listening. All CPU work.
- **Rented GPU (L40S / A100 / 4090):** anchor-prompt iteration, then the batch render. This is a one-shot job — a full book render is plausibly 8–20 GPU-hours depending on realtime factor, which is tens of dollars, not thousands.

Render one chapter end-to-end and QC it completely before committing to the full run. You will change the anchor prompt at least twice.

## 12. Disclosure

Output is SilentCipher-watermarked by default. **Do not strip it.** Disclose synthetic narration in the front matter, in the retail metadata, and in the first thirty seconds of the audiobook itself.

This is not just compliance. A book arguing that epistemic honesty is a moral duty cannot quietly ship an undisclosed synthetic narrator; the first reviewer to notice will make that the story, and they will be right to. Handled openly — a short author's note explaining the choice — it becomes a point in the book's favor instead.

Distributor policies on AI narration differ and have been changing quickly. Verify current terms with whichever platform you're using before you commit to the render.

## 13. The gateway edition

Release **Parts One and Two only** — roughly 20,000 words, ninety minutes of audio — as a free standalone primer. That is the actual answer to "introduce someone to this framework." Nobody is introduced by 300 pages. They are introduced by ninety minutes that reframes something they already experience, ends on the axiom, and tells them where the rest lives.

---

## Build order

1. Write the ASR-diff QC harness. (It shapes every downstream decision.)
2. Draft the prologue and Chapter 10 (*Three Gates*) to establish the prose register at both extremes — narrative and technical.
3. Record and iterate the three anchor prompts against those two chapters.
4. Render Chapter 10 end to end, master it, QC it fully. Fix the pipeline.
5. Write the rest to the register those chapters set.
6. Batch render, assemble, master, full listen-through.
7. Cut the gateway edition from the finished master.
