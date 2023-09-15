#!/usr/bin/env python

# file = "Aligned_7_2E_Aligned.out.sam"

# with open (file, "r") as sam:
#     mapped_reads = 0 #initalizing mapped reads sum
#     unmapped_reads = 0 #initalizing unmapped reads sum
#     bflaglist = [] #empty list for bitflags
#     for line in sam: #looping through lines
#         if line.startswith('@'): #passing through top lines with '@'
#             pass
#         else:
#             bflaglist = line.split('\t')[1] #converting to strings?
#             flag = int(bflaglist[1]) #grabbing 2nd column (our bitflags)
#             if (flag & 256) == 256: #check if aligned multiple times
#                 pass
#             elif((flag & 4) != 4): #checking if bitflag signifies mapped or not
#                 mapped_reads+=1
#             else:
#                 unmapped_reads+=1
#     print (mapped_reads)
#     print (unmapped_reads)
        

import argparse 

def get_args():
    parser= argparse.ArgumentParser()
    parser.add_argument("-f1", "--filename1", help="Input filename", required=True)

    parser.add_argument("-o", "--output", help="Output filename", required=False)
    return parser.parse_args()
args = get_args()
f1=args.filename1
o=args.output



with open (f1, "r") as samfile:
    i=0
    mappedreads = 0
    unmappedreads = 0
    for line in samfile:
        if line.startswith("@"): 
            pass
        else: 
            bit_flag=int(line.split('\t')[1])
            #print(bit_flag)
            if (bit_flag & 256) == 256:
                pass
            elif((bit_flag & 4) != 4):  
                mappedreads +=1
            else:
                # print("unmapped :( ")
                unmappedreads+=1
       

print("Mapped reads are:", mappedreads)
print("Unmapped reads are:", unmappedreads)