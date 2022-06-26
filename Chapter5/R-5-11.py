# Use standard control structures to compute the sum of all numbers in an n x n data set, represented as a list of lists.
import random

def set_matrix(n,seq):
    "Set an n x n matrix."
    matrix = list()
    for i in range(n):
        unit = list()
        for j in range(n):
            a = random.choice(seq)
            unit.append(a)
        matrix.append(unit)
    return matrix

def matrix_sum(n,seq):
    matrix = set_matrix(n,seq)
    result = list()
    for i in range(len(matrix)):
        a = sum(matrix[i])
        result.append(a)
    return sum(result)

if __name__ in "__main__":
    n = 2
    seq = list(i for i in range(1,11))
    print(matrix_sum(n,seq))
