# Book Data — Repository Map

**Active project:** an ~80,000-word general-audience introduction to the moral framework, plus (later) a Miso TTS audiobook. Everything current lives in `book-production/`.

```
book-production/      ← THE ACTIVE PROJECT (start at book-production/PLAN.md)
  spec/               production bible, style bible, voice spec, chapter briefs, audio spec
  canon/              CANON.md + POSITIONS.md + GLOSSARY.md — source of truth (frozen)
  research/           per-chapter evidence + case packets
  manuscript/         drafts per chapter; frozen/ = immutable finals
  reviews/            gate reviews, decisions logs, DEVIATIONS.md (proxy protocol)
  audio/              lexicon/homograph tables, Miso setup, scripts (generated per freeze)
  tools/              lint, burstiness, asr_diff, render, assemble, build_pdf, RUNBOOK
  build/              assembled PDF lands here (build/book.pdf)

Files/                source library (34 works) — used by Researcher/Verifier
MisoTTS/              cloned MisoLabsAI/MisoTTS inference repo (code only, no weights)
archive/v1/FirstEdition_Backup/  first-edition chapter backup (anti-corpus source)

archive/
  v1/                 the original 49-chapter book: chapters, bible, index, registry,
                      reviews, context, builds (PDF/HTML), Kokoro audiobook, old tools,
                      old CLAUDE.md
  planning/           superseded planning docs (old workflow, review strategy,
                      scrapped second-edition style guide + directives)
  NewPlan/            original files.zip extraction
  files.zip           the delivered production system, as received
```

**v1 status:** the 207,000-word draft is retired as a publication target. It remains the content quarry (arguments, quotes, structure) and the anti-corpus (examples of the register the new book must not have). Nothing in it should be edited.
