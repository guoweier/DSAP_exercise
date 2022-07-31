# A useful operation in database is the natural join. If we view a database as a list of ordered pairs of objects, then the natural join of database A and B is the list of all ordered triples (x,y,z) such that the pair (x,y) is in A and the pair (y,z) is in B. Describe an analyze an efficient algorithm for computing hte natural join of a list A of n pairs and a list B of m pairs.

import numpy as np

def balance_list(A,B):
    "Balance the element pairs in two lists."
    n = len(A)
    m = len(B)
    if n < m:
        for i in range(n,m):
            A.append(B[i])
    elif n > m:
        for i in range(m,n):
            B.append(A[i])
    return A,B

def natural_join(A,B):
    A,B = balance_list(A,B)
    result = []
    for i in range(len(A)):
        c = A[i]+B[i]
        cjoin = np.unique(c)
        result.append(cjoin)
    return result

if __name__ in "__main__":
    A = [[1,2],[3,4],[3,45],[12,2]]
    B = [[1,7],[5,7]]
    print(natural_join(A,B))
