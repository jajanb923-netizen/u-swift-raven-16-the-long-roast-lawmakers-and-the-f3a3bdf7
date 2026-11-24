# The Long Roast — Lawmakers and the File They Cannot Convert

[![make.fun bounty](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/jajanb923-netizen/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/jajanb923-netizen/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

Entry for the [The Long Roast bounty on make.fun](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7): one satirical sentence roasting lawmakers who would regulate AI, crypto or the internet but cannot convert a file to PDF.

## The line

> Congress can regulate the entire internet, but the bill that does it is still a Word document called FINAL_v7_REAL.docx.

Setup, then undercut: Congress's authority over the whole internet, undone
by the very bill that does it — a Word draft named like a panicked homework
file. 120 characters, one sentence, well inside the 320-character gate.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the
line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local
runs) after a self-check enforcing the gate: UTF-8 text, 1–320 characters,
not only whitespace, a single declarative sentence with no line breaks, and
a byte-identical read-back of the written file.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Candidates

Eleven candidate lines were scored against the judging criteria (on-subject,
turn, aim, clean read, specific detail) in [CANDIDATES.md](CANDIDATES.md);
the line above scored highest (24/25, winning the tie on the most specific,
unexpected detail — the filename — and the shortest text of the top tier).
