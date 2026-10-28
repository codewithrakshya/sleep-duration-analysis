#!/usr/bin/env bash
set -euo pipefail

# Submit one Core HPC GCTB job per trait.
# Replace this skeletal implementation when trait manifests and the Core HPC scheduler interface are confirmed.

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <trait.yaml>" >&2
  exit 1
fi

trait_config=$1
sbatch hpc/gctb_trait.sbatch "$trait_config"
