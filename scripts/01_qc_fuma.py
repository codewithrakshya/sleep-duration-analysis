#!/usr/bin/env python3
"""Stage 1: validate and summarize FUMA exports."""

import argparse
from pathlib import Path

REQUIRED_FILES = ("GenomicRiskLoci.txt", "IndSigSNPs.txt", "leadSNPs.txt")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("trait\tstatus\tmessage\n", encoding="utf-8")
    print(f"Skeleton stage complete: {args.config} -> {output}")


if __name__ == "__main__":
    main()
