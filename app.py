from grna_design.grna_finder import find_grnas
from off_target.off_target_analysis import count_off_targets

gene_sequence = "ATGCGTACGTAGCTAGCTAGCGGATCGTACGATCGTAGCGG"
background_genome = "ATGCGTACGTAGCTAGCTAGCGGATCGTACGATCGTAGCGGATGCGTACGTAGCTAGCTAG"

grnas = find_grnas(gene_sequence)

for g in grnas:
    hits = count_off_targets(g["guide_rna"], background_genome)
    print("gRNA:", g["guide_rna"])
    print("Off-target hits:", hits)
    print("-" * 40)

