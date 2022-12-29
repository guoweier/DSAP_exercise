# Describe a nonrecursive algorithm for enumerating all permutations of the numbers {1,2...n} using an explicit stack.


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

if __name__ in '__main__':
    iterable = 'ABCD'
    result = list(permutations(iterable))
    for item in result:
        print("".join(item))


# WORKING EXAMPLE
#permutations('ABCD')
#pool = ('A','B','C','D')
#n = 4
#r = 4
#indcies = [0,1,2,3]
#cycles = [4,3,2,1]
#yield:
#('A','B','C','D')

#for i in [3,2,1,0]:
#i = 3:
#cycles[3] = cycles[3]-1 = 1-1=0
#if cycles[3] == 0: (TRUE)
#indices[3:] = indices[4:] + indices[3:4] = [3]
#cycles[3] = 4-3 = 1
#So: indices = [0,1,2,3], cycles = [4,3,2,1]

#i = 2:
#cycles[2] = cycles[2]-1 = 2-1 = 1 (cycles = [4,3,1,1])
#if cycles[2] == 0: (FALSE)
#j = cycles[2] = 1
#indices[2] = indices[-1] = 3, indices[-1] = indices[2] = 2 (indices=[0,1,3,2], cycles=[4,3,1,1])
#yield ('A','B','D','C')
#break (first loop finished, switch last two elements)

#i = 3:
#cycles[3] = cycles[3]-1 = 1-1 = 0
#if cycles[3] == 0 (TRUE)
#indices[3:] = indices[4:] + indices[3:4] = [2]
#cycles[3] = 4-3 = 1 (indices=[0,1,3,2], cycles=[4,3,1,1])

#i = 2:
#cycles[2] = cycles[2]-1 = 1-1 = 0
#if cycles[2] == 0 (TRUE)
#indices[2:] = indices[3:] + indices[2:3] = [2,3]
#cycles[2] = 4-2 = 2 (indices=[0,1,2,3], cycles=[4,3,2,1])

#i = 1:
#cycles[1] = cycles[1]-1 = 3-1 = 2
#if cycles[1] == 0 (FALSE)
#j = cycles[1] = 2
#indices[1] = indices[-2] = 2, indices[-2] = indices[1] = 1 (indices=[0,2,1,3], cycles=[4,2,2,1])
#yield ('A','C','B','D')
#break (second loop finished, start switch last three elements)

#i = 3:
#cycles[3] = cycles[3]-1 = 1-1 = 0
#if cycles[3] == 0 (TRUE)
#indices[3:] = indices[4:] + indices[3:4] = [3]
#cycles[3] = 4-3 = 1 (indices=[0,2,1,3], cycles=[4,2,2,1])

#i = 2:
#cycles[2] = cycles[2]-1 = 2-1 = 1
#if cycles[2] == 0 (FALSE)
#j = cycles[2] = 1
#indices[2] = indices[-1] = 3, indices[-1] = indices[2] = 1 (indices=[0,2,3,1], cycles=[4,2,1,1])
#yield ('A','C','D','B')
#break (third loop finished, continue switch last three elements)

#i = 3:
#cycles[3] = cycles[3]-1 = 1-1 = 0
#if cycles[3] == 0 (TRUE)
#indices[3:] = indices[4:] + indices[3:4] = [1]
#cycles[3] = 4-3 = 1 (indices=[0,2,3,1], cycles=[4,2,1,1])

#i = 2:
#cycles[2] = cycles[2]-1 = 1-1 = 0
#if cycles[2] == 0 (TRUE)
#indices[2:] = indices[3:] + indices[2:3] = [1,3]
#cycles[2] = 4-2 = 2 (indices=[0,2,1,3], cycles=[4,2,2,1])

#i = 1:
#cycles[1] = cycles[1]-1 = 2-1 = 1
#if cycles[1] == 0 (FALSE)
#j = cycles[1] = 1
#indices[1] = indices[-1] = 3, indices[-1] = indices[1] = 2 (indices=[0,3,1,2], cycles=[4,1,2,1])
#yield ('A','D','B','C')
#break (forth loop finished, continue switch last three elements)

#i = 3:
#cycles[3] = cycles[3]-1 = 1-1 = 0
#if cycles[3] == 0 (TRUE)
#indices[3:] = indices[4:] + indices[3:4] = [2]
#cycles[3] = 4-3 = 1 (indices=[0,3,1,2], cycles=[4,1,2,1])

#i = 2:
#cycles[2] = cycles[2]-1 = 2-1 = 1
#if cycles[2] == 0 (FALSE)
#j = cycles[2] = 1
#indices[2] = indices[-1] = 2, indices[-1] = indices[2] = 1 (indices=[0,3,2,1], cycles=[4,1,1,1])
#yield ('A','D','C','B')
#break (fifth loop finished, continue switch last three elements)

#i = 3:
#cycles[3] = cycles[3]-1 = 1-1 = 0
#if cycles[3] == 0 (TRUE)
#indices[3:] = indices[4:] + indices[3:4] = [1]
#cycles[3] = 4-3 = 1 (indices=[0,3,2,1], cycles=[4,1,1,1])

#i = 2:
#cycles[2] = cycles[2]-1 = 1-1 = 0
#if cycles[2] == 0 (TRUE)
#indices[2:] = indices[3:] + indices[2:3] = [1,2]
#cycles[2] = 4-2 = 2 (indices=[0,3,1,2], cycles=[4,1,2,1])

#i = 1:
#cycles[1] = cycles[1]-1 = 1-1 = 0
#if cycles[1] == 0 (TRUE)
#indices[1:] = indices[2:] + indices[1:2] = [1,2,3]
#cycles[1] = 4-1 = 3 (indices=[0,1,2,3], cycles=[4,3,2,1])

#i = 0:
#cycles[0] = cycles[0]-1 = 4-1 = 3
#if cycles[0] == 0 (FALSE)
#j = cycles[0] = 3
#indices[0] = indices[-3] = 1, indices[-3] = indices[0] = 0 (indices=[1,0,2,3], cycles=[3,3,2,1])
#yield ('B','A','C','D')
#break (sixth loop finished, put original second elemnet at first. Treat rest three elements as previous steps)

#.
#.
#.
