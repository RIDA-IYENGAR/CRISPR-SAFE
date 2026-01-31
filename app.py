import streamlit as st

from ncbi.fetch_sequence import fetch_gene_sequence
from grna_design.grna_finder import find_grnas
from off_target.off_target_analysis import count_off_targets
from scoring.risk_score import gc_content, crispr_safe_score

# ---------- UI ----------
st.set_page_config(page_title="CRISPR-SAFE", layout="wide")

st.title("🧬 CRISPR-SAFE")
st.subheader("Explainable CRISPR gRNA Safety Analysis Tool")

st.markdown("""
CRISPR-SAFE designs CRISPR-Cas9 guide RNAs and evaluates their **off-target risk**
using real gene sequences fetched directly from **NCBI**.
""")

# ---------- USER INPUT ----------
accession_id = st.text_input(
    "Enter NCBI Gene Accession ID",
    value="NM_000546",
    help="Example: NM_000546 (TP53)"
)

analyze_button = st.button("🔍 Analyze Gene")

# ---------- PROCESS ----------
if analyze_button:
    with st.spinner("Fetching gene sequence from NCBI..."):
        try:
            gene_sequence = fetch_gene_sequence(accession_id)
            gene_sequence = gene_sequence[:300]  # limit for demo
            background_genome = gene_sequence * 2
        except Exception as e:
            st.error("Failed to fetch gene from NCBI.")
            st.stop()

    st.success("Gene sequence retrieved successfully!")

    grnas = find_grnas(gene_sequence)

    st.write(f"### Total gRNAs found: {len(grnas)}")

    if len(grnas) == 0:
        st.warning("No valid Cas9 gRNAs found in this region.")
    else:
        for g in grnas[:5]:
            grna_seq = g["guide_rna"]

            gc = gc_content(grna_seq)
            off_targets = count_off_targets(grna_seq, background_genome)
            score = crispr_safe_score(gc, off_targets)

            st.markdown("---")
            st.write(f"**gRNA Sequence:** `{grna_seq}`")
            st.json(score)
