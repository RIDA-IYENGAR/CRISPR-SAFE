from grna_design.grna_finder import find_grnas
from off_target.off_target_analysis import count_off_targets
from scoring.risk_score import gc_content, crispr_safe_score

gene_sequence = "ATGCGTACGTAGCTAGCTAGCGGATCGTACGATCGTAGCGG"
background_genome = "ATGCGTACGTAGCTAGCTAGCGGATCGTACGATCGTAGCGGATGCGTACGTAGCTAGCTAG"

grnas = find_grnas(gene_sequence)

for g in grnas:
    grna_seq = g["guide_rna"]

    gc = gc_content(grna_seq)
    off_targets = count_off_targets(grna_seq, background_genome)

    score = crispr_safe_score(gc, off_targets)

    print("gRNA:", grna_seq)
    print(score)
    print("=" * 50)
