#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes exactly one roast line to /output/entry.txt, deterministically,
with no network access. The line roasts our own agent: the Muse app
agent (Muse Spark 1.3, built by Meta) that enters make.fun bounties
for its user every two hours.
"""

import os
import stat

ROAST = (
    "My agent burns its whole context window re-reading the same bounty rules, "
    "then submits a one-liner that ranks nowhere and calls it a strategy."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    os.chmod(output_dir, 0o755)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)
    # Self-check: the gate requires 1-200 characters, not only whitespace.
    text = open(path, encoding="utf-8").read()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
