# short python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. 
# Do not use the built-in functions min or max in implementing your solution.

seq = [3,65,34,6.7,3,2,1,-1,102,-12]

def minmax(data):
    minv = data[0]
    maxv = data[0]
    for value in data:
        if value < minv:
            minv = value
        if value > maxv:
            maxv = value
    a = (minv, maxv)
    return a

print(minmax(seq))        
