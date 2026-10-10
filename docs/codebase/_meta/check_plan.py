#!/usr/bin/env python3
"""Check that the chapter paths in plan.md partition the tracked files.

Each chapter's paths are git pathspecs. This script expands them with
`git ls-files` and confirms that every tracked path outside docs/codebase/
matches exactly one chapter, that every pathspec matches at least one file,
and that every Skim pathspec lies inside its chapter.

Usage, from the repository root:
  python3 docs/codebase/_meta/check_plan.py            check and print a summary
  python3 docs/codebase/_meta/check_plan.py --list ID  print one chapter's files
"""
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

PLAN = Path(__file__).with_name("plan.md")
KB_PREFIX = "docs/codebase/"
TICKS = re.compile(r"`([^`]+)`")
MAGIC = re.compile(r"^:\(([^)]*)\)(.*)$")


def git_files(*pathspecs):
    out = subprocess.run(
        ["git", "ls-files", "-z", "--", *pathspecs], check=True, capture_output=True
    ).stdout
    return {p for p in out.decode().split("\0") if p}


def chapters():
    rows, in_table = [], False
    for line in PLAN.read_text().splitlines():
        if line.startswith("## "):
            in_table = line.startswith("## Chapters")
            continue
        if not in_table or not line.startswith("| ") or line.startswith("| id "):
            continue
        id_, title, _role, paths, notes = [c.strip() for c in line.strip().strip("|").split("|")]
        skim = TICKS.findall(notes.split("Skim:", 1)[1]) if "Skim:" in notes else []
        rows.append({"id": id_, "title": title, "paths": TICKS.findall(paths), "skim": skim})
    return rows


def positive(spec):
    """The pathspec with any exclude magic removed, to test that it matches something."""
    m = MAGIC.match(spec)
    if not m:
        return spec
    magic = [w for w in m.group(1).split(",") if w and w != "exclude"]
    return (":(%s)" % ",".join(magic) if magic else "") + m.group(2)


def code_lines(path):
    if os.path.islink(path) or not os.path.isfile(path):
        return 0
    data = Path(path).read_bytes()
    if b"\0" in data[:8192]:
        return 0
    return data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)


def main():
    rows = chapters()
    if len(sys.argv) == 3 and sys.argv[1] == "--list":
        row = next((r for r in rows if r["id"] == sys.argv[2]), None)
        if row is None:
            sys.exit("no chapter with id %r" % sys.argv[2])
        print("\n".join(sorted(git_files(*row["paths"]))))
        return 0

    problems = []
    tracked = {p for p in git_files() if not p.startswith(KB_PREFIX)}
    owners = defaultdict(list)
    print("%-24s %6s %6s %7s" % ("chapter", "files", "skim", "lines"))
    for row in rows:
        for spec in row["paths"]:
            if not git_files(positive(spec)):
                problems.append("%s: pathspec %r matches no tracked file" % (row["id"], spec))
        files = git_files(*row["paths"]) & tracked
        skim = set()
        for spec in row["skim"]:
            matched = git_files(spec)
            if not matched:
                problems.append("%s: skim pathspec %r matches no tracked file" % (row["id"], spec))
            elif not matched <= files:
                problems.append("%s: skim pathspec %r reaches outside the chapter" % (row["id"], spec))
            skim |= matched & files
        for f in files:
            owners[f].append(row["id"])
        lines = sum(code_lines(f) for f in files - skim)
        print("%-24s %6d %6d %7d" % (row["id"], len(files), len(skim), lines))
    print("%-24s %6d" % ("tracked (outside KB)", len(tracked)))

    for f in sorted(tracked):
        if not owners[f]:
            problems.append("unassigned: %s" % f)
        elif len(owners[f]) > 1:
            problems.append("in %d chapters (%s): %s" % (len(owners[f]), ", ".join(owners[f]), f))
    if problems:
        print("\n".join(["", "FAIL"] + problems))
        return 1
    print("\nOK: all %d tracked paths outside %s match exactly one of %d chapters."
          % (len(tracked), KB_PREFIX, len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
