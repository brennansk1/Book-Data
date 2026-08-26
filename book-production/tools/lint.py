#!/usr/bin/env python3
"""
Gate 2 style linter for the book production pipeline.

Usage:
    python lint.py manuscript/ch-10/draft-v1.md
    python lint.py manuscript/ch-10/draft-v1.md --frozen manuscript/frozen/*.md

Exit 0 = pass, 1 = hard fail. Warnings do not fail the build.
Thresholds mirror STYLE_BIBLE.md §6. Tune them once, in one place, here.
"""

import argparse
import glob
import re
import statistics
import sys
from collections import Counter

# ---------------------------------------------------------------- thresholds

T = {
    "words":            (3200, 5600, 4000, 4800),   # hard_lo, hard_hi, soft_lo, soft_hi
    "sent_mean":        (None, 24,   15,   20),
    "sent_sd":          (7,    None, 9,    None),
    "pct_short":        (4.0,  None, 8.0,  None),   # sentences < 8 words
    "pct_long":         (None, 5.0,  None, 2.0),    # sentences > 40 words
    "para_mean":        (None, 150,  None, 110),
    "para_max":         (None, 260,  None, 200),
    "headers":          (None, 3,    None, 2),
    "lists":            (None, 1,    None, 1),
    "named_people":     (2,    None, 3,    None),
    "first_person":     (3,    None, 5,    None),
    "confidence_mods":  (1,    None, 2,    None),
    "emdash_per_kw":    (None, 7.0,  None, 4.0),
    "tricolons":        (None, 5,    None, 3),
    "not_x_but_y":      (None, 4,    None, 2),
    "negate_correct":   (None, 8,    None, 4),   # IDIOLECT: one cluster (<=3) + slack
    "nominal_openers":  (None, 5,    None, 2),
    "passive_pct":      (None, 18.0, None, 12.0),
    # --- VOICE.md
    "para_sd":          (30,   None, 45,   None),
    "solo_paras":       (1,    None, 2,    None),   # one-sentence paragraphs
    "long_paras":       (1,    None, 1,    None),   # > 160 words
    "connectives":      (None, 8,    None, 4),
    "plain_band":       (3,    None, 6,    None),
    "anchor_words":     (1,    None, 200,  400),    # <!-- ANCHOR --> block
    "keep_marks":       (1,    None, 2,    4),
}

CONNECTIVE_OPENER = re.compile(
    r"^\s*(However|Moreover|Furthermore|Additionally|That said|Nevertheless|"
    r"Nonetheless|In addition|Consequently|Therefore|Thus|Indeed)\b", re.M)

PLAIN_BAND = re.compile(
    r"\b(thing|things|stuff|mess|messy|bad|weird|big|awful|gets|got|"
    r"kind of|sort of|a lot|pretty much|whole)\b", re.I)

BANNED = [
    r"\bit'?s not just .{1,40}, it'?s\b",
    r"\blet us (be precise|examine|consider|turn)\b",
    r"\bconsider the following\b",
    r"\bthe key insight is\b",
    r"\bthe crucial point is\b",
    r"\bin this chapter,? we (will|shall)\b",
    r"\bit'?s worth noting that\b",
    r"\b(importantly|notably|crucially),",
    r"\bwhat this chapter (established|has established)\b",
    r"\b(in )?summary\b\s*$",
    r"\bthe framework (holds|argues|maintains|contends)\b",
    r"\bdelve\b", r"\btapestry\b", r"\bunderscore(s|d)?\b",
    r"\bmultifaceted\b", r"\bat its core\b", r"\bleverag(e|ing)\b",
    r"\b(navigat\w+|landscape) (the|of) \w+ (complexit|challeng|terrain)",
    r"\bprofound(ly)?\b",
]

CONFIDENCE_MODS = [
    r"\bI'?m (fairly |quite |reasonably |much )?(confident|certain|sure)\b",
    r"\bI'?m (much |far )?less (sure|confident|certain)\b",
    r"\bI don'?t know\b",
    r"\bI could be wrong\b",
    r"\bthe evidence here is (weak|thin|mixed|contested)\b",
    r"\b(genuinely|honestly) (unsettled|contested|divided)\b",
]

PASSIVE = re.compile(
    r"\b(is|are|was|were|been|being|be)\s+(\w+ly\s+)?\w+(ed|en)\b(?=\s+by\b|\s|[.,;])",
    re.I,
)

NOMINAL_OPENER = re.compile(
    r"^(The|A|An)\s+\w*(tion|ity|ism|ness|ment|ance|ence)\b", re.I
)

TRICOLON = re.compile(r"\b[\w'-]+(?:\s+[\w'-]+){0,3},\s+[\w'-]+(?:\s+[\w'-]+){0,3},\s+and\s+[\w'-]+")

NOT_X_BUT_Y = re.compile(r"\bnot\s+(?:merely\s+|simply\s+|just\s+)?[^.,;]{3,60},?\s+but\s+", re.I)

# The negation-and-correct family, in every guise the red team has caught it wearing.
# Reviewers found this in five consecutive chapters under names the plain
# "not X but Y" regex never matched; IDIOLECT.md rations it to one cluster.
NEGATE_CORRECT = [
    NOT_X_BUT_Y,
    # "not X — it's Y" / "not X. It's Y." / "not X; it was Y"
    re.compile(r"\bnot\s+[^.;—]{3,70}[—;.]\s*(?:it|he|she|they|that|this)\s+(?:'s|s|is|was|were|are)\b", re.I),
    # "X isn't/wasn't [vice]. X is/was [structural reason]."
    re.compile(r"\b(?:is|was|are|were)n'?t\s+[^.;—]{3,70}[.;—]\s*(?:it|he|she|they|that|this)\s+(?:is|was|were|are)\b", re.I),
    # "wasn't being X" / "weren't being X" — the book's own signature form
    re.compile(r"\b(?:is|was|are|were)n'?t\s+being\s+\w+", re.I),
]

# crude proper-noun-person detector: capitalised token not at sentence start,
# excluding a stoplist of places/institutions/months.
STOP_CAPS = {
    "The","This","That","These","Those","But","And","Or","If","When","While",
    "Chapter","Part","Book","Volume","Monday","Tuesday","Wednesday","Thursday",
    "Friday","Saturday","Sunday","January","February","March","April","May",
    "June","July","August","September","October","November","December",
    "America","American","Europe","European","English","Western","God","I",
}


def sentences(text):
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'“‘])", text)
    return [p.strip() for p in parts if p.strip()]


def strip_meta(md):
    md = re.sub(r"^---.*?^---", "", md, flags=re.S | re.M)   # frontmatter
    md = re.sub(r"^>.*$", "", md, flags=re.M)                # block quotes
    return md


def ngrams(text, n=6):
    toks = re.findall(r"[a-z']+", text.lower())
    return {" ".join(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def check(name, value, fmt="{:.1f}"):
    hard_lo, hard_hi, soft_lo, soft_hi = T[name]
    status = "ok"
    if hard_lo is not None and value < hard_lo:
        status = "FAIL"
    elif hard_hi is not None and value > hard_hi:
        status = "FAIL"
    elif soft_lo is not None and value < soft_lo:
        status = "warn"
    elif soft_hi is not None and value > soft_hi:
        status = "warn"
    return status, f"{name:<18} {fmt.format(value):>8}  [{status}]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--frozen", nargs="*", default=[],
                    help="glob(s) of frozen chapters, for repetition detection")
    args = ap.parse_args()

    raw = open(args.path, encoding="utf-8").read()
    body = strip_meta(raw)

    words = re.findall(r"\b[\w'-]+\b", body)
    sents = sentences(body)
    paras = [p for p in re.split(r"\n\s*\n", body) if p.strip() and not p.strip().startswith("#")]
    slens = [len(re.findall(r"\b[\w'-]+\b", s)) for s in sents]
    plens = [len(re.findall(r"\b[\w'-]+\b", p)) for p in paras]
    kw = max(len(words) / 1000, 0.001)

    results, fails, warns = [], 0, 0

    def run(name, val, fmt="{:.1f}"):
        nonlocal fails, warns
        st, line = check(name, val, fmt)
        results.append(line)
        if st == "FAIL":
            fails += 1
        elif st == "warn":
            warns += 1

    run("words", len(words), "{:.0f}")
    run("sent_mean", statistics.mean(slens) if slens else 0)
    run("sent_sd", statistics.pstdev(slens) if len(slens) > 1 else 0)
    run("pct_short", 100 * sum(1 for x in slens if x < 8) / max(len(slens), 1))
    run("pct_long", 100 * sum(1 for x in slens if x > 40) / max(len(slens), 1))
    run("para_mean", statistics.mean(plens) if plens else 0)
    run("para_max", max(plens) if plens else 0, "{:.0f}")
    run("headers", len(re.findall(r"^#{1,6}\s", body, re.M)), "{:.0f}")
    run("lists", len(re.findall(r"^\s*(?:[-*+]|\d+\.)\s", body, re.M)) and
        len(re.findall(r"(?:^\s*(?:[-*+]|\d+\.)\s.*\n)+", body, re.M)), "{:.0f}")

    people = Counter()
    for s in sents:
        for tok in re.findall(r"(?<!^)\b([A-Z][a-z]{2,})\b", s):
            if tok not in STOP_CAPS:
                people[tok] += 1
    run("named_people", len(people), "{:.0f}")

    run("first_person", len(re.findall(r"\bI\b", body)), "{:.0f}")
    run("confidence_mods",
        sum(len(re.findall(p, body, re.I)) for p in CONFIDENCE_MODS), "{:.0f}")
    run("emdash_per_kw", body.count("—") / kw)
    run("tricolons", len(TRICOLON.findall(body)), "{:.0f}")
    run("not_x_but_y", len(NOT_X_BUT_Y.findall(body)), "{:.0f}")
    run("negate_correct", sum(len(r.findall(body)) for r in NEGATE_CORRECT), "{:.0f}")
    run("nominal_openers", sum(1 for s in sents if NOMINAL_OPENER.match(s)), "{:.0f}")
    run("passive_pct", 100 * sum(1 for s in sents if PASSIVE.search(s)) / max(len(sents), 1))

    # ---- VOICE.md metrics
    run("para_sd", statistics.pstdev(plens) if len(plens) > 1 else 0)
    run("solo_paras", sum(1 for p in paras if len(sentences(p)) == 1), "{:.0f}")
    run("long_paras", sum(1 for x in plens if x > 160), "{:.0f}")
    run("connectives", len(CONNECTIVE_OPENER.findall(body)), "{:.0f}")
    run("plain_band", len(PLAIN_BAND.findall(body)), "{:.0f}")

    anchors = re.findall(r"<!--\s*ANCHOR\s*-->(.*?)<!--\s*/ANCHOR\s*-->", raw, re.S)
    run("anchor_words",
        sum(len(re.findall(r"\b[\w'-]+\b", a)) for a in anchors), "{:.0f}")
    run("keep_marks", len(re.findall(r"<!--\s*KEEP\s*-->", raw)), "{:.0f}")

    # ---- hard fails not expressible as thresholds
    hits = []
    for pat in BANNED:
        for m in re.finditer(pat, body, re.I | re.M):
            line = body[:m.start()].count("\n") + 1
            hits.append(f"  line {line}: {m.group(0)[:70]!r}")
    if hits:
        fails += 1

    nested = re.findall(r"^\s{2,}(?:[-*+]|\d+\.)\s", body, re.M)
    if nested:
        fails += 1

    repeats = []
    if args.frozen:
        frozen_text = ""
        for g in args.frozen:
            for f in glob.glob(g):
                frozen_text += open(f, encoding="utf-8").read()
        overlap = ngrams(body) & ngrams(frozen_text)
        repeats = sorted(overlap)[:20]
        if repeats:
            fails += 1

    # ---- report
    print(f"\n=== {args.path} ===\n")
    print("\n".join(results))
    if hits:
        print(f"\nBANNED PHRASES ({len(hits)})  [FAIL]")
        print("\n".join(hits[:25]))
    if nested:
        print(f"\nNESTED LISTS ({len(nested)})  [FAIL]")
    if repeats:
        print(f"\nREPEATED 6-GRAMS vs frozen chapters ({len(repeats)})  [FAIL]")
        for r in repeats:
            print(f"  {r!r}")
    if people:
        print(f"\nnamed candidates: {', '.join(sorted(people)[:15])}")

    print(f"\n--- {fails} hard fail(s), {warns} warning(s) ---\n")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
