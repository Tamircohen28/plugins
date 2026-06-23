#!/usr/bin/env python3
"""Bump version in the canonical Claude marketplace manifest."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CLAUDE_MANIFEST = REPO_ROOT / ".claude-plugin" / "marketplace.json"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: bump-marketplace-version.py <version>", file=sys.stderr)
        return 1

    version = sys.argv[1]
    with CLAUDE_MANIFEST.open(encoding="utf-8") as f:
        data = json.load(f)
    data["version"] = version
    with CLAUDE_MANIFEST.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"Version bumped to {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
