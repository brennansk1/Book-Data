# The Source Library — what is in `Files/`, and how to reach it

**Absolute path: `/Users/brennankelley/Desktop/Projects/Book-Data-main/Files/`**

It sits at the PROJECT ROOT, one level ABOVE `book-production/`. An agent whose working directory is
`book-production/` will not find it with a relative `Files/` path, and at least one researcher has
already concluded the library "does not exist anywhere on the filesystem" for exactly this reason.
**Always brief agents with the absolute path.**

`Files/` is gitignored (third-party copyrighted texts; 305 MB), so it is present locally and never
published.

## Extraction status

Every PDF here was tested with `pdftotext -f 40 -l 44` (five pages mid-book):

**Extracts cleanly (~12,000–16,000 chars / 5pp)** — use `pdftotext` and cite page numbers.
Rawls *A Theory of Justice* · Singer *Practical Ethics* · Parfit *Reasons and Persons* ·
Kant *Groundwork* · Aquinas *Summa Theologica* · MacIntyre *After Virtue* · Ostrom *Governing the
Commons* · Schelling *Strategy of Conflict* · Sowell *Basic Economics* and *A Conflict of Visions* ·
Sen *Development as Freedom* · Scott *Seeing Like a State* · Kahneman *Thinking, Fast and Slow* ·
Caplan *Myth of the Rational Voter* · Bueno de Mesquita *The Dictator's Handbook* · Simler & Hanson
*The Elephant in the Brain* · Gilligan *In a Different Voice* · Broodryk on Ubuntu · Confucius
*Analects*.

**Extracts, but noisy OCR — verify quotations against a rendered page image before printing.**
Axelrod *The Evolution of Cooperation* (~3,900 chars/5pp; the ch-02 and ch-03 verifiers both
re-derived the page offset independently before trusting it — do the same).

**Image-only, `pdftotext` returns nothing:**
- *Nicomachean Ethics* (Aristotle) — confirmed by test, and independently by the v1 project's own
  notes (MR-014). Two OCR attempts (ocrmypdf/tesseract) were killed before writing output and the
  effort was abandoned as not worth the time: **cite Aristotle by Bekker number** (the cross-edition scholarly standard) with wording from a named
  public-domain translation, naming the translation in the endnote. This is standard practice for
  classical texts and is the settled approach for this book, not a workaround.
- Adams *Finite and Infinite Goods* — image-only. Not needed by the current 19-unit outline.

**EPUBs** (Haidt *The Righteous Mind*, Galef *The Scout Mindset*, Dawkins *The Selfish Gene*,
Taleb *Antifragile*, Bostrom *Superintelligence*, Friedman *Machinery of Freedom*, the Federalist,
the Dhammapada): unzip and read the XHTML. Three are already extracted under
`Files/*_extracted/`.

## Standing warnings

- **Aristotle misattributions.** "Habit is second nature" is **Cicero**, not Aristotle. "We are what
  we repeatedly do; excellence, then, is not an act but a habit" is **Will Durant's 1926 paraphrase**,
  not a quotation from the *Ethics*. The v1 project caught the Durant error once already; do not
  reintroduce it. The genuine habituation passage is at Bekker 1103a32–1103b2.
- Anything not in this library goes on `research/SOURCES_NEEDED.md` rather than being reconstructed
  from memory.
