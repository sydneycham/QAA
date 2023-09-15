#!/bin/bash

#SBATCH --time=4:00:00
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=interactive               #REQUIRED: which partition to use
#SBATCH --mail-user=syha@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB

conda activate BGMP_QAA

/usr/bin/time htseq-count --stranded=yes Aligned_7_2E_Aligned.out.sam Mus_musculus.GRCm39.110.gtf > Aligned_yes_7_2E_out.tsv

/usr/bin/time htseq-count --stranded=yes Aligned_19_3F_Aligned.out.sam Mus_musculus.GRCm39.110.gtf > Aligned_yes_19_3F_out.tsv


/usr/bin/time htseq-count --stranded=reverse Aligned_7_2E_Aligned.out.sam Mus_musculus.GRCm39.110.gtf > Aligned_reverse_7_2E_out.tsv

/usr/bin/time htseq-count --stranded=reverse Aligned_19_3F_Aligned.out.sam Mus_musculus.GRCm39.110.gtf > Aligned_reverse_19_3F_out.tsv