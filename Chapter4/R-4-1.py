def maximum(seq, n):
    '''find the maximum elemoent in a sequence S of n elements.'''
    if n == 0:
        return 0
    elif n == 1:
        return seq[0]
    else:
        if seq[n-1] > maximum(seq,n-1):
            return seq[n-1]
        else:
            return maximum(seq,n-1)


if __name__ in '__main__':
    seq = [1,2,53,3,6,42,4]
    n = 6
    print(maximum(seq,n))
