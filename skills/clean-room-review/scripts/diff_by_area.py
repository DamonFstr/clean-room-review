"""Count lines added between two git refs, bucketed by area and split into source and tests."""

import argparse
import re
import subprocess
import sys
from collections import defaultdict


def parse_area(spec: str) -> tuple[str, re.Pattern]:
    name, sep, pattern = spec.partition("=")
    if not sep or not name or not pattern:
        raise argparse.ArgumentTypeError(f"--area must be NAME=REGEX, got {spec!r}")
    return name, re.compile(pattern)


def numstat(repo: str, base: str, head: str) -> list[tuple[int, str]]:
    out = subprocess.run(
        ["git", "-C", repo, "diff", "--numstat", base, head],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    rows = []
    for line in out.splitlines():
        added, _deleted, path = line.split("\t", 2)
        if added == "-":  # binary file
            continue
        rows.append((int(added), path))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--base", required=True, help="usually the merge base with trunk")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--area", action="append", type=parse_area, default=[], help="NAME=REGEX; first match wins")
    parser.add_argument("--test-regex", default=r"test|spec", help="a path matching this counts as tests")
    args = parser.parse_args()

    test_pattern = re.compile(args.test_regex)
    totals: dict[str, dict[str, int]] = defaultdict(lambda: {"source": 0, "tests": 0})
    for added, path in numstat(args.repo, args.base, args.head):
        area = next((name for name, pattern in args.area if pattern.search(path)), "other")
        totals[area]["tests" if test_pattern.search(path) else "source"] += added

    order = [name for name, _ in args.area if name in totals] + (["other"] if "other" in totals else [])
    width = max([len(name) for name in order] + [5])
    print(f"{'area':<{width}}  {'source':>8}  {'tests':>8}")
    for name in order:
        print(f"{name:<{width}}  {totals[name]['source']:>8,}  {totals[name]['tests']:>8,}")
    source = sum(t["source"] for t in totals.values())
    tests = sum(t["tests"] for t in totals.values())
    print(f"{'total':<{width}}  {source:>8,}  {tests:>8,}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
