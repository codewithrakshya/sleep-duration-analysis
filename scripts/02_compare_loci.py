#!/usr/bin/env python3
"""Stage 2: compare Genomic SEM FUMA loci with source-GWAS FUMA loci."""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("factor_locus\tchr\tstart\tend\texact_source_overlap\tflanked_source_overlap\n", encoding="utf-8")
    print(f"Skeleton stage complete: {args.config} -> {output}")


if __name__ == "__main__":
    main()
