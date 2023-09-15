#!/usr/bin/env python

import argparse
import gzip
import matplotlib.pyplot as plt


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Input filename", required=True)
    parser.add_argument("-f2", "--filename2", help="Input filename2", required=True)
    parser.add_argument("-o", "--outfile", help="Input output filename", required=False)
    return parser.parse_args()

args = get_args()

f=args.filename
f2=args.filename2
o=args.outfile

r1_dict = {}
r2_dict = {}


with open (f, "r") as file:
    i=0
    for line in file:
        i+=1
        line=line.strip("\n")
        line=line.split()
        r1_dict[int(line[1])]=int(line[0])

            
with open (f2, "r") as file2:
    k=0
    for line in file2:
        k+=1
        line=line.strip("\n")
        line=line.split()
        r2_dict[int(line[1])]=int(line[0])


plt.title("Trimmed Length Distribution of Read 1 and Read 2")
plt.xlabel("Length of Read")
plt.ylabel("Log Transformed Frequency")
plt.bar(x=list(r1_dict.keys()),height=list(r1_dict.values()),alpha=0.5,label="Forward Reads")
plt.bar(x=list(r2_dict.keys()),height=list(r2_dict.values()),alpha=0.5,label="Reverse Reads")
plt.yscale("log")
plt.legend(loc="upper left")
plt.savefig(fname=o) 