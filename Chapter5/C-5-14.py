# The shuffle method, supported by the random module, takes a Python list and rearranges it so that every possible ordering is equally likely. Implement your own version of such a function. You may rely on the randrange(n) function of the random module, which returns a random number between 0 and n-1 inclusive.

import random

def shuffle(A):
    B = list()
    for k in range(len(A)):
        i = random.randrange(0,(len(A)),1)
        B.append(A[i])
        A.pop(i)
    return B

if __name__ in "__main__":
    A = list(i for i in range(1,11))
    print(shuffle(A))
