#!/usr/bin/env python3
"""Assemble frozen chapters into the print PDF.

Pipeline: frozen markdown -> pandoc (HTML fragments) -> book-styled HTML -> WeasyPrint PDF.

Usage:
    python3 tools/build_pdf.py                 # full book from manuscript/frozen/
    python3 tools/build_pdf.py --draft         # include draft-v3 chapters not yet frozen, watermarked DRAFT
    python3 tools/build_pdf.py --out path.pdf

Reads BOOK_ORDER below; missing units are skipped with a warning so partial
builds work throughout production. Endnotes are collected from per-chapter
`notes/ch-NN.md` files if present; the bibliography from `research/sources.bib`
(fallback: research/*/evidence.md source lines, deduplicated).
"""

import argparse
import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
FROZEN = MANUSCRIPT / "frozen"

# (unit-id, display kind, part-heading-to-emit-before-or-None, title)
BOOK_ORDER = [
    ("prologue", "prologue", None, "Prologue — The Thing Nobody Chose"),
    ("ch-01", "chapter", "Part One — The Trap", "1 · Everyone Hates This"),
    ("ch-02", "chapter", None, "2 · The Shadow of the Future"),
    ("ch-03", "chapter", None, "3 · Eight Rules from a Spanish Water Court"),
    ("ch-04", "chapter", None, "4 · Morality as Technology"),
    ("ch-05", "chapter", "Part Two — The Ground", "5 · The Dentist's Drill"),
    ("ch-06", "chapter", None, "6 · Whose Suffering"),
    ("ch-07", "chapter", None, "7 · What I Don't Know"),
    ("ch-08", "chapter", "Part Three — The Architecture", "8 · The Fence in the Field"),
    ("ch-09", "chapter", None, "9 · The Man at the Door"),
    ("ch-10", "chapter", None, "10 · Three Gates"),
    ("ch-11", "chapter", None, "11 · Firmware"),
    ("ch-12", "chapter", "Part Four — The Life", "12 · Tuesday Morning"),
    ("ch-13", "chapter", None, "13 · Love Is an Iterated Game (And That's Not an Insult)"),
    ("ch-14", "chapter", None, "14 · Building Purpose Without a Script"),
    ("ch-15", "chapter", None, "15 · What the Stoics Got Right"),
    ("ch-16", "chapter", "Part Five — The Scale", "16 · Institutions That Can Be Wrong"),
    ("ch-17", "chapter", None, "17 · Prices Are Sentences"),
    ("coda", "prologue", None, "Coda — What This Doesn't Solve"),
]

CSS = """
@page {
    size: 6in 9in;
    margin: 0.85in 0.7in 0.9in 0.7in;
    @bottom-center { content: counter(page); font-family: 'Palatino', 'Georgia', serif; font-size: 9pt; color: #444; }
}
@page :first { @bottom-center { content: none; } }
html { font-size: 10.8pt; }
body { font-family: 'Palatino', 'Georgia', serif; line-height: 1.52; color: #111; text-align: justify; hyphens: auto; }
h1.part { page-break-before: right; text-align: center; margin-top: 2.8in; font-size: 1.7rem; font-weight: 600; letter-spacing: 0.04em; }
h1.chapter { page-break-before: right; margin-top: 1.6in; margin-bottom: 1.4rem; font-size: 1.35rem; font-weight: 600; text-align: left; }
h2 { font-size: 1.02rem; font-weight: 600; margin-top: 1.6rem; letter-spacing: 0.02em; }
p { margin: 0 0 0 0; text-indent: 1.35em; orphans: 2; widows: 2; }
h1 + p, h2 + p, blockquote + p.noindent, p.first { text-indent: 0; }
blockquote { margin: 0.8rem 1.4em; font-size: 0.97rem; text-indent: 0; }
blockquote p { text-indent: 0; }
.front { page-break-before: right; }
.title-page { text-align: center; margin-top: 2.2in; }
.title-page .title { font-size: 2rem; font-weight: 700; }
.title-page .subtitle { font-size: 1.05rem; margin-top: 0.8rem; font-style: italic; }
.title-page .author { margin-top: 2.4rem; font-size: 1.1rem; }
.disclosure { font-size: 0.85rem; color: #333; margin-top: 3.2in; text-indent: 0; }
.draftmark { position: fixed; top: 3.5in; left: 0.5in; font-size: 3.2rem; color: rgba(200,30,30,0.13); transform: rotate(-30deg); }
.toc { margin-top: 1.2rem; }
.toc p { text-indent: 0; margin: 0 0 0.28rem 0; }
.toc-part { font-weight: 600; margin-top: 1.1rem !important; margin-bottom: 0.5rem !important; font-size: 0.95rem; letter-spacing: 0.03em; }
.toc-entry { padding-left: 1.1em; font-size: 0.95rem; }
.toc-missing { color: #999; }
.endnotes h2 { margin-top: 1.5rem; font-size: 0.95rem; }
.endnotes p, .bibliography p { font-size: 0.88rem; text-indent: -1.2em; padding-left: 1.2em; margin-bottom: 0.35rem; }
.anchor-draft { background: #fff6d6; }
"""


def pandoc_fragment(md_path: Path) -> str:
    out = subprocess.run(
        ["pandoc", "-f", "markdown+smart", "-t", "html", str(md_path)],
        capture_output=True, text=True, check=True,
    )
    frag = out.stdout
    # Mark ANCHOR-DRAFT spans visibly in draft builds (comments survive pandoc as raw HTML)
    frag = frag.replace("<!-- ANCHOR-DRAFT -->", '<span class="anchor-draft">[ANCHOR-DRAFT]</span>')
    # Drop the source H1 (title is emitted by the assembler)
    frag = re.sub(r"<h1[^>]*>.*?</h1>\n?", "", frag, count=1)
    return frag


def find_unit(unit: str, allow_draft: bool):
    frozen = FROZEN / f"{unit}.md"
    if frozen.exists():
        return frozen, False
    if allow_draft:
        for cand in sorted((MANUSCRIPT / unit).glob("draft-v*.md"), reverse=True):
            return cand, True
    return None, False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", action="store_true", help="include latest drafts for unfrozen units, watermarked")
    ap.add_argument("--out", default=str(ROOT / "build" / "book.pdf"))
    ap.add_argument("--title", default="The Thing Nobody Chose")
    ap.add_argument("--subtitle", default="An honest moral framework for people who don't believe in cosmic authority")
    ap.add_argument("--author", default="Brennan Kelley")
    args = ap.parse_args()

    parts = []
    missing = []
    any_draft = False

    parts.append(
        f'<div class="front title-page"><div class="title">{html.escape(args.title)}</div>'
        f'<div class="subtitle">{html.escape(args.subtitle)}</div>'
        f'<div class="author">{html.escape(args.author)}</div></div>'
    )
    parts.append(
        '<div class="front"><p class="disclosure">This book was produced with AI drafting assistance '
        'under the author’s direction, against a documented review pipeline; the arguments, '
        'judgments, and final text are the author’s responsibility. The companion audiobook, '
        'when released, uses a disclosed synthetic narration of the author’s own voice. '
        'A methods appendix describes the process.</p></div>'
    )

    # Edition / provenance page
    parts.append(
        '<div class="front"><p class="disclosure">First edition, work in progress. '
        'Chapters marked DRAFT have not completed the production pipeline\u2019s review gates. '
        'Every quotation and empirical claim in a finished chapter has been checked twice: once '
        'by the researcher who supplied it and once, independently, against the original source. '
        'Where the evidence would not support a claim, the claim was cut. Notes at the back carry '
        'the sources.</p></div>'
    )

    # Contents
    toc = ['<div class="front"><h1 class="chapter">Contents</h1><div class="toc">']
    for unit, kind, part_heading, title in BOOK_ORDER:
        path, _ = find_unit(unit, args.draft)
        if part_heading:
            toc.append(f'<p class="toc-part">{html.escape(part_heading)}</p>')
        cls = "toc-entry" if path else "toc-entry toc-missing"
        toc.append(f'<p class="{cls}">{html.escape(title)}</p>')
    toc.append('</div></div>')
    parts.append("".join(toc))

    for unit, kind, part_heading, title in BOOK_ORDER:
        path, is_draft = find_unit(unit, args.draft)
        if path is None:
            missing.append(unit)
            continue
        any_draft = any_draft or is_draft
        if part_heading:
            parts.append(f'<h1 class="part">{html.escape(part_heading)}</h1>')
        cls = "chapter" if kind == "chapter" else "chapter"
        mark = ' <span style="font-size:0.7em;color:#a00">[DRAFT]</span>' if is_draft else ""
        parts.append(f'<h1 class="{cls}">{html.escape(title)}{mark}</h1>')
        parts.append(pandoc_fragment(path))

    # Endnotes + bibliography
    notes_dir = ROOT / "notes"
    if notes_dir.exists():
        ordered = [notes_dir / f"{u}.md" for u, _, _, _ in BOOK_ORDER]
        note_files = [f for f in ordered if f.exists()]
        note_files += sorted(set(notes_dir.glob("*.md")) - set(note_files))
        if note_files:
            parts.append('<h1 class="chapter endnotes">Notes</h1>')
            for f in note_files:
                title = f.stem.replace("ch-", "Chapter ").replace("prologue", "Prologue").title()
                frag = pandoc_fragment(f)
                parts.append(f'<div class="endnotes"><h2>{html.escape(title)}</h2>{frag}</div>')
    bib = ROOT / "research" / "sources.bib.md"
    if bib.exists():
        parts.append('<h1 class="chapter bibliography">Sources</h1>')
        parts.append(f'<div class="bibliography">{pandoc_fragment(bib)}</div>')
    positions = ROOT / "canon" / "POSITIONS.md"
    if positions.exists():
        parts.append('<h1 class="chapter">Appendix — Positions, Confidence, and What Would Change My Mind</h1>')
        parts.append(pandoc_fragment(positions))

    watermark = '<div class="draftmark">DRAFT — NOT FOR RELEASE</div>' if any_draft else ""
    doc = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{watermark}{''.join(parts)}</body></html>"
    )

    out_pdf = Path(args.out)
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    html_path = out_pdf.with_suffix(".html")
    html_path.write_text(doc)

    subprocess.run(
        ["weasyprint", str(html_path), str(out_pdf)],
        check=True,
    )

    print(f"PDF: {out_pdf}")
    print(f"HTML: {html_path}")
    if missing:
        print(f"WARNING — missing units skipped: {', '.join(missing)}")
    if any_draft:
        print("NOTE — contains unfrozen drafts; watermarked.")


if __name__ == "__main__":
    main()
