#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

Writes one original word an ex would use to describe you to /output/entry.txt.
"""

ENTRY = "Practice"


import os


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 24, f"word is {len(text)} chars"
    assert len(text.split()) == 1, "entry must be exactly one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
