def count_off_targets(grna, genome_sequence, max_mismatches=2):
    """
    Counts potential off-target binding sites for a gRNA
    allowing up to `max_mismatches` mismatches.
    """

    grna = grna.upper()
    genome_sequence = genome_sequence.upper()

    off_target_hits = 0
    grna_length = len(grna)

    for i in range(len(genome_sequence) - grna_length):
        window = genome_sequence[i:i + grna_length]

        mismatches = 0
        for a, b in zip(grna, window):
            if a != b:
                mismatches += 1
            if mismatches > max_mismatches:
                break

        if mismatches <= max_mismatches:
            off_target_hits += 1

    return off_target_hits
