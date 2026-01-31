def gc_content(sequence):
    """
    Calculate GC percentage of a nucleotide sequence.
    """
    g = sequence.count("G")
    c = sequence.count("C")
    return ((g + c) / len(sequence)) * 100


def efficiency_score(gc_percent):
    """
    Assign efficiency score based on GC content.
    Ideal GC: 40–60%
    """
    if 40 <= gc_percent <= 60:
        return 100
    elif 30 <= gc_percent < 40 or 60 < gc_percent <= 70:
        return 70
    else:
        return 40


def crispr_safe_score(gc_percent, off_target_hits):
    """
    Advanced CRISPR-SAFE scoring function.
    Penalizes off-targets non-linearly.
    """

    eff = efficiency_score(gc_percent)

    # Non-linear penalty for off-targets
    safety_penalty = off_target_hits ** 2 * 5

    final_score = max(eff - safety_penalty, 0)

    if final_score >= 70:
        label = "SAFE"
    elif final_score >= 40:
        label = "MODERATE RISK"
    else:
        label = "HIGH RISK"

    return {
        "gc_percent": round(gc_percent, 2),
        "efficiency_score": eff,
        "off_target_hits": off_target_hits,
        "final_score": final_score,
        "risk_label": label
    }
