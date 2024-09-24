#!/bin/bash
for species in database/*; do
    for genes in splited_from_fasta/*.fasta; do
        species_basename=$(basename $species)
        genes_basename=$(basename "$genes" .fasta)
        blastn -query $genes -db ${species}/${species_basename}_db \
        -out blast_output/$genes_basename/${species_basename}.xml -outfmt 5
        
    done
    # echo $species
done
