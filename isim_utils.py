import math
import numpy as np 
import pickle
import random

def read_fp(filename, fp_type):
    with open(filename, 'rb') as f:
        data = pickle.load(f)

    return np.array(data[fp_type])

def quick_jt(fp_1, fp_2):
    s1 = np.sum(fp_1)
    a = np.dot(fp_1, fp_2)
    return a / (s1 + np.sum(fp_2) - a)

def jt_matrix(fingerprints):
    matrix = []
    for fp_1 in fingerprints:
        matrix.append([])
        s1 = np.sum(fp_1)
        for fp_2 in fingerprints:
            a = np.dot(fp_1, fp_2)
            matrix[-1].append(a / (s1 + np.sum(fp_2) - a))
    matrix = np.array(matrix)
    return matrix

def sali_matrix(jt_matrix, prop):
    matrix = []
    for i in range(jt_matrix.shape[0]):
      matrix.append([])
      for j in range(jt_matrix.shape[0]):
        if i != j:
            sali = np.abs(prop[i] - prop[j])/(1-jt_matrix[i,j])
        elif i == j:
            sali = np.inf
        matrix[-1].append(sali)
    matrix = np.array(matrix)
    return matrix

def quick_matrix_search(matrix, search_criteria = 'max'):
    # Find the index of the max value in the matrix using np.argmax and np.unravel_index
    pairs = []
    if search_criteria == 'max':
        np.fill_diagonal(matrix, -np.inf)
        while len(pairs) < math.floor(len(matrix)/2):    
            max_index = np.argmax(matrix)
            indexes = np.unravel_index(max_index, matrix.shape)
            matrix[indexes[0],:] = -np.inf
            matrix[indexes[1],:] = -np.inf
            matrix[:,indexes[0]] = -np.inf
            matrix[:,indexes[1]] = -np.inf
            pairs.append(indexes)

    elif search_criteria == 'min':
        np.fill_diagonal(matrix, np.inf)
        while len(pairs) < math.floor(len(matrix)/2):
            min_index = np.argmin(matrix)
            indexes = np.unravel_index(min_index, matrix.shape)
            matrix[indexes[0],:] = np.inf
            matrix[indexes[1],:] = np.inf
            matrix[:,indexes[0]] = np.inf
            matrix[:,indexes[1]] = np.inf
            pairs.append(indexes)

    return pairs