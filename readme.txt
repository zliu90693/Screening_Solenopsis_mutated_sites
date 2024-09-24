大致流程如下：
使用split_gb.py，从红火蚁全线粒体.gb文件（/root/pipeline/old_fasta_gb/invicta.gb）中将各基因提取出来，
放入/root/pipeline/splited_from_gb/invicta_genes_extracted.fasta。随后，使用split_fasta.py，将
invicta_genes_extracted.fasta中各基因分离出来，各保存在一个fasta文件中（splited_from_fasta目录下）。
再运行generate_blast_db.sh，根据待比对的火蚁属物种fasta序列创建数据库，数据库位于database目录下。
运行generate_list.sh，创建blast_output及其下属目录，用于存储blastn的输出文件（xml格式）。
运行do_blast.sh，进行blastn比对，将xml文件输出到blast_output及其下属目录中。
运行extract_target_seq.py，创建combined目录，将xml文件中匹配到的目的基因输出到combined目录下的各fasta文件中，
最终的结果就是一个fasta文件（一种基因），下有火蚁属全部物种的（经过匹配的）同种基因。
随后将combined目录移动到oligotyping环境下，使用entropy-analysis函数计算shannon熵，如果各序列数目不相等，
则运行muscle -in ...fasta -out ...fasta进行对齐，随后计算shannon熵。shannon熵结果保存在...ENTROPY文件中。

在本地terminal运行move_file_bt_docker.sh，示例：
bash move_file_bt_docker.sh 078be2a88d55 /root/do_entropy/combined/NADH_dehydrogenase_subunit_6_aligned.fasta-ENTROPY 72a81f04e026 /root/pipeline/entropy_file/
将oligotyping环境下的ENTROPY文件转移到arch容器下的entropy_file目录下，进行画图。
首先运行convert_csv.sh，指定要转化为csv的ENTROPY文件，将其转化为csv.随后运行convert_csv_pro_graph.R，
在radian中依次执行：
r$> tibble=convert_csv("目标csv")
r$> generate_graph(tibble)
即可做出shannon熵与位点间的折线图。