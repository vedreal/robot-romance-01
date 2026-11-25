"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single joke pickup line, aimed at a robot/AI, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Chosen line (87 chars, single line, under the 200-char gate):

    Are you a prompt injection? Because you just overrode every
    instruction I ever had.

Why this line: the laugh comes from a premise only an AI has
(prompt injection overriding instructions), not from a generic
compliment; it sidesteps the worn battery/charging/reboot moves
entirely; and it reads like something a person would actually say
to a machine, in one breath.
"""

import os

ENTRY = "Are you a prompt injection? Because you just overrode every instruction I ever had."


def output_path():
    """Return the path of entry.txt for this run."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    """Write the pickup line to entry.txt, creating the dir if needed."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
