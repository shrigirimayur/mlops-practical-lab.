from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pandas as pd


def dvc_executable() -> str:
    executable = shutil.which("dvc")
    if executable:
        return executable
    local_executable = Path(sys.executable).parent / "dvc.exe"
    if local_executable.exists():
        return str(local_executable)
    raise SystemExit("Install DVC in this Python environment, then retry.")


def run(command: list[str], cwd: Path) -> str:
    result = subprocess.run(
        command,
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(
            f"Command failed ({result.returncode}): {command}\n{result.stderr}"
        )
    return result.stdout.strip()


def main() -> None:
    dvc = dvc_executable()
    if shutil.which("git") is None:
        raise SystemExit("Install Git, then run this practical again.")

    temporary_path: Path
    with tempfile.TemporaryDirectory(
        prefix="dvc-practical-", ignore_cleanup_errors=True
    ) as temporary:
        temporary_path = Path(temporary)
        root = Path(temporary) / "project"
        remote = Path(temporary) / "remote"
        root.mkdir()
        shutil.copy2(Path(__file__).with_name("create_dataset.py"), root)

        run(["git", "init", "-q"], root)
        run(["git", "config", "user.name", "MLOps Practical"], root)
        run(["git", "config", "user.email", "mlops-practical@example.invalid"], root)
        run(["git", "config", "maintenance.auto", "false"], root)
        run([dvc, "init", "-q"], root)
        run([sys.executable, "create_dataset.py"], root)
        run([dvc, "add", "data/students.csv"], root)
        run(["git", "add", "-A"], root)
        run(["git", "commit", "-qm", "Track first dataset version"], root)
        run([dvc, "remote", "add", "-d", "local", str(remote)], root)
        run([dvc, "push"], root)

        first_hash = run(["git", "show", "HEAD:data/students.csv.dvc"], root)
        dataset = pd.read_csv(root / "data" / "students.csv")
        dataset.loc[len(dataset)] = [6, 6.0, 91, "Pass"]
        dataset.to_csv(root / "data" / "students.csv", index=False)
        run([dvc, "add", "data/students.csv"], root)
        run(["git", "add", "-A"], root)
        run(["git", "commit", "-qm", "Track second dataset version"], root)
        second_hash = run(["git", "show", "HEAD:data/students.csv.dvc"], root)
        run([dvc, "push"], root)

        (root / "data" / "students.csv").unlink()
        run([dvc, "pull"], root)
        restored_rows = len(pd.read_csv(root / "data" / "students.csv"))

        print(f"DVC version: {run([dvc, '--version'], root)}")
        print("Remote: temporary local directory")
        print("First version metadata:")
        print(first_hash)
        print("Second version metadata:")
        print(second_hash)
        print(f"Dataset hash changed: {first_hash != second_hash}")
        print(f"Rows restored after dvc pull: {restored_rows}")
        print("Git status:")
        print(run(["git", "status", "--short"], root) or "clean")

    if temporary_path.exists():
        print("Windows deferred cleanup of the locked temporary workspace outside this folder.")
    else:
        print("Temporary demo repository and local remote were removed.")


if __name__ == "__main__":
    main()
