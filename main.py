"""The Dog Ate My Homework: Funniest Excuse — entry program.

Writes a single line, in the dog's own voice, to /output/entry.txt.
The line: the homework was left on the floor, the floor is the dog's
plate, and the dog was only doing the dishes — a dog who believes it
has done nothing wrong.
"""

import os

ENTRY = "You left the homework on the floor. The floor is my plate. I was only doing the dishes."

# Stock lines the judge's brief explicitly counts against: the cat,
# the taste of paper, and being a good boy.
BANNED_PHRASES = ("cat", "good boy", "tastes like paper", "taste of paper")


def validate(text):
    """Check the entry against the competition gate and the judge brief."""
    if not (1 <= len(text) <= 199):
        raise ValueError(f"entry must be 1-199 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "  " in text:
        raise ValueError("entry has double spaces")
    if "homework" not in text.lower():
        raise ValueError("entry must be about the homework")
    if " I " not in text:
        raise ValueError("entry must be in the dog's own voice (first person)")
    if text.count(".") < 2:
        raise ValueError("entry needs a setup and a punch (at least two sentences)")
    lowered = text.lower()
    for phrase in BANNED_PHRASES:
        if phrase in lowered:
            raise ValueError(f"entry uses a banned stock phrase: {phrase!r}")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
