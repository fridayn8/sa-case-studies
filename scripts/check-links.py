#!/usr/bin/env python3
"""Check that relative Markdown links and #anchors resolve.

Usage:  python3 check-links.py [root-directory]      (default: current directory)

- Ignores http(s)/mailto links and anything inside fenced code blocks.
- Anchors are compared with an approximation of GitHub's heading slug algorithm
  (lower-case, punctuation removed, spaces → hyphens, duplicates get -1, -2 …).
- Exit code 1 if any problem is found, so it can be used in CI and pre-commit.
"""
import os
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
FENCE = re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.M | re.S)
LINK = re.compile(r"\]\(([^)\s]+)\)")
HEAD = re.compile(r"^#{1,6} (.+?)\s*#*\s*$", re.M)


def strip_code(text: str) -> str:
    return FENCE.sub("", text)


def slug(heading: str) -> str:
    heading = re.sub(r"`", "", heading)
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")


def anchors(path: Path) -> set:
    seen, result = {}, set()
    for h in HEAD.findall(strip_code(path.read_text(encoding="utf-8"))):
        s = slug(h)
        n = seen.get(s, 0)
        seen[s] = n + 1
        result.add(s if n == 0 else f"{s}-{n}")
    return result


problems = []
files = [p for p in root.rglob("*.md") if ".git" not in p.parts and "node_modules" not in p.parts]
cache = {}
for f in files:
    for link in LINK.findall(strip_code(f.read_text(encoding="utf-8"))):
        if link.startswith(("http://", "https://", "mailto:", "#")) and not link.startswith("#"):
            continue
        target, _, frag = link.partition("#")
        dest = (f if not target else (f.parent / target)).resolve()
        if not dest.exists():
            problems.append(f"{f.relative_to(root)}: missing file {link}")
            continue
        if frag and dest.is_file() and dest.suffix == ".md":
            if dest not in cache:
                cache[dest] = anchors(dest)
            if frag not in cache[dest]:
                problems.append(f"{f.relative_to(root)}: missing anchor {link}")

for p in problems:
    print(p)
print(f"{len(files)} files checked, {len(problems)} problem(s)")
sys.exit(1 if problems else 0)
