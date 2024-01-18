from isim_utils import *
import argparse

# Script to generate the JT matrix

# Arguments
parser = argparse.ArgumentParser(description='Generate the JT matrix')
parser.add_argument('-f','file', metavar='file', type=str)
parser.add_argument('-fp','fp_type', metavar='fp_type', type=str)


args = parser.parse_args()

# Load the data
fingerprints = read_fp(args.file, args.fp_type)
file_name = args.file.split('/')[-1].split('.')[0]

# Generate the JT matrix
jt_matrix = jt_matrix(fingerprints)

# Save the JT matrix
np.save(file_name + '_' + args.fp_type + '_jtmatrix.npy', jt_matrix)
