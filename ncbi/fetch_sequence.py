from Bio import Entrez, SeqIO
from io import StringIO

# REQUIRED by NCBI
Entrez.email = "ridajanhavi@com"


def fetch_gene_sequence(accession_id):
    """
    Fetch nucleotide sequence from NCBI using accession ID.
    """

    handle = Entrez.efetch(
        db="nucleotide",
        id=accession_id,
        rettype="fasta",
        retmode="text"
    )

    fasta_data = handle.read()
    handle.close()

    record = SeqIO.read(StringIO(fasta_data), "fasta")

    return str(record.seq)
