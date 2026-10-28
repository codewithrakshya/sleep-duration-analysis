#!/usr/bin/env bash
#SBATCH --job-name=sleep_gctb
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=16G
#SBATCH --output=results/gctb-%j.log

set -euo pipefail

trait_config=${1:?Usage: sbatch gctb_trait.sbatch <trait.yaml>}
echo "Trait configuration: $trait_config"

# TODO: Load the Core HPC module environment and run GCTB.
# Write the normalized heritability estimate, standard error, and CI to results.
