#!/bin/bash
fasta_dir="/root/pipeline/splited_from_fasta"

# 切换到该目录
cd "$fasta_dir" || exit

# 遍历目录下的所有 .fasta 文件
for fasta_file in *.fasta; do
  # 提取文件名（去掉 .fasta 后缀）
  dir_name="/root/pipeline/blast_output/${fasta_file%.fasta}"
  
  # 创建与文件名同名的目录
  mkdir -p "$dir_name"
done