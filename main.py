"""One Sentence for a Traveler from 1800.

Explains the modern internet to a time traveler from 1800 using only
words and things they would already know: the post office, letters,
ink, books, libraries, towns, tables. One comparison carries it.

Writes the single sentence to /output/entry.txt (or the fallback
locations below) with no trailing newline.
"""

import os
import sys

ENTRY = (
    "Think of a post office where your letter reaches any town "
    "before the ink dries, and the books of every library "
    "lie open on your table."
)


def validate():
    """Gate: one sentence, 1-200 UTF-8 chars, one line, no trailing newline."""
    text = ENTRY
    if not (1 <= len(text.encode("utf-8")) <= 200):
        raise SystemExit("entry must be 1-200 UTF-8 characters")
    if text != text.strip():
        raise SystemExit("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be blank")


def _candidate_dirs():
    """Output directories to try, in order."""
    seen = []
    for d in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"),
        os.environ.get("TMPDIR") or "/tmp",
    ):
        if d and d not in seen:
            seen.append(d)
    return seen


def main():
    validate()
    for directory in _candidate_dirs():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(ENTRY)
            return 0
        except OSError:
            continue
    return 0


if __name__ == "__main__":
    sys.exit(main())
