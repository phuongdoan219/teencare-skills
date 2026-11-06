"""Install the three bundled TeenCare skills; Python 3.9+, no extra packages."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from datetime import datetime

ROOT = Path(__file__).resolve().parent
NAMES = ("teencare-video-editor", "teencare-scriptwriter", "content-webinar-teencare")


def verify():
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    actual = {p.relative_to(ROOT).as_posix(): p for p in (ROOT / "skills").rglob("*") if p.is_file()}
    if set(actual) != set(manifest["files"]):
        raise ValueError("Skill file list differs from manifest.json; use a fresh checkout.")
    for relative, path in actual.items():
        if path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest() != manifest["files"][relative]:
            raise ValueError(f"Integrity check failed: {relative}")
    for name in NAMES:
        if not (ROOT / "skills" / name / "SKILL.md").is_file():
            raise ValueError(f"Missing SKILL.md: {name}")
    return len(actual)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    default_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    parser.add_argument("--dest", type=Path, default=default_home / "skills", help="Skills directory (default: CODEX_HOME/skills or ~/.codex/skills)")
    parser.add_argument("--replace", action="store_true", help="Back up existing skills before replacing them")
    parser.add_argument("--check", action="store_true", help="Verify bundled file hashes without installing")
    args = parser.parse_args()
    count = verify()
    print(f"Verified {len(NAMES)} skills, {count} files.")
    if args.check:
        return 0
    dest = args.dest.expanduser().resolve()
    source = (ROOT / "skills").resolve()
    if dest == source or source in dest.parents or dest in source.parents:
        raise ValueError("Installation destination must be separate from the repository's skills directory.")
    existing = [name for name in NAMES if (dest / name).exists() or (dest / name).is_symlink()]
    if existing and not args.replace:
        raise ValueError("Already installed: " + ", ".join(existing) + ". Run with --replace to back up and update.")
    if any((dest / name).is_symlink() for name in NAMES):
        raise ValueError("A destination skill is a symlink; choose another --dest.")
    dest.mkdir(parents=True, exist_ok=True)
    backup_root = dest.parent / "skill-backups" / ("teencare-" + datetime.now().strftime("%Y%m%d-%H%M%S-%f"))
    with tempfile.TemporaryDirectory(prefix=".teencare-stage-", dir=dest.parent) as stage_dir:
        stage = Path(stage_dir)
        for name in NAMES:
            shutil.copytree(source / name, stage / name)
        installed, saved = [], []
        try:
            for name in NAMES:
                target = dest / name
                if name in existing:
                    backup_root.mkdir(parents=True, exist_ok=True)
                    target.rename(backup_root / name)
                    saved.append(name)
                (stage / name).rename(target)
                installed.append(name)
        except OSError:
            for name in reversed(installed):
                (dest / name).rename(stage / name)
            for name in reversed(saved):
                (backup_root / name).rename(dest / name)
            raise
    for name in NAMES:
        print(f"Installed: {dest / name}")
    if saved:
        print(f"Previous versions backed up: {backup_root}")
    print("Restart Codex to discover the installed skills. See README.md for video dependencies and machine paths.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
