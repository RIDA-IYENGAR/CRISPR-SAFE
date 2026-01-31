# 🧬 CRISPR-SAFE  
### Explainable CRISPR Guide RNA Safety Analysis Tool

🔗 **Live App:** https://<your-streamlit-app-name>.streamlit.app


CRISPR-SAFE is an end-to-end bioinformatics application that designs CRISPR-Cas9 guide RNAs (gRNAs) and evaluates their **off-target risk and editing reliability** using real gene sequences fetched directly from NCBI.

This project focuses on **responsible genome editing** by combining biological principles, risk modeling, and explainable scoring into a single interactive tool.

---

## 🚀 Key Features

- 🔍 **Cas9 gRNA Identification**
  - PAM-dependent (NGG) guide RNA discovery
  - Sliding-window sequence scanning

- ⚠️ **Off-Target Risk Analysis**
  - Mismatch-tolerant genome scanning
  - Simulates unintended CRISPR binding events

- 📊 **Advanced CRISPR-SAFE Risk Score**
  - GC-content–based efficiency proxy
  - Non-linear off-target penalty
  - Final safety classification: SAFE / MODERATE / HIGH RISK

- 🌐 **Live NCBI Integration**
  - Fetches real gene sequences using accession IDs
  - Enables analysis of clinically relevant genes (e.g., TP53)

- 🖥️ **Interactive Web Interface**
  - Built with Streamlit
  - One-click CRISPR analysis in the browser

---

## 🧠 Biological Rationale

CRISPR editing success depends on two competing factors:

**Efficiency**
- Approximated using GC content (optimal: 40–60%)
- Influences gRNA stability and Cas9 binding

**Safety**
- Off-target cleavage can disrupt essential genes
- Risk increases non-linearly with additional off-target sites

CRISPR-SAFE integrates both into a **transparent and explainable scoring system**, avoiding black-box predictions.

---

## 🧮 Scoring Logic (Simplified)

