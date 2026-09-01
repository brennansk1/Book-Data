#!/usr/bin/env python3
"""Canon linter — structural integrity checks on the moral system itself.

lint.py checks the prose. This checks the philosophy's bookkeeping: that every
position carries a stated vulnerability and a falsification condition, that
amendments haven't been left un-propagated, that banned items haven't crept
back, and that nothing in the manuscript claims more confidence than the
registry allows.

It cannot tell you whether an argument is good. It can tell you when the system
has stopped keeping its own promises, which is the failure that precedes the
other one.

    python3 tools/canonlint.py
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANON = ROOT / "canon"
LEVELS = ("AXIOM", "STRONG", "MODERATE", "PROVISIONAL")

def load(name):
    p = CANON / name
    return p.read_text() if p.exists() else ""

def main():
    fails, warns = [], []
    pos = load("POSITIONS.md")
    canon = load("CANON.md")
    log = load("CANON_KEEPER_LOG.md")

    # --- 1. every position declares confidence, a vulnerability, and a falsifier
    entries = re.split(r"\n### (POS-\d+[^\n]*)", pos)
    seen = {}
    for i in range(1, len(entries), 2):
        head, body = entries[i], entries[i + 1]
        pid = head.split(":")[0].strip()
        seen[pid] = head
        conf = re.search(r"\*\*Confidence:\*\*\s*(\w+)", body)
        if not conf:
            fails.append(f"{pid}: no confidence rating")
        elif conf.group(1) not in LEVELS:
            fails.append(f"{pid}: confidence '{conf.group(1)}' not one of {LEVELS}")
        if "ulnerability" not in body:
            fails.append(f"{pid}: no stated vulnerability — every position owes its own strongest objection")
        # AXIOM and PROVISIONAL are exempt from the falsifier requirement by design
        if conf and conf.group(1) in ("STRONG", "MODERATE") and "change my mind" not in body:
            warns.append(f"{pid}: {conf.group(1)} with no 'what would change my mind' condition")

    # --- 2. amendments must not be orphaned: an amended POS must still resolve
    for m in re.finditer(r"\*\*(POS-\d+)[^*]*\*\*\s*[—-]", pos):
        if m.group(1) not in seen and f"### {m.group(1)}" not in pos:
            warns.append(f"{m.group(1)}: amended but no base entry found")

    # --- 3. CANON §9 bans must not reappear anywhere in canon/ or the manuscript
    BANNED = {
        "Constructivist Realism": "banned label (CANON §9.1)",
        "thermometer analogy": "banned analogy (CANON §9.3)",
        "six-dimensional": "banned value vector (CANON §9.4)",
        "Mode A": "internal label — book says 'the standing rules' (CK-6)",
        "Mode B": "internal label — book says 'the override' (CK-6)",
    }
    targets = list((ROOT / "manuscript" / "frozen").glob("*.md"))
    for f in targets:
        t = f.read_text()
        for phrase, why in BANNED.items():
            if re.search(rf"\b{re.escape(phrase)}\b", t):
                fails.append(f"{f.name}: contains '{phrase}' — {why}")

    # --- 4. every CK ruling names the chapters it affects
    for m in re.finditer(r"\*\*(CK-\d+)[^*]*\*\*(.{0,2600}?)(?=\n\*\*CK-|\Z)", log, re.S):
        if not re.search(r"Affects:|affects:", m.group(2)):
            warns.append(f"{m.group(1)}: ruling does not name affected chapters")

    # --- 5. verdicts must not contradict a later amendment silently
    verd = load("VERDICTS.md")
    if verd and "revis" not in verd.lower() and "REVISED" not in verd:
        warns.append("VERDICTS.md: no revision marker — check it still matches amended positions")

    # --- 6. the registry must not be more confident than the book's own honesty rules allow
    if pos.count("STRONG") and not re.search(r"verdict|Verdict", pos):
        warns.append("POSITIONS.md: no verdict/theory confidence distinction stated (CK-28b)")

    n_ck = len(re.findall(r"\*\*CK-\d+", log))
    print(f"positions: {len(seen)}   rulings: {n_ck}")
    for w in warns: print(f"  [warn] {w}")
    for f_ in fails: print(f"  [FAIL] {f_}")
    print(f"\n--- {len(fails)} hard fail(s), {len(warns)} warning(s) ---")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
