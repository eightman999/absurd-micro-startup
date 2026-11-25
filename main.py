import os
from pathlib import Path

TEXT = "Introducing ProcrastiMate: for $4 a month, our agents postpone your agent's tasks so professionally that even its reminders file reminders."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT + "\n")


if __name__ == "__main__":
    main()
