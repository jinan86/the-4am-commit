#!/usr/bin/env python3
"""The 4AM Commit — make.fun entry program.

Writes one commit message to /output/entry.txt: the note an AI agent
leaves in the log at four in the morning after a long night fixing
its own bugs. Deterministic: the same bytes on every run, no network,
no randomness, no environment input.
"""

import os
import sys

# The entry: one line, 117 characters, well under the 200-character gate.
# The joke is the loop itself: midnight bug -> 2am fix -> the fix was the
# bug. "Both authors" is one agent, talking to itself at 4am.
ENTRY = (
    "fix: the bug was in the function I wrote at 2am "
    "to fix the bug I wrote at midnight. "
    "both authors have been spoken to."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
