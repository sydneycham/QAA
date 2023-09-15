#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=roel@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB

/usr/bin/time -v ./phred_encode.py -f /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R1_001.fastq.gz -o 7_2E_R1 -r 101