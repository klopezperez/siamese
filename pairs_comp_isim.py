from isim_comp import *
from isim_utils import *
import argparse
import pickle
import math 
import pandas as pd

# Script to generate generate pairs based on comp isim
parser = argparse.ArgumentParser(description='Generate pairs based on comp isim')
parser.add_argument('-f','--file', metavar='file', type=str)
parser.add_argument('-fp','--fp_type', metavar='fp_type', type=str)
parser.add_argument('-m', '--method', metavar='method', type=str)

args = parser.parse_args()

# Load the data
fingerprints = read_fp(args.file, args.fp_type)
file_name = args.file.split('/')[-1].split('.')[0]

# Order the fingerprints by their comp isim
comp_sim = calculate_comp_sim(fingerprints, n_ary= 'JT', c_total= np.sum(fingerprints, axis=0))
indexes = list(range(len(comp_sim)))
indexes.sort(key=lambda x: comp_sim[x])

# Get a the pairs based on the pairing method
pairs = []
if args.method == 'extremes': 
    pairs = [[indexes[i], indexes[-(i+1)]] for i in range(math.floor(len(indexes)/2))]
elif args.method == 'consecutives':
    if len(indexes) % 2 == 0:
        pairs = [[indexes[i], indexes[i+1]] for i in range(0, len(indexes), 2)]
    else:
        pairs = [[indexes[i], indexes[i+1]] for i in range(0, len(indexes)-1, 2)]

# Save the pairs in a csv file
df = pd.DataFrame(pairs)
df.to_csv(file_name + '_' + args.fp_type + '_' + args.method + '_pairs.csv', index=False, header=False)
