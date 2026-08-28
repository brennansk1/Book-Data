#!/usr/bin/env python3
"""Mechanically convert a frozen chapter into an audio-edition draft.

Does the deterministic 80% that agents were doing by hand at ~150k tokens per
chapter: comment stripping, citation stripping, number-to-speech, blockquote
voice marking, frontmatter. Emits a TODO block listing exactly the judgment
calls a human or agent still has to make (homographs in risky positions,
sentences too long to say in one breath, antecedents worth restating).

    python3 tools/mkaudio.py manuscript/frozen/ch-05.md --title "Chapter Five. The Dentist's Drill."
"""
import argparse, re, sys
from pathlib import Path

ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}

def small(n):
    if n < 20: return ONES[n]
    if n < 100:
        t, r = divmod(n, 10)
        return TENS[t] + ("-" + ONES[r] if r else "")
    h, r = divmod(n, 100)
    return ONES[h] + " hundred" + (" " + small(r) if r else "")

def spell(n):
    if n < 1000: return small(n)
    if n < 1_000_000:
        th, r = divmod(n, 1000)
        return small(th) + " thousand" + (" " + small(r) if r else "")
    m, r = divmod(n, 1_000_000)
    return small(m) + " million" + (" " + spell(r) if r else "")

def year(y):
    n = int(y)
    if 1100 <= n <= 1999:
        hi, lo = divmod(n, 100)
        if lo == 0: return small(hi) + " hundred"
        return small(hi) + " " + ("oh " + ONES[lo] if lo < 10 else small(lo))
    if 2000 <= n <= 2009: return "two thousand" + ("" if n == 2000 else " " + ONES[n-2000])
    if 2010 <= n <= 2099: return "twenty " + small(n - 2000)
    return spell(n)

HOMOGRAPHS = ["defect","defects","read","reads","close","closer","deliberate","separate","record",
              "records","present","lead","live","minute","object","conduct","content","refuse",
              "produce","project","subject","wound","bow","resume","invalid","second","seconds"]

def convert(md: str) -> tuple[str, list[str]]:
    todo = []
    t = md
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)                  # ANCHOR / KEEP / PLACEHOLDER
    t = re.sub(r"\s*\((?:pp?\.|see )[^)]*\)", "", t)              # (p. 33) (pp. 53-54) (see ...)
    t = re.sub(r"^#\s+.*$", "", t, flags=re.M)                    # source H1; assembler adds its own

    # money: $3.8 billion / $1,499
    t = re.sub(r"\$([\d,]+(?:\.\d+)?)\s*(billion|million|thousand)?",
               lambda m: (m.group(1).replace(",", "") + (" " + m.group(2) if m.group(2) else "") + " dollars")
               if "." in m.group(1) else (spell(int(m.group(1).replace(",", ""))) +
               (" " + m.group(2) if m.group(2) else "") + " dollars"), t)
    # decades: 1850s
    t = re.sub(r"\b(1[0-9]{3})s\b", lambda m: "the " + year(m.group(1)) + "s", t)
    # bare years
    t = re.sub(r"\b(1[1-9][0-9]{2}|20[0-9]{2})\b", lambda m: year(m.group(1)), t)
    # remaining integers with separators or 3+ digits
    t = re.sub(r"\b(\d{1,3}(?:,\d{3})+|\d{3,})\b",
               lambda m: spell(int(m.group(1).replace(",", ""))), t)
    t = re.sub(r"\n{3,}", "\n\n", t).strip()

    # judgment calls left for the pass that follows
    for w in HOMOGRAPHS:
        for m in re.finditer(rf"\b{w}\b", t, re.I):
            s = t[max(0, m.start()-45):m.end()+45].replace("\n", " ")
            todo.append(f"HOMOGRAPH `{w}`: …{s}…")
    for sent in re.split(r"(?<=[.!?])\s+", t):
        n = len(sent.split())
        if n > 40:
            todo.append(f"BREATH ({n} words): {sent[:110]}…")
    if re.search(r"\b(this|that|these|those|the former|the latter)\b\s+(one|thing|point|case)?\s*$",
                 t, re.M):
        todo.append("ANTECEDENT: dangling demonstrative at a line end — check a listener can resolve it.")
    return t, todo

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source"); ap.add_argument("--title", required=True)
    ap.add_argument("--voice", default="narration")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    src = Path(a.source)
    body, todo = convert(src.read_text())
    out = Path(a.out or f"audio/script/{src.stem}.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    head = f"---\nvoice-default: {a.voice}\n---\n\n# {a.title}\n\n"
    out.write_text(head + body + "\n")
    todo_path = out.with_suffix(".todo.txt")
    todo_path.write_text("\n".join(todo) + "\n" if todo else "clean\n")
    print(f"{out}  ({len(body.split())} words)")
    print(f"{todo_path}  ({len(todo)} judgment items)")

if __name__ == "__main__":
    main()
