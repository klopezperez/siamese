from isim_utils import *
import argparse
import pandas as pd

# Script to search for pairs in a given matrix
parser = argparse.ArgumentParser(description='Search for pairs in a given matrix')
parser.add_argument('-m','--matrix', metavar='matrix', type=str)
parser.add_argument('-sc','--search_criteria', metavar='search_criteria', type=str)

args = parser.parse_args()

# Load the matrix
matrix = np.load(args.matrix)

# Search for pairs
pairs = matrix_search(matrix, args.search_criteria)

# Save the pairs in a csv file
df = pd.DataFrame(pairs)
df.to_csv(args.matrix.split('/')[-1].split('.')[0] + '_' + args.search_criteria + '_pairs.csv', index=False, header=False)
