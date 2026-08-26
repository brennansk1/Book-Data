#!/usr/bin/env python3
"""
Gate 2.5 — sentence-level surprisal variance ("burstiness").

Machine prose is predictable in a *uniform* way. Human prose spikes. This
scores each sentence's mean token surprisal under a small local LM, reports
the variance across sentences, and — the part that actually matters — prints
the flattest sentences as a rewrite worklist.

Do not optimise the score directly. It is gameable and it is a pointer, not
a judge. Use the worklist.

Setup (M-series Mac):
    pip install torch transformers
    # first run downloads ~1GB

MLX alternative: if you'd rather stay in MLX, swap the Scorer class for
mlx_lm — `pip install mlx-lm`, then `mlx_lm.load("mlx-community/Qwen2.5-0.5B")`
and take log_softmax over the returned logits the same way. The scoring maths
below is unchanged; only the model/device plumbing differs. MLX will be
noticeably faster on unified memory.

Usage:
    # calibrate against the model books
    python burstiness.py --build-reference voice/seed/models/*.md

    # score a chapter
    python burstiness.py manuscript/ch-10/draft-v3.md
"""

import argparse
import glob
import json
import os
import re
import statistics
import sys

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = os.environ.get("BURST_MODEL", "Qwen/Qwen2.5-0.5B")
REF_PATH = "voice/seed/reference.json"
CONTEXT_SENTS = 3          # preceding sentences used as context
MIN_TOKENS = 6             # skip fragments too short to score meaningfully


def device():
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def sentences(text):
    text = re.sub(r"^---.*?^---", "", text, flags=re.S | re.M)
    text = re.sub(r"^#{1,6}\s.*$", "", text, flags=re.M)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'“‘])", text)
    return [p.strip() for p in parts if len(p.strip()) > 1]


class Scorer:
    def __init__(self):
        self.dev = device()
        self.tok = AutoTokenizer.from_pretrained(MODEL)
        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL, torch_dtype=torch.float32
        ).to(self.dev).eval()

    @torch.no_grad()
    def surprisal(self, context, sentence):
        """Mean surprisal (nats/token) of `sentence` given `context`."""
        ctx_ids = self.tok(context, return_tensors="pt").input_ids if context else None
        full = (context + " " + sentence).strip()
        ids = self.tok(full, return_tensors="pt").input_ids.to(self.dev)
        if ids.shape[1] < 2:
            return None
        start = ctx_ids.shape[1] if ctx_ids is not None else 1
        if ids.shape[1] - start < MIN_TOKENS:
            return None

        logits = self.model(ids).logits
        logprobs = torch.log_softmax(logits[0, :-1], dim=-1)
        targets = ids[0, 1:]
        tok_lp = logprobs[torch.arange(targets.shape[0]), targets]
        # only the tokens belonging to `sentence`
        sent_lp = tok_lp[start - 1:]
        if sent_lp.numel() == 0:
            return None
        return float(-sent_lp.mean())


def score_text(scorer, text):
    sents = sentences(text)
    out = []
    for i, s in enumerate(sents):
        ctx = " ".join(sents[max(0, i - CONTEXT_SENTS):i])
        v = scorer.surprisal(ctx, s)
        if v is not None:
            out.append((v, s))
    return out


def build_reference(scorer, paths):
    files = [f for p in paths for f in glob.glob(p)]
    if not files:
        sys.exit("no reference files matched")
    allv = []
    for f in files:
        vals = score_text(scorer, open(f, encoding="utf-8").read())
        allv += [v for v, _ in vals]
        print(f"  {f}: {len(vals)} sentences")
    ref = {
        "model": MODEL,
        "n": len(allv),
        "mean": statistics.mean(allv),
        "variance": statistics.pvariance(allv),
        "sd": statistics.pstdev(allv),
        "p10": sorted(allv)[len(allv) // 10],
    }
    os.makedirs(os.path.dirname(REF_PATH), exist_ok=True)
    json.dump(ref, open(REF_PATH, "w"), indent=2)
    print(f"\nreference written to {REF_PATH}")
    print(json.dumps(ref, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--build-reference", nargs="*", default=None)
    ap.add_argument("--worklist", type=int, default=20)
    args = ap.parse_args()

    scorer = Scorer()
    print(f"model={MODEL} device={scorer.dev}\n")

    if args.build_reference is not None:
        build_reference(scorer, args.build_reference)
        return

    if not args.path:
        sys.exit("give a manuscript path, or --build-reference")

    vals = score_text(scorer, open(args.path, encoding="utf-8").read())
    if not vals:
        sys.exit("nothing scoreable")

    v = [x for x, _ in vals]
    mean, var, sd = statistics.mean(v), statistics.pvariance(v), statistics.pstdev(v)

    print(f"=== {args.path} ===")
    print(f"sentences scored : {len(v)}")
    print(f"mean surprisal   : {mean:.3f} nats/token")
    print(f"variance         : {var:.3f}")
    print(f"sd               : {sd:.3f}")

    if os.path.exists(REF_PATH):
        ref = json.load(open(REF_PATH))
        print(f"\nreference ({ref['n']} sentences from model corpus)")
        print(f"  mean {ref['mean']:.3f}   variance {ref['variance']:.3f}   sd {ref['sd']:.3f}")
        flags = []
        if var < ref["variance"] * 0.80:
            flags.append("LOW VARIANCE — prose is uniformly predictable (§1.1, §1.8)")
        if mean < ref["mean"] * 0.85:
            flags.append("LOW MEAN — diction sitting in the mid-band (§1.4)")
        for f in flags:
            print(f"  !! {f}")
        if not flags:
            print("  within range of the model corpus")
    else:
        print(f"\n(no reference at {REF_PATH} — run --build-reference first)")

    print(f"\n--- flattest {args.worklist} sentences (rewrite worklist) ---")
    for s_val, s in sorted(vals)[: args.worklist]:
        print(f"{s_val:5.2f}  {s[:110]}")

    print("\nA flat sentence is not automatically bad. Beat sentences (VOICE §1.1)")
    print("score low by design. Look for flat sentences that were *trying* to")
    print("carry an argument — those are the ones the reader slides off.")


if __name__ == "__main__":
    main()
