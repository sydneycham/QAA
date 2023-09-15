#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import gzip 

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Input filename", required=True)
    parser.add_argument("-o", "--outfile", help="Input output filename", required=False)
    parser.add_argument("-r", "--readlength", help="Input read length", required=False)
    return parser.parse_args()

args = get_args()

f=args.filename
o=args.outfile
r=args.readlength

def init_list(lst: list, value: float=0.0) -> list:
    '''This function takes an empty list and will populate it with
    the value passed in "value". If no value is passed, initializes list
    with 101 values of 0.0.'''
    #init_list = lst[value]*101
    for x in range(int(r)):
        lst.append(value)
    return lst
my_list: list = []
my_list = init_list(my_list)

def convert_phred(letter: str): #-> int
    '''Converts a single character into a phred score'''
    return ord(letter)-33
    
def populate_list(f: str) -> tuple[list, int]:
    """quality scores"""
    checkitout=[]
    checkitout=init_list(checkitout)
    with gzip.open (f, "rt") as testfile:
        i=0
        sum =0
        for line in testfile:
            i+=1
            line =line.strip('\n')
            if i%4==0:
                for index,letter in enumerate(line):
                    phredtest= convert_phred(letter)
                    checkitout[index]+=phredtest
        return checkitout, i 

my_list, num_lines = populate_list(f)

for index,sumscore in enumerate(my_list):
    mean = sumscore/(num_lines/4)
    my_list[index]=mean
    print(f'{index}\t{mean}')

plt.plot(range(len(my_list)), my_list)
plt.xlabel('Nucleotide')
plt.ylabel('Mean Quality Score')
plt.title('Mean Quality score for each Nucleotide location')

plt.savefig(f'{o}.png')
#plt.show()