#!/bin/bash

input_file=$1
output_file=${input_file%.fasta-ENTROPY}.csv

echo "position,entropy" >> $output_file
sed 's/[ \t]/,/g' $input_file >> $output_file
rm $input_file