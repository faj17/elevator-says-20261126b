"""What the Elevator Would Say — make.fun entry.

Writes the entry line to /output/entry.txt.
"""

SETUP = "I know where you live. I take you there every day,"
PUNCH = "and I have never once complained."


def assemble():
    return SETUP + " " + PUNCH


def validate(text):
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1-120 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    line = validate(assemble())
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
