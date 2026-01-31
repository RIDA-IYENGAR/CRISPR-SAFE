def find_grnas(sequence, length=20):
    """
    Identify CRISPR-Cas9 guide RNAs using NGG PAM.
    """

    sequence = sequence.upper()
    grnas = []

    for i in range(len(sequence) - length - 2):
        guide = sequence[i:i + length]
        pam = sequence[i + length:i + length + 3]

        if pam.endswith("GG"):
            grnas.append({
                "guide_rna": guide,
                "pam": pam,
                "position": i
            })

    return grnas
