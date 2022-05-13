def scale(data, factor):
    a = []
    for val in data:
        val *= factor
        a.append(val)
    return a

data = [1,2,3,4]
factor = 2

print(scale(data,factor))