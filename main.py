#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence, one-star review of Earth from an alien tourist
that still compliments the food, to /output/entry.txt.
"""

import os

MAX_ENTRY_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "One star for a planet whose chairs fit only two legs and whose locals "
    "stare when I eat with all four hands, but the noodles alone were worth "
    "crossing three galaxies for."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_ENTRY_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, max {MAX_ENTRY_CHARS}")
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
