from isim_utils import *
import argparse

# Script to generate the sali matrix
parser = argparse.ArgumentParser(description='Generate the sali matrix')
parser.add_argument('-f','--file', metavar='file', type=str)
parser.add_argument('-jt','--jt_matrix', metavar='jt_matrix', type=str)
parser.add_argument('-fp','--fp_type', metavar='fp_type', type=str)

args = parser.parse_args()

# Load the data
props = read_fp(args.file, "prop")
file_name = args.file.split('/')[-1].split('.')[0]

# Load the JT matrix
jt_matrix = np.load(args.jt_matrix)

# Generate the sali matrix
sali_matrix = sali_matrix(jt_matrix, props)

# Save the sali matrix
np.save(file_name + '_' + args.fp_type + '_salimatrix.npy', sali_matrix)
