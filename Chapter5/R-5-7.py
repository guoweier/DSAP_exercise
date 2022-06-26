# Let A be an array of size n >= 2 containing integers from 1 to n-1, inclusive, with exactly one repeated. Describe a fast algorithm for finding the integer in A that is repeated.
import random

def select_rep(A):
    "Select the repeated element in array A."
    A.sort()
    for i in range(1,len(A)):
        if A[i] == A[i-1]:
            return A[i]

if __name__ in '__main__':
    A = [1,24,3,234,2,13,7,7,14,32]
    print(select_rep(A))
