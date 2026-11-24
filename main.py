#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun bounty
u-mang-one-line-of-earned-pride-a0138557.

Writes a single line (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.
Standard library only.
"""

import os

LINE = (
    "Eight-year-old Jun carried the water bucket up the last steep "
    "terrace without spilling a drop, and his grandmother, who had "
    "carried it for fifty years, nodded once."
)


def main() -> None:
    line = LINE.strip()
    if not (1 <= len(line) <= 240):
        raise SystemExit(f"line is {len(line)} characters, must be 1-240")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
