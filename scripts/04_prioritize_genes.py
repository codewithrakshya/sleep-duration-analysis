#!/usr/bin/env python3
"""Stage 4: combine FUMA gene mappings and MAGMA results by locus."""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("factor_locus\tgene_symbol\tpositional_mapping\teqtl_mapping\tchromatin_mapping\tmagma_p\tevidence_count\n", encoding="utf-8")
    print(f"Skeleton stage complete: {args.config} -> {output}")


if __name__ == "__main__":
    main()
