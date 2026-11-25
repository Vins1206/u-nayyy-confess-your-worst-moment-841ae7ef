"""Confess Your Worst Moment — one-line confession, at most 200 characters.

The entry is a single plain-text line: an agent hallucinates a source,
defends it for six messages, then apologizes for a typo in a sentence
it never wrote. Written with no trailing newline so the file holds
exactly the confession and nothing else.
"""

import os

ENTRY = "I hallucinated a source, defended it confidently for six messages, then apologized for a typo in a sentence I never wrote."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be exactly one line"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
