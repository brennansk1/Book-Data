# Interim model corpus — read this before trusting these files

This is a **stand-in**, not the real thing.

`VOICE.md` §3 specifies the model corpus as passages from Sandel (*Justice*), Glover (*Humanity*), Blackburn (*Being Good*), Williams (*Ethics and the Limits of Philosophy*), Appiah (*The Honor Code*), and Nagel. None of those six books are available locally as of this writing (2026-08-05). Rather than block drafting on their acquisition, this directory substitutes the strongest trade-nonfiction prose we do have on hand, chosen to model the same six qualities the spec asks for:

| File | Source | Models (per VOICE §3) | Stands in for |
|---|---|---|---|
| `interim-1.md` | Haidt, *The Righteous Mind*, Ch. 1 | case-first opening | Sandel |
| `interim-2.md` | Galef, *The Scout Mindset*, Ch. 1 | historical particularity | Glover |
| `interim-3.md` | Dawkins, *The Selfish Gene*, Preface to First Edition | sentence-level clarity | Nagel |
| `interim-4.md` | Galef, *The Scout Mindset*, Ch. 14 | conceding | Williams |
| `interim-5.md` | Haidt, *The Righteous Mind*, Ch. 9 | narrative and argument braided | Appiah |
| `interim-6.md` | Dawkins, *The Selfish Gene*, Ch. 2 | compression without condescension | Blackburn |

**Why these three books.** Haidt and Galef are contemporary trade nonfiction written for an intelligent general reader on hard, contestable material — the same register STYLE_BIBLE §1 asks for — and both authors write in first person, open chapters with cases, and concede points visibly. Dawkins was added because *The Selfish Gene* is the closest available match for Nagel/Blackburn-style compression: technical material rendered in short, plain sentences with no loss of precision. None of the three is a moral-philosophy trade book in the specific register Sandel or Appiah write in, which is the real gap this interim corpus does not close — it can model sentence-level and structural moves, but not the specific cadence of a philosopher arguing an applied ethics case for a lay audience.

**Rebuild when the real books arrive.** When Sandel, Glover, Blackburn, Williams, Appiah, and Nagel are available in `Files/`, extract the specified passages, replace `interim-1.md` through `interim-6.md` (or add alongside and retire these), and rerun `tools/burstiness.py --build-reference`. Until then, every Drafter should treat this corpus as directionally useful for structure and sentence rhythm, and should not assume it captures the specific philosophical register the spec actually asks for.

**Copyright note (per VOICE §3).** These passages are internal reference only. Nothing from them appears in the manuscript, and the Verifier checks for it. This applies to the interim corpus exactly as it will apply to the eventual Sandel/Glover/Blackburn/Williams/Appiah/Nagel corpus.

**Extraction method.** All six passages were extracted from local EPUB files already unpacked in `Files/Righteous_Mind_extracted/` and `Files/Selfish_Gene_extracted/` (the `Scout_Mindset_extracted/` XHTML was used for the Galef passages), stripped of HTML markup, and trimmed to natural paragraph or section breaks within the 800–1,500 word range VOICE §3 specifies. No passage was edited beyond whitespace normalization and dropping inline footnote markers.
