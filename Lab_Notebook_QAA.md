Lab Notebook QAA
-history | grep srun
-module spider fastqc
-module load fastqc/0.11.5

fastqc --outdir=/projects/bgmp/syha/bioinfo/Bi623/QAA /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R2_001.fastq.gz 
fastqc --outdir=/projects/bgmp/syha/bioinfo/Bi623/QAA /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R2_001.fastq.gz

#bash script so we can time the program

9/7/23
-change phred_encode.py to include arg parse readlength input
---19_3F_R1 = Elapsed (wall clock) time (h:mm:ss or m:ss): 3:40.41
Exit Status 0
---19_3F_R2 = Elapsed (wall clock) time (h:mm:ss or m:ss): 3:46.89
Exit Status 0
---7_2E_R1 = Elapsed (wall clock) time (h:mm:ss or m:ss): 1:16.13
Exit Status 0
---7_2E_R2 = Elapsed (wall clock) time (h:mm:ss or m:ss): 1:12.98
Exit Status 0

Also, produce plots of the per-base N content, and comment on whether or not they are consistent with the quality score plots.
-On all of the plots there appears to be no N's in either quality score plot ot N plot so yes they are consistent. 

Describe how the FastQC quality score distribution plots compare to your own
FastQC was faster than the script we wrote.

Comment on the overall data quality of your two libraries. Go beyond per-base qscore distributions. Make and justify a recommendation on whether or these data are of high enough quality to use for further analysis.
-They're all above cutoff and the R1's look pretty good so they would be prepared for further analysis. 

-conda installed trimmomatic and cutadapt

9/8/23

checking sequences for adapters
-zcat 7_2E_fox_S6_L008_R1_001.fastq.gz | grep "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA" | wc -l

-running cutadapt
-cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o 7_2E_R1_out.fastq -p 7_2E_R2_out.fastq /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R2_001.fastq.gz > cutadapt_7_2E_output.txt

-cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o 19_3F_R1_out.fastq -p 19_3F_R2_out.fastq /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R2_001.fastq.gz > cutadapt_19_3F_output.txt

- What proportion of reads (both R1 and R2) were trimmed?
----  7_2E
----  Read 1 with adapter:                 173,473 (3.3%)
----  Read 2 with adapter:                 212,512 (4.0%)
----  19_3F
----  Read 1 with adapter:                 546,623 (3.3%)
----  Read 2 with adapter:                 676,564 (4.1%)


-trimmomatic PE -phred33 /projects/bgmp/syha/bioinfo/Bi623/QAA/7_2E_R1_out.fastq /projects/bgmp/syha/bioinfo/Bi623/QAA/cutadapt_7_2E_output.txt \
                /projects/bgmp/syha/bioinfo/Bi623/QAA/7_2E_fox_S6_L008_R1_001.trim.fastq.gz /projects/bgmp/syha/bioinfo/Bi623/QAA/7_2E_fox_S6_L008_R1_001un.trim.fastq.gz \
                /projects/bgmp/syha/bioinfo/Bi623/QAA/7_2E_fox_S6_L008_R2_001.trim.fastq.gz /projects/bgmp/syha/bioinfo/Bi623/QAA/7_2E_fox_S6_L008_R2_001un.trim.fastq.gz \
                SLIDINGWINDOW:5:15 MINLEN:35 LEADING:3 TRAILING:3

Input Read Pairs: 5278425 Both Surviving: 4882388 (92.50%) Forward Only Surviving: 388675 (7.36%) Reverse Only Surviving: 3814 (0.07%) Dropped: 3548 (0.07%)
TrimmomaticPE: Completed successfully

-trimmomatic PE -phred33 /projects/bgmp/syha/bioinfo/Bi623/QAA/19_3F_R1_out.fastq /projects/bgmp/syha/bioinfo/Bi623/QAA/cutadapt_19_3F_output.txt \
                /projects/bgmp/syha/bioinfo/Bi623/QAA/19_3F_fox_S14_L008_R1_001.trim.fastq.gz /projects/bgmp/syha/bioinfo/Bi623/QAA/19_3F_fox_S14_L008_R1_001un.trim.fastq.gz \
                /projects/bgmp/syha/bioinfo/Bi623/QAA/19_3F_fox_S14_L008_R2_001.trim.fastq.gz /projects/bgmp/syha/bioinfo/Bi623/QAA/19_3F_fox_S14_L008_R2_001un.trim.fastq.gz \
                SLIDINGWINDOW:5:15 MINLEN:35 LEADING:3 TRAILING:3

Input Read Pairs: 16348255 Both Surviving: 15898789 (97.25%) Forward Only Surviving: 428905 (2.62%) Reverse Only Surviving: 14879 (0.09%) Dropped: 5682 (0.03%)
TrimmomaticPE: Completed successfully

zcat 7_2E_fox_S6_L008_R1_001.trim.fastq.gz | grep -E "[AGTC]+" | sed -n '2~4p' | awk '{print length($0)}' | sort -n | uniq -c > trimmed_dist_7_2E_R1.txt

zcat 7_2E_fox_S6_L008_R2_001.trim.fastq.gz | grep -E "[AGTC]+" | sed -n '2~4p' | awk '{print length($0)}' | sort -n | uniq -c > trimmed_dist_7_2E_R2.txt

zcat 19_3F_fox_S14_L008_R1_001.trim.fastq.gz | grep -E "[AGTC]+" | sed -n '2~4p' | awk '{print length($0)}' | sort -n | uniq -c > trimmed_dist_19_3F_R1.txt

zcat 19_3F_fox_S14_L008_R2_001.trim.fastq.gz | grep -E "[AGTC]+" | sed -n '2~4p' | awk '{print length($0)}' | sort -n | uniq -c > trimmed_dist_19_3F_R2.txtE


9-11-23
-in matplotlib: alpha=0.5 gives us opacity when plotting two sets of data   

-conda list --envs (lists environments)
-conda install -c bioconda star

-unzipping downloaded fasta and gtf files for our script from PS8 that runs star

-saving figures to computer for markdown report
scp syha@login.talapas.uoregon.edu:/projects/bgmp/syha/bioinfo/Bi623/QAA/trimmed_19_3F_lengthdist.png .
scp syha@login.talapas.uoregon.edu:/projects/bgmp/syha/bioinfo/Bi623/QAA/trimmed_7_2E_lengthdist.png .

scp syha@login.talapas.uoregon.edu:/projects/bgmp/syha/bioinfo/Bi623/QAA/19_3F_R1.png .
scp syha@login.talapas.uoregon.edu:/projects/bgmp/syha/bioinfo/Bi623/QAA/19_3F_R2.png .
scp syha@login.talapas.uoregon.edu:/projects/bgmp/syha/bioinfo/Bi623/QAA/7_2E_R1.png .
scp syha@login.talapas.uoregon.edu:/projects/bgmp/syha/bioinfo/Bi623/QAA/7_2E_R2.png .

9-12-23
-ran slurm script for STAR
STAR --version (to check version of STAR)
ls -lahrt (to check the last thing that was output or edited)
#SBATCH --time=4:00:00 (needed when running in interactive because it sets default time)
--genomeDir (refers to the genome to align to [not the output directory])

Aligned_19_3F_Aligned.out.sam
Mapped reads are: 30,511,270
Unmapped reads are: 1,286,308
Total = 31,797,578
Percent Mapped = 95.95%

Aligned_7_2E_Aligned.out.sam
Mapped reads are: 9,424,188
Unmapped reads are: 340,588
Total = 9,764,776
Percent Mapped = 96.51%

-{r 19_3F_R1, fig.cap="Quality Score plot of $19_3F$ read 1.", echo=FALSE, out.width="250px"} 
    -this header cannot match another code block

9-14-23
- grep -v "^__" Aligned_reverse_7_2E_out.tsv | awk '$2>0 {sum+=$2} END {print sum}'
grep -v "^__" Aligned_yes_7_2E_out.tsv | awk '$2>0 {sum+=$2} END {print sum}'
grep -v "^__" Aligned_reverse_19_3F_out.tsv | awk '$2>0 {sum+=$2} END {print sum}'
grep -v "^__" Aligned_yes_19_3F_out.tsv | awk '$2>0 {sum+=$2} END {print sum}'

used on HTSeq outputs to determine strandedness

reverse 7_2E: 4026820
forward 7_2E: 179664
percent reverse: 95.72%

reverse 19_3F: 12935458
forward 19_3F: 545722
percent reverse: 95.95%

Both pairs have more reverse reads than forward reads which is a sign of strandedness. 