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
