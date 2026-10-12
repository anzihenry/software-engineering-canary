from __future__ import annotations

import subprocess
from pathlib import Path

PIN = "eb674f606ba36b6b8e5b7da3c00c40b915c49f17"
BASE = "a37d46a346b0d955d99db1c55aa65df1fb281a71"


def run(args: list[str]) -> None:
    result = subprocess.run(args, check=False, timeout=120)
    if result.returncode:
        raise SystemExit(result.returncode)


def main() -> None:
    shallow = subprocess.check_output(["git", "rev-parse", "--is-shallow-repository"], text=True)
    if shallow.strip() == "true":
        run(["git", "fetch", "--unshallow", "--tags", "origin"])
    run(["git", "fetch", "origin", "main"])
    harness = Path("../pinned-harness")
    if not harness.exists():
        run(["git", "clone", "https://github.com/anzihenry/software-engineering.git", str(harness)])
    run(["git", "-C", str(harness), "checkout", "--detach", PIN])
    actual = subprocess.check_output(["git", "-C", str(harness), "rev-parse", "HEAD"], text=True)
    dirty = subprocess.check_output(["git", "-C", str(harness), "status", "--porcelain"], text=True)
    if actual.strip() != PIN or dirty.strip():
        raise SystemExit("fixed knowledge drift")
    run(
        [
            "python",
            str(harness / "scripts/documentation_check.py"),
            "check",
            "--root",
            ".",
            "--base",
            BASE,
        ]
    )


if __name__ == "__main__":
    main()
