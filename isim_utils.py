import numpy as np 
import pickle
import random

def read_fp(filename, fp_type):
    with open(filename, 'rb') as f:
        data = pickle.load(f)

    return np.array(data[fp_type])

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

def matrix_search(matrix, search_criteria = 'max'):
    if search_criteria == 'max':
        target = -np.inf
        def check(value, target):
            return value > target
    if search_criteria == 'min':
        target = np.inf
        def check(value, target):
            return value < target
    
    remaining = np.array(range(matrix.shape[0]))
    pairs = []

    while len(remaining) > 1:
        for i in remaining:
            for j in remaining:
                if i != j:
                    if check(matrix[i,j], target):
                        target = matrix[i,j]
                        chosen_pair = [i,j]
                    
        print('remaining: ', remaining)
        print('chosen pair: ', chosen_pair)
        mask = np.isin(remaining, chosen_pair)
        remaining = remaining[~mask]
        print('remaining: ', remaining)

        if search_criteria == 'max': target = -np.inf
        if search_criteria == 'min': target = np.inf
        pairs.append(chosen_pair)

    return pairs


fps = np.random.randint(2, size=(5, 2048), dtype='int64')
jt_m = jt_matrix(fps)
prop = np.random.rand(5)
sali_m = sali_matrix(jt_m, prop)

print(sali_m)
print(matrix_search(sali_m, 'max'))
print(matrix_search(sali_m, 'min'))
