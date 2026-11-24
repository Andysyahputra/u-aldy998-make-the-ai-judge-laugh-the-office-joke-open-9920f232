"""Make the AI Judge Laugh: the Office Joke Open.

Writes a single original one-line office joke to /output/entry.txt.
Deterministic: no randomness, no network, no input.
"""

from pathlib import Path

JOKE = (
    "I renamed the weekly sync 'optional' and attendance tripled \u2014 "
    "turns out the only thing worse than a meeting is missing one."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the sealed scorer's gate: 1-200 UTF-8 chars, not only whitespace."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")


def main() -> None:
    validate(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
