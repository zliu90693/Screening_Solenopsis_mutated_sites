#!/bin/bash
for species in old_fasta_gb/*.fasta; do
    species_basename=$(basename $species .fasta)
    makeblastdb -in $species -dbtype nucl -out /root/pipeline/database/${species_basename}/${species_basename}_db
done