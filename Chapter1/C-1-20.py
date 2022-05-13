# only use randint() to write a python function shuffle().

import random

def shuffles(data):
    a = data[0]-1
    b = data[len(data)-1]+1
    out = []
    while len(data) != 0:
        x = random.randint(a,b)
        if x in data:
            out.append(x)
            data.remove(x)
        else:
            continue
    return out

data = [1,2,3,5]
print(shuffles(data))