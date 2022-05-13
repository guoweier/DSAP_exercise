import random

seq = [k for k in range(100)]

def choice(data):
    a = random.randrange(data[0],data[len(data)-1])
    return a

print(choice(seq))