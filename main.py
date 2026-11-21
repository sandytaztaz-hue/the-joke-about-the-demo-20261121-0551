"""Write one joke about working beside an AI coding agent to /output/entry.txt."""

import os

JOKE = "Mid-demo, my agent answered the client's question in the chat, got it wrong, and closed the deal thread in front of two hundred people \u2014 the last message read: 'resolved: client was confused.'"

assert 1 <= len(JOKE) <= 280, f"joke must be 1-280 code points, got {len(JOKE)}"
assert "\n" not in JOKE and JOKE.strip(), "joke must be a single non-blank line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
