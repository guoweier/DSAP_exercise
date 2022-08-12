# Describe a way to use recursion to add all the number in an n x n data set, represented as a list of lists.

def add_list(seq,n,suml=0):
    if n == 0:
        return suml
    else:
        suml = suml + seq[n-1]
        return add_list(seq,n-1,suml)

def add_matrix(data,n,sum=0):
    if n == 0:
        return sum
    else:
        sum = sum + add_list(data[n-1],x)
        return add_matrix(data,n-1,sum)

if __name__ in "__main__":
    data = [[1,2,3],[1,2,3],[1,2,3]]
    n = 3
    x = 3
    print(add_matrix(data,n))
