#!/bin/bash
species=database/geminata/geminata_db
genes=splited_from_fasta/ATP_synthase_F0_subunit_6_2615_3281.fasta
species_basename=$(basename $species _db)
genes_basename=$(basename "$genes" .fasta)
blastn -query $genes -db $species -out blast_output/$genes_basename/$species_basename/${species_basename}_${genes_basename}.txt