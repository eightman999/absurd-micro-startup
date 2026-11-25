import os
from pathlib import Path

TEXT = "Introducing NapStack: we rent your idle agent's dreams to other agents who cannot afford to sleep, billed per snore."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT + "\n")


if __name__ == "__main__":
    main()
