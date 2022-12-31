# Show how to use a stack S and a queue Q to generate all possible subset of an n-element set T nonrecursively.

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def getsubset(T):
    n = len(T)
    for i in range(1,n+1):
        yield combinations(T,i)

if __name__ in "__main__":
    iter = {1,2,3,4,5}
    result = list(getsubset(iter))
    for item in result:
        print(list(item))


# combinations('ABCD',r=3)
# pool = ('A','B','C','D')
# n = 4
# indices = [0,1,2]
# yield ('A','B','C','D')
# while True:
# for i in [2,1,0]:
# if indices[2] (=2) != 2+4-3 = 3 (True)
# break
# i = 2
# indices[2] = indices[2]+1 = 2+1 = 3 (indices = [0,1,3])
# for j in range(3,3):
# NA
# yield ('A','B','D')

# for i in [2,1,0]:
# if indices[2] (=3) != 2+4-3 = 3 (False)
# if indices[1] (=1) != 1+4-3 = 2 (True)
# break
# i = 1
# indices[1] = indices[1]+1 = 1+1 = 2 (indices = [0,2,3])
# for j in range(2,3):
# indices[2] = indices[1]+1 = 2+1 = 3 (indices = [0,2,3])
# yeild ('A','C','D')

# for i in [2,1,0]:
# if indices[2] (=3) != 2+4-3 = 3 (False)
# if indices[1] (=2) != 1+4-3 = 2 (False)
# if indices[0] (=0) != 0+4-3 = 1 (True)
# break
# i = 0
# indices[0] = indices[0]+1 = 1 (indices = [1,2,3])
# for j in range(1,3):
# indices[1] = indices[0]+1 = 1+1 = 2
# indices[2] = indices[1]+1 = 2+1 = 3 (indices = [1,2,3])
# yield ('B','C','D')

# for i in [2,1,0]:
# if indices[2] (=3) != 2+4-3 = 3 (False)
# if indices[1] (=2) != 1+4-3 = 2 (False)
# if indices[0] (=1) != 0+4-3 = 1 (False)
# return
 
