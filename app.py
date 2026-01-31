from grna_design.grna_finder import find_grnas

test_sequence = "ATGCGTACGTAGCTAGCTAGCGGATCGTACGATCGTAGCGG"

grnas = find_grnas(test_sequence)

for g in grnas:
    print(g)
