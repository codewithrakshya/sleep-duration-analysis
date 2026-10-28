# Sleep-duration analysis pipeline

A reproducible pipeline for identifying and interpreting Genomic SEM sleep-duration loci from FUMA outputs.

## Planned stages

1. QC FUMA exports.
2. Compare Genomic SEM loci with Dashti, Austin-Zimmerman, and Portas FUMA loci.
3. Compare candidate-specific loci with the GWAS Catalog.
4. Prioritize mapped and MAGMA-supported genes.
5. Summarize FUMA functional and pathway results.
6. QC ANNOVAR annotation categories and plots.
7. Join final meeting deliverables.

GCTB heritability analyses are intended for Core HPC and are isolated under `hpc/`.

## Usage

Place FUMA exports under `input/fuma/`, then edit `config/analysis.yaml`.

```bash
snakemake --cores 8
```

Submit GCTB jobs separately using the files under `hpc/`.
