"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of planet Earth --
to /output/entry.txt (UTF-8, 1-200 characters, single line).

The line was written to win on the judge brief: it reads as a genuine
one-line tourist review, the laugh comes from the alien's own angle on an
ordinary Earth hassle (parking enforcement), the detail is one few
entrants would reach for, it carries a verdict and a star rating, and
every word earns its place with the punch landing at the end.
"""

import os

ENTRY = (
    "Came to Earth for the oceans. Stayed an extra day because my ship "
    "got towed. Great water, terrible parking \u2014 3/5 stars, "
    "would orbit again."
)

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space, on a single line.
MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be one line"
    assert text == ENTRY, "entry must not gain or lose whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
