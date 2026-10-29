#!/usr/bin/env python3
"""Install the complete focused skill set without overwriting existing skills."""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

from validate_repository import EXPECTED, ROOT, validate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, type=Path,
                        help='Explicit user/project skills directory')
    parser.add_argument('--mode', choices=['symlink', 'copy'], default='symlink')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    errors = validate()
    if errors:
        parser.error('Source validation failed: ' + '; '.join(errors))
    source = ROOT/'skills'
    target = args.target.expanduser().absolute()
    if target.resolve().is_relative_to(source.resolve()):
        parser.error('Target must not be inside the source skills directory.')
    if os.path.lexists(target) and not target.is_dir():
        parser.error('Target exists and is not a directory.')
    conflicts = [name for name in sorted(EXPECTED) if os.path.lexists(target/name)]
    if conflicts:
        parser.error('Nothing installed; existing skill destinations: ' + ', '.join(conflicts))
    for name in sorted(EXPECTED):
        print(f'{"PLAN" if args.dry_run else "INSTALL"} {args.mode}: {source/name} -> {target/name}')
    if args.dry_run:
        print('Dry run complete; no files written.')
        return 0

    created: list[Path] = []
    try:
        target.mkdir(parents=True, exist_ok=True)
        for name in sorted(EXPECTED):
            destination = target/name
            if args.mode == 'symlink':
                destination.symlink_to(source/name, target_is_directory=True)
                created.append(destination)
            else:
                # Create first so rollback only removes paths created by this call.
                destination.mkdir()
                created.append(destination)
                shutil.copytree(source/name, destination, dirs_exist_ok=True,
                                ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    except OSError as exc:
        for destination in reversed(created):
            if destination.is_symlink():
                destination.unlink()
            elif destination.is_dir():
                shutil.rmtree(destination)
        print(f'Installation failed; newly created skill entries rolled back: {exc}', file=sys.stderr)
        return 1
    print(f'Installed {len(created)} skills in {target}. Existing unrelated entries were preserved.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
