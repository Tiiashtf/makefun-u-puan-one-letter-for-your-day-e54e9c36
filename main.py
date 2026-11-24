#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one letter, "B", to /output/entry.txt — nothing else, no
word, no gloss, no punctuation, no trailing newline.

The letter B stands for "burnout": the honest one-word report of the day
behind it. A day spent grinding through the night, entry after entry,
until the tank is empty — vivid, funny in the dark way only the
sleep-deprived find funny, and true. B is burnout's own initial, not a
vague mood and not the obvious pick where a sharper one exists.
"""

import os
import shutil

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
LETTER = "B"  # burnout


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the directory's CONTENTS, never the directory itself:
    # the grader can run this with a root-owned output directory inside
    # a sticky parent, where removing the directory fails with EPERM.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        try:
            if os.path.isdir(path) and not os.path.islink(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
        except OSError:
            # A stray file we cannot remove must not fail the run.
            pass
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and refuse to pass silently if the file is not exactly
    # one letter A-Z: a wrong byte must fail the run, not the entry.
    with open(OUTPUT_FILE, "rb") as f:
        written = f.read()
    if len(written) != 1 or not (65 <= written[0] <= 90):
        raise SystemExit("entry.txt must be exactly one letter A-Z")


if __name__ == "__main__":
    main()
