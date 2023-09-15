#!/bin/bash

#SBATCH --time=4:00:00
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=interactive               #REQUIRED: which partition to use
#SBATCH --mail-user=syha@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB

conda activate BGMP_QAA

# /usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
# --outFilterMultimapNmax 3 \
# --outSAMunmapped Within KeepPairs \
# --alignIntronMax 1000000 --alignMatesGapMax 1000000 \
# --readFilesCommand zcat \
# --readFilesIn /projects/bgmp/syha/bioinfo/Bi623/QAA/19_3F_fox_S14_L008_R1_001.trim.fastq.gz /projects/bgmp/syha/bioinfo/Bi623/QAA/19_3F_fox_S14_L008_R2_001.trim.fastq.gz \
# --genomeDir /projects/bgmp/syha/bioinfo/Bi623/QAA/database \
# --outFileNamePrefix Aligned_19_3F_

/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
--outFilterMultimapNmax 3 \
--outSAMunmapped Within KeepPairs \
--alignIntronMax 1000000 --alignMatesGapMax 1000000 \
--readFilesCommand zcat \
--readFilesIn /projects/bgmp/syha/bioinfo/Bi623/QAA/7_2E_fox_S6_L008_R1_001.trim.fastq.gz /projects/bgmp/syha/bioinfo/Bi623/QAA/7_2E_fox_S6_L008_R2_001.trim.fastq.gz \
--genomeDir /projects/bgmp/syha/bioinfo/Bi623/QAA/database \
--outFileNamePrefix Aligned_7_2E_

