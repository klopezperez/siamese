from isim_comp import *
from isim_utils import *
import argparse
import pickle

# Script to generate pair complementary similarity matrix
parser = argparse.ArgumentParser(description='Generate pair complementary similarity matrix')
parser.add_argument('-f','--file', metavar='file', type=str)
parser.add_argument('-fp','--fp_type', metavar='fp_type', type=str)

args = parser.parse_args()

# Load the data
fingerprints = read_fp(args.file, args.fp_type)

# Do the column wise sum
c_sum = np.sum(fingerprints, axis=0)

# Get number of compounds after pair removal
n_comp = len(fingerprints) - 2

# Generate the pair complementary similarity matrix
matrix = []
for fp_1 in fingerprints:
    matrix.append([])
    for fp_2 in fingerprints:
        c = c_sum - fp_1 - fp_2
        pc = gen_sim_dict(c, n_comp)['JT']
        matrix[-1].append(pc)
matrix = np.array(matrix)

# Save the pair complementary similarity matrix
file_name = args.file.split('/')[-1].split('.')[0]
np.save(file_name + '_' + args.fp_type + '_pairccomp_matrix.npy', matrix)

