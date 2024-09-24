from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import xml.etree.ElementTree as ET
from pathlib import Path
import os
import shutil

def extract_sbjct_sequences(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()


    for hsp in root.findall(".//Hsp"):
        hseq = hsp.find("Hsp_hseq").text
        # return hseq
        target_object = SeqRecord(Seq(hseq), id=os.path.basename(xml_file).rstrip(".xml"), description="")
        return target_object
    return None
    # with open("/root/pipeline/try.fasta","w") as file:
    #     SeqIO.write(record, file, "fasta")


# xml_file = "/root/pipeline/blast_output/ATP_synthase_F0_subunit_6_2615_3281/geminata.xml"
# extract_sbjct_sequences(xml_file)
if not os.path.isdir("/root/pipeline/combined"):
    # 如果目录A不存在，则复制目录splited_from_fasta到目录combined
    shutil.copytree("/root/pipeline/splited_from_fasta", "/root/pipeline/combined")

for gene_name in Path("/root/pipeline/blast_output").iterdir():
    for species_xml in gene_name.iterdir():
        target_seq = extract_sbjct_sequences(species_xml)
        output_path = f"/root/pipeline/combined/{os.path.basename(gene_name)}.fasta"
        if target_seq:
            with open(output_path, "a") as file:
                SeqIO.write(target_seq, file, "fasta")



# extract_sbjct_sequences("/root/pipeline/blast_output/tRNA-Gly_4084_4156/geminata.xml")