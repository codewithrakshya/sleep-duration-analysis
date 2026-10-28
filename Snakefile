configfile: "config/analysis.yaml"

RESULTS = config["outputs"]["results_dir"]

rule all:
    input:
        f"{RESULTS}/01_qc/fuma_qc.tsv",
        f"{RESULTS}/02_locus_overlap/source_overlap.tsv",
        f"{RESULTS}/03_catalog_overlap/catalog_overlap.tsv",
        f"{RESULTS}/04_gene_prioritization/novel_locus_genes.tsv",
        f"{RESULTS}/05_functional_summary/fuma_functional_summary.tsv",
        f"{RESULTS}/06_annotation_qc/annotation_summary.tsv",
        f"{RESULTS}/07_final/novel_loci_and_genes.tsv"

rule qc_fuma:
    output: f"{RESULTS}/01_qc/fuma_qc.tsv"
    shell: "python scripts/01_qc_fuma.py --config config/analysis.yaml --output {output}"

rule compare_loci:
    input: rules.qc_fuma.output
    output: f"{RESULTS}/02_locus_overlap/source_overlap.tsv"
    shell: "python scripts/02_compare_loci.py --config config/analysis.yaml --output {output}"

rule catalog_overlap:
    input: rules.compare_loci.output
    output: f"{RESULTS}/03_catalog_overlap/catalog_overlap.tsv"
    shell: "python scripts/03_catalog_overlap.py --config config/analysis.yaml --output {output}"

rule prioritize_genes:
    input: rules.catalog_overlap.output
    output: f"{RESULTS}/04_gene_prioritization/novel_locus_genes.tsv"
    shell: "python scripts/04_prioritize_genes.py --config config/analysis.yaml --output {output}"

rule summarize_fuma:
    input: rules.qc_fuma.output
    output: f"{RESULTS}/05_functional_summary/fuma_functional_summary.tsv"
    shell: "python scripts/05_summarize_fuma.py --config config/analysis.yaml --output {output}"

rule annotation_qc:
    input: rules.qc_fuma.output
    output: f"{RESULTS}/06_annotation_qc/annotation_summary.tsv"
    shell: "python scripts/06_annotation_qc.py --config config/analysis.yaml --output {output}"

rule join_results:
    input:
        novel_genes=rules.prioritize_genes.output,
        functional=rules.summarize_fuma.output,
        annotations=rules.annotation_qc.output
    output: f"{RESULTS}/07_final/novel_loci_and_genes.tsv"
    shell: "python scripts/07_join_results.py --config config/analysis.yaml --output {output}"
