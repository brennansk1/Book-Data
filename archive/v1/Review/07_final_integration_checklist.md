# Phase 7 — Final Integration Checklist

**Status:** PREPARED (awaiting Phase 6 completion)

---

## 7A. Planning Document Sync

| Document | Check | Status |
|----------|-------|--------|
| BOOK_INDEX.md | All 48 chapters listed, all marked DRAFTED or FINAL, titles match actual files | PENDING |
| BOOK_BIBLE.md | All 48 chapters have summary entries | DONE (agent completed) |
| POSITION_REGISTRY.md | All chapter refs correct (48-chapter numbering), confidence/vulnerability current | DONE (fixed in Phase 0+5) |
| DECISIONS.md | DEC-001 through DEC-006 present and current | DONE |
| OPEN_QUESTIONS.md | OQ-003 SUBSTANTIALLY RESOLVED, OQ-006 RESOLVED, remaining OQs current | DONE |
| REVIEW_STRATEGY.md | Exists and is current | DONE |

## 7B. Chapter Promotion

After Phase 6 edits are complete:
```bash
# Promote all chapters from Drafts/ to Chapters/
cp Book/Drafts/CH-*.md Book/Chapters/
# Promote front/back matter
cp Book/Drafts/PREFACE.md Book/Chapters/
cp Book/Drafts/TITLE_PAGE.md Book/Chapters/
cp Book/Drafts/BACK_MATTER.md Book/Chapters/
```

Then update BOOK_INDEX.md: change all 48 statuses from DRAFTED to FINAL.

## 7C. Front Matter Verification

| Component | File | Status |
|-----------|------|--------|
| Title Page | Book/Drafts/TITLE_PAGE.md | DRAFTED |
| Preface | Book/Drafts/PREFACE.md | DRAFTED |
| Table of Contents | Generated from BOOK_INDEX.md | PENDING (typesetting step) |

## 7D. Back Matter Verification

| Component | File | Status |
|-----------|------|--------|
| Position Index | Book/Drafts/BACK_MATTER.md (section 1) | DRAFTED |
| Key Terms Glossary | Book/Drafts/BACK_MATTER.md (section 2) | DRAFTED |
| Thinkers Engaged Index | Book/Drafts/BACK_MATTER.md (section 3) | DRAFTED |
| Notes on Position Registry | Book/Drafts/BACK_MATTER.md (section 4) | DRAFTED |
| Bibliography | NOT YET DRAFTED — generate from CH-47 syllabus + in-text citations | PENDING |

## 7E. Formatting Consistency Check

After Phase 6 edits, verify:
- [ ] All chapters use `# Chapter N:` as first line
- [ ] All chapters have `> *"quote"*` epigraph format
- [ ] All chapters have `## Summary` as final section before closing
- [ ] All block quotes use consistent `> *"text"*` formatting
- [ ] Cross-references use "Chapter N" format (not "CH-N" in body text)
- [ ] No duplicate epigraphs remain (3 were fixed; verify CH-11/CH-42 Durant paraphrase)

## 7F. Final Word Count

Run after Phase 6 to get definitive numbers:
```bash
cd Book/Chapters && for f in CH-*.md; do echo "$(echo $f | sed 's/\.md//') $(wc -w < $f)"; done
```

Target: ~190,000 words total. At standard typesetting (~250 words/page), this is ~760 pages.

## 7G. Fresh-Eyes Proofread

Per REVIEW_STRATEGY.md: a full read-through by a reviewer who has NOT been doing the substantive review. This catches what familiar eyes miss. 

Options:
1. Human reviewer reads the promoted Chapters/ files
2. A new AI agent reads all 48 chapters sequentially with instructions to flag: typos, grammatical errors, unclear sentences, formatting inconsistencies, passages that don't make sense on first read
3. Both (recommended)

## 7H. Sign-Off Record

After all checks pass:

| Check | Reviewer | Date | Sign-off |
|-------|----------|------|----------|
| Phase 0 Baseline | Claude | 2026-04-05 | COMPLETE |
| Phase 1 Structural | Claude (agent) | 2026-04-05 | COMPLETE, all issues resolved |
| Phase 2 Argument Integrity | Claude (3 agents) | 2026-04-05 | COMPLETE, FAILs fixed |
| Phase 3 Consistency | Claude (agent) | 2026-04-05 | COMPLETE, 0 contradictions |
| Phase 4 Citations | Claude (agent) | 2026-04-05 | COMPLETE, HIGHs fixed |
| Phase 5 Steel-man/Vulnerability | Claude (agent) | 2026-04-05 | COMPLETE, URGENT fixed |
| Phase 6 Prose | Claude (3 agents) | PENDING | IN PROGRESS |
| Phase 7 Final Integration | — | PENDING | — |
| Fresh-eyes Proofread | — | PENDING | — |

## Definition of Done (from REVIEW_STRATEGY.md)

The manuscript is ready for PDF conversion when:
- [x] Every chapter has passed Phases 1 through 5
- [ ] Every chapter has passed Phase 6 (prose editing) — IN PROGRESS
- [ ] Every planning document reflects final manuscript state
- [ ] Every chapter file is in Book/Chapters/ (not Drafts/)
- [x] Front matter drafted
- [x] Back matter drafted (except bibliography)
- [x] Every direct quote is verified (Phase 4)
- [x] Every HIGH-vulnerability position has in-chapter acknowledgment (Phase 5)
- [x] Every rival system steel-manned at recognizable level (Phase 5)
- [ ] Fresh-eyes proofread completed
- [ ] Errata track set up for Phase 8
