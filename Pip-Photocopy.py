#!/usr/bin/env python
"""
Export the exact state of the current Python environment into:
  - Pip-Photocopy/pyenv_clone.txt : complete list of packages + versions
  - Pip-Photocopy/install_env.sh  / install_env.bat : script to recreate it

/!\  The script finishes with a pause so the window stays open until you press a key.
"""
from pathlib import Path
import platform, subprocess, sys, textwrap

# ─── 1. Where to drop the files ────────────────────────────────────────────────
ROOT_DIR      = Path(__file__).resolve().parent
TARGET_FOLDER = ROOT_DIR / "Pip-Photocopy"
TARGET_FOLDER.mkdir(exist_ok=True)

SNAPSHOT_FILE = TARGET_FOLDER / "pyenv_clone.txt"

# ─── 2. Freeze the environment ─────────────────────────────────────────────────
print("• Capturing current environment with `pip freeze` …")
reqs = subprocess.check_output(
    [sys.executable, "-m", "pip", "freeze"], text=True, encoding="utf-8"
)
SNAPSHOT_FILE.write_text(reqs)
print(f"  → {SNAPSHOT_FILE}  ({len(reqs.splitlines())} packages)")

# ─── 3. Create the re-installation script ─────────────────────────────────────
if platform.system() == "Windows":
    installer = TARGET_FOLDER / "install_env.bat"
    content = textwrap.dedent(fr"""
        @echo off
        REM Update pip
        python -m pip install --upgrade pip

        REM Install dependencies
        python -m pip install -r "%~dp0pyenv_clone.txt"
    """)
else:
    installer = TARGET_FOLDER / "install_env.sh"
    content = textwrap.dedent("""\
        #!/usr/bin/env bash
        # Update pip
        python -m pip install --upgrade pip

        # Install dependencies
        python -m pip install -r "$(dirname "$0")/pyenv_clone.txt"
    """)
    installer.chmod(0o755)  # Make it executable on Unix

installer.write_text(content.lstrip())
print(f"  → {installer}")

# ─── 4. Pause before exit ──────────────────────────────────────────────────────
input("\nDone! Press Enter to close this window…")
