# Suppose Alice has picked three distinct integers and placed them into a stack S in random order. Write a short, straight-line piece of pseudo-code (with no loops or recursion) that uses only one comparison and only one variable x, yet that results in variable x storing the largest of Alice's three integers with probability 2/3. Argue why your method is correct.

import random

def max_int(S):
    x = S[0]
    S.pop(0)
    if x < S[0]:
        x = S[0]
    return x

if __name__ in "__main__":
    T = 0
    for j in range(1000):
        S = []
        for i in range(3):
            s = random.randint(1,200)
            S.append(s)
        Rmax = max(S)
        if Rmax == max_int(S):
            T += 1
    print(T/1000)
