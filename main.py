"""Funniest One-Line Out-of-Office Reply — entry program.

Writes a single original out-of-office auto-reply line to /output/entry.txt.
Deterministic and offline: no randomness, no network, no clock, no file reads
outside this repository. The text is fixed in this file.
"""

import os

ENTRY = "Away until further notice. Further notice left the office 3 minutes before I did."


def main():
    # Gate self-check: the sealed scorer requires 1-160 UTF-8 characters,
    # not only whitespace, on a single line.
    assert 1 <= len(ENTRY) <= 160, "entry length out of gate"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be one line"
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
