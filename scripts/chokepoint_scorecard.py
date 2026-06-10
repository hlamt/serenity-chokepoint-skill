#!/usr/bin/env python3
"""Print the offline chokepoint scorecard field guide."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCORECARD_PATH = ROOT / "assets" / "chokepoint-scorecard.json"


def load_scorecard() -> dict:
    with SCORECARD_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def print_template(data: dict) -> None:
    scale = data["scale"]
    print("Supply-chain chokepoint scorecard template")
    print(f"Scale: {scale['min']}-{scale['max']}")
    print(f"Note: {scale['meaning']}")
    print()
    for name, item in data["dimensions"].items():
        score_range = item["score_range"]
        print(
            f"{name} [{score_range[0]}-{score_range[1]}, {item['polarity']}]: "
            f"{item['description']}"
        )
    print()
    print("Negative-polarity dimensions are risk items and must not be added directly to positive opportunity scores.")
    print(f"Source: {SCORECARD_PATH.relative_to(ROOT)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect the local supply-chain chokepoint scorecard."
    )
    parser.add_argument(
        "--template",
        action="store_true",
        help="Print scorecard field names and descriptions.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.template:
        print("Use --template to print the scorecard field guide.")
        return 0
    print_template(load_scorecard())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
