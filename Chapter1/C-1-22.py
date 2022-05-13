#python program
#takes arrays a and b (length n) storing int values.
#rturn the dot product of a and b in array c.

def product(a,b):
    c = [a[i]*b[i] for i in range(len(a))]
    return c

a=[1,2,3,4]
b=[1,2,3,4]

print(product(a,b))
        