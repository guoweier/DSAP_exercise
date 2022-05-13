# p-norm of a vector

import math


def norms(v,p=2):
    sumv = sum(i**p for i in v)
    pnorm_v = sumv**(1./p)
    return pnorm_v

v = [1,2,3,4]

print(norms(v,3))