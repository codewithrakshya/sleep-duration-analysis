#!/usr/bin/env python3
"""Stage 5: extract MAGMA, pathway, and tissue summaries from FUMA."""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("category\ttest\tn\tp_value\tfdr\n", encoding="utf-8")
    print(f"Skeleton stage complete: {args.config} -> {output}")


if __name__ == "__main__":
    main()
