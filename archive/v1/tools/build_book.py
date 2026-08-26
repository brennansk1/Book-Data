#!/usr/bin/env python3
"""Build The Manual of Harmonious Rationality as a formatted PDF."""

import subprocess
import os

PROJECT = "/Users/brennankelley/Desktop/Projects/Book-Data-main"
CHAPTERS_DIR = os.path.join(PROJECT, "Book", "Chapters")
OUTPUT_DIR = PROJECT

# Book structure
BOOK_ORDER = [
    # Front matter
    ("front", "TITLE_PAGE.md"),
    ("front", "PREFACE.md"),

    # Book I: Foundations
    ("book", "# Book I: Foundations — What Is Real?"),
    ("ch", "CH-01.md"),
    ("ch", "CH-02.md"),
    ("ch", "CH-03.md"),
    ("ch", "CH-04.md"),
    ("ch", "CH-05.md"),

    # Book II: The Enemy
    ("book", "# Book II: The Enemy — Why Suffering Persists"),
    ("ch", "CH-06.md"),
    ("ch", "CH-07.md"),
    ("ch", "CH-08.md"),

    # Book III: The Moral Architecture
    ("book", "# Book III: The Moral Architecture — How to Decide"),
    ("ch", "CH-09.md"),
    ("ch", "CH-10.md"),
    ("ch", "CH-11.md"),
    ("ch", "CH-12.md"),

    # Book IV: Personal Ethics
    ("book", "# Book IV: Personal Ethics — Living the System"),
    ("ch", "CH-13.md"),
    ("ch", "CH-14.md"),
    ("ch", "CH-15.md"),
    ("ch", "CH-16.md"),

    # Book V: Political Philosophy
    ("book", "# Book V: Political Philosophy — Engineering the State"),
    ("ch", "CH-17.md"),
    ("ch", "CH-18.md"),
    ("ch", "CH-19.md"),
    ("ch", "CH-20.md"),
    ("ch", "CH-21.md"),
    ("ch", "CH-22.md"),
    ("ch", "CH-23.md"),
    ("ch", "CH-24.md"),
    ("ch", "CH-25.md"),

    # Book VI: Economic Philosophy
    ("book", "# Book VI: Economic Philosophy — The Machinery of Prosperity"),
    ("ch", "CH-26.md"),
    ("ch", "CH-27.md"),
    ("ch", "CH-28.md"),
    ("ch", "CH-29.md"),
    ("ch", "CH-30.md"),
    ("ch", "CH-31.md"),

    # Book VII: The Frontier
    ("book", "# Book VII: The Frontier — Problems at the Edge"),
    ("ch", "CH-32.md"),
    ("ch", "CH-33.md"),
    ("ch", "CH-34.md"),
    ("ch", "CH-35.md"),
    ("ch", "CH-36.md"),

    # Book VIII: Defense
    ("book", "# Book VIII: Defense — Defeating Rival Systems"),
    ("ch", "CH-37.md"),
    ("ch", "CH-38.md"),
    ("ch", "CH-39.md"),
    ("ch", "CH-40.md"),
    ("ch", "CH-41.md"),
    ("ch", "CH-42.md"),
    ("ch", "CH-43.md"),
    ("ch", "CH-44.md"),
    ("ch", "CH-45.md"),
    ("ch", "CH-46.md"),

    # Book IX: Synthesis
    ("book", "# Book IX: Synthesis"),
    ("ch", "CH-47.md"),
    ("ch", "CH-48.md"),
    ("ch", "CH-49.md"),

    # Back matter
    ("front", "BACK_MATTER.md"),
]

def build_combined_markdown():
    """Combine all chapters into a single markdown file."""
    parts = []

    for entry_type, content in BOOK_ORDER:
        if entry_type == "book":
            # Book divider
            parts.append(f"\n\n<div class='book-divider'></div>\n\n{content}\n\n---\n\n")
        elif entry_type in ("ch", "front"):
            filepath = os.path.join(CHAPTERS_DIR, content)
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    text = f.read()
                # Add page break before each chapter
                parts.append(f"\n\n<div class='chapter-break'></div>\n\n{text}\n\n")
            else:
                print(f"WARNING: {filepath} not found")

    return "\n".join(parts)


def build_html(markdown_content):
    """Convert markdown to styled HTML using pandoc."""
    # Write combined markdown
    combined_path = os.path.join(OUTPUT_DIR, "book_combined.md")
    with open(combined_path, 'w') as f:
        f.write(markdown_content)

    html_path = os.path.join(OUTPUT_DIR, "book.html")

    # Use pandoc to convert markdown to HTML with standalone template
    result = subprocess.run([
        "pandoc",
        combined_path,
        "-o", html_path,
        "--standalone",
        "--toc",
        "--toc-depth=2",
        f"--metadata=title:The Manual of Harmonious Rationality",
        "--wrap=none",
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Pandoc error: {result.stderr}")
        return None

    # Read the HTML and inject custom CSS for book formatting
    with open(html_path, 'r') as f:
        html = f.read()

    custom_css = """
    <style>
    @page {
        size: 6in 9in;
        margin: 0.8in 0.7in 0.8in 0.7in;
        @bottom-center { content: counter(page); font-family: 'Georgia', serif; font-size: 9pt; }
    }
    @page :first { @bottom-center { content: none; } }

    body {
        font-family: 'Georgia', 'Times New Roman', serif;
        font-size: 11pt;
        line-height: 1.55;
        color: #1a1a1a;
        max-width: 100%;
        hyphens: auto;
    }

    h1 {
        font-size: 22pt;
        font-weight: bold;
        margin-top: 1.5in;
        margin-bottom: 0.3in;
        text-align: center;
        page-break-before: always;
        font-family: 'Georgia', serif;
        letter-spacing: 0.02em;
    }

    h2 {
        font-size: 14pt;
        font-weight: bold;
        margin-top: 0.5in;
        margin-bottom: 0.15in;
        font-family: 'Georgia', serif;
        border-bottom: none;
    }

    h3 {
        font-size: 12pt;
        font-weight: bold;
        margin-top: 0.3in;
        margin-bottom: 0.1in;
        font-family: 'Georgia', serif;
    }

    p {
        margin-top: 0;
        margin-bottom: 0.6em;
        text-align: justify;
        text-indent: 0;
    }

    blockquote {
        margin: 0.8em 0.3in;
        padding-left: 0.2in;
        border-left: 2pt solid #888;
        font-style: italic;
        font-size: 10.5pt;
        color: #333;
    }

    blockquote p { text-align: left; text-indent: 0; }

    strong { font-weight: bold; }
    em { font-style: italic; }

    hr {
        border: none;
        border-top: 0.5pt solid #ccc;
        margin: 0.4in 1in;
    }

    ul, ol {
        margin-left: 0.3in;
        margin-bottom: 0.5em;
    }

    li { margin-bottom: 0.25em; }

    table {
        width: 100%;
        border-collapse: collapse;
        margin: 0.3in 0;
        font-size: 9.5pt;
    }

    th, td {
        border: 0.5pt solid #999;
        padding: 4pt 6pt;
        text-align: left;
        vertical-align: top;
    }

    th {
        background-color: #f0f0f0;
        font-weight: bold;
    }

    .book-divider {
        page-break-before: always;
    }

    .chapter-break {
        page-break-before: always;
    }

    /* Table of Contents styling */
    #TOC {
        page-break-after: always;
        margin-top: 0.5in;
    }
    #TOC ul { list-style: none; padding-left: 0; }
    #TOC li { margin-bottom: 0.15em; font-size: 10.5pt; }
    #TOC a { text-decoration: none; color: #1a1a1a; }

    /* Title page */
    .title {
        font-size: 28pt;
        text-align: center;
        margin-top: 2.5in;
        font-family: 'Georgia', serif;
        font-weight: bold;
        letter-spacing: 0.03em;
    }
    </style>
    """

    # Inject CSS before </head>
    html = html.replace("</head>", custom_css + "\n</head>")

    with open(html_path, 'w') as f:
        f.write(html)

    return html_path


def html_to_pdf(html_path):
    """Convert HTML to PDF using weasyprint."""
    pdf_path = os.path.join(OUTPUT_DIR, "The_Manual_of_Harmonious_Rationality.pdf")

    env = os.environ.copy()
    env["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib"

    result = subprocess.run([
        "/Users/brennankelley/Library/Python/3.9/bin/weasyprint",
        html_path,
        pdf_path,
    ], capture_output=True, text=True, env=env)

    if result.returncode != 0:
        print(f"WeasyPrint error: {result.stderr}")
        return None

    return pdf_path


if __name__ == "__main__":
    print("Step 1: Building combined markdown...")
    md = build_combined_markdown()
    print(f"  Combined: {len(md):,} characters")

    print("Step 2: Converting to styled HTML...")
    html_path = build_html(md)
    if not html_path:
        print("  FAILED at HTML generation")
        exit(1)
    print(f"  HTML: {html_path}")

    print("Step 3: Converting to PDF...")
    pdf_path = html_to_pdf(html_path)
    if not pdf_path:
        print("  FAILED at PDF generation")
        exit(1)

    size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"  PDF: {pdf_path} ({size_mb:.1f} MB)")
    print("\nDone! Your book is ready.")
