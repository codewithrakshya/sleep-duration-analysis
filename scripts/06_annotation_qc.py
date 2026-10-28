#!/usr/bin/env python3
"""Stage 6: normalize and QC FUMA ANNOVAR annotation categories."""

import argparse
from pathlib import Path

CATEGORIES = (
    "exonic", "intronic", "intergenic", "upstream", "downstream",
    "UTR", "ncRNA", "other",
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("trait\tannotation_category\tcount\tproportion\n", encoding="utf-8")
    print(f"Skeleton stage complete: {args.config} -> {output}")


if __name__ == "__main__":
    main()
