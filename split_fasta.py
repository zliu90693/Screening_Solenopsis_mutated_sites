from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import os

# 将红火蚁fasta格式文件中的基因逐个提取出来，分成若干个小fasta文件，一个文件一个基因
invicta_genes_splited = "/root/pipeline/splited_from_gb/invicta_genes_extracted.fasta"
invicta_genes = list(SeqIO.parse(invicta_genes_splited, "fasta"))

for gene in invicta_genes:
    gene_name = gene.description.replace(" ","_")
    sequence = gene.seq

    query_fasta = f"/root/pipeline/splited_from_fasta/{gene_name}.fasta"
    record = SeqRecord(sequence, id=gene_name, description="")

    with open(query_fasta, "w") as f:
        SeqIO.write(record, f, "fasta")
