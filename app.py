from ncbi.fetch_sequence import fetch_gene_sequence
from grna_design.grna_finder import find_grnas
from off_target.off_target_analysis import count_off_targets
from scoring.risk_score import gc_content, crispr_safe_score

# Example: Human TP53 gene
accession_id = "NM_000546"

print("Fetching gene from NCBI:", accession_id)
gene_sequence = fetch_gene_sequence(accession_id)

# Use a small region for demo (first 300 bp)
gene_sequence = gene_sequence[:300]

background_genome = gene_sequence * 2

grnas = find_grnas(gene_sequence)

print(f"Total gRNAs found: {len(grnas)}")
print("=" * 60)

for g in grnas[:5]:  # limit output
    grna_seq = g["guide_rna"]

    gc = gc_content(grna_seq)
    off_targets = count_off_targets(grna_seq, background_genome)

    score = crispr_safe_score(gc, off_targets)

    print("gRNA:", grna_seq)
    print(score)
    print("-" * 60)
