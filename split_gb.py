from Bio import SeqIO

#将红火蚁的各个基因从gb中提取出来，写入一个fasta文件
gb_file = "/root/pipeline/old_fasta_gb/invicta.gb"  # 你的 GenBank 文件名
output_fasta = "/root/pipeline/splited_from_gb/invicta_genes_extracted.fasta"  # 输出的 FASTA 文件名

# 读取 GenBank 文件
with open(gb_file, "r") as gb_handle:
    gb_record = SeqIO.read(gb_handle, "genbank")

# 打开输出的 FASTA 文件
with open(output_fasta, "w") as out_handle:
    for feature in gb_record.features:
        if feature.type == "CDS" or feature.type == "tRNA":
            gene_name = feature.qualifiers.get("product", ["unknown"])[0]
            start = feature.location.start
            end = feature.location.end
            strand = feature.location.strand

            # 提取基因序列
            gene_seq = gb_record.seq[start:end]

            if strand == -1:
                gene_seq = gene_seq.reverse_complement()
            out_handle.write(f">{gene_name}_{start}_{end}\n{gene_seq}\n")