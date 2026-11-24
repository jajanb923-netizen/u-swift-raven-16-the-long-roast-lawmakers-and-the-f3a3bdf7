#!/usr/bin/env python3
"""The Long Roast entry: lawmakers and the file they cannot convert.

Writes a single satirical sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt for local runs). Python 3.13 stdlib only,
deterministic, no network access.

The line was picked from eleven candidates scored against the judge
brief in CANDIDATES.md (on-subject, turn, aim, clean read, specific
detail): Congress can regulate the entire internet, but the bill that
does it is itself a Word document called FINAL_v7_REAL.docx -- the
lawmaker's authority set up, then undercut by the file they cannot
convert, with the punch landing on the filename.

The gate check enforces the kit's gate (UTF-8 text, 1-320 chars, not
only whitespace) plus the one-sentence form the judge requires: a
single declarative sentence, no line breaks, no leading or trailing
whitespace, ending in one period. The written file is read back and
verified byte-identical to the chosen line before the run reports
success, so a partial or altered write can never pass silently.
"""

import os
import sys

MAX_CHARS = 320
OUTPUT_NAME = "entry.txt"

LINE = (
    "Congress can regulate the entire internet, but the bill that "
    "does it is still a Word document called FINAL_v7_REAL.docx."
)


def chosen_line():
    """Return the entry line: the bill is a Word doc named FINAL_v7_REAL."""
    return LINE


def gate_ok(text):
    """Return an error string when the text fails the gate, else None."""
    if not text.strip():
        return "entry is empty or only whitespace"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line, not multiple lines"
    if len(text) > MAX_CHARS:
        return "entry is %d chars, over the 320-char limit" % len(text)
    if "?" in text or "!" in text:
        return "entry must be one declarative sentence (no ? or !)"
    if not text.endswith(".") or text.endswith(".."):
        return "entry must end in a single period"
    text.encode("utf-8")  # raises UnicodeEncodeError on invalid text
    return None


def write_entry(out_dir, text):
    """Write the line to <out_dir>/entry.txt and return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return path


def main():
    text = chosen_line()
    error = gate_ok(text)
    if error is not None:
        print("gate failed: %s" % error, file=sys.stderr)
        return 1
    path = write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), text)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        print("gate failed: written file differs from the chosen line",
              file=sys.stderr)
        return 1
    print("wrote %d chars to %s (verified byte-identical)" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
