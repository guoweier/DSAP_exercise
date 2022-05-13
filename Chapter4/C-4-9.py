def findmax(seq, n):
    """find the maximun value.
    seq:    the sequence of values.
    n:      the length of sequence.
    """
    if n == 0:
        return 0
    elif n == 1:
        return seq[0]
    else:
        if seq[n-1] > findmax(seq,n-1):
            return seq[n-1]
        else:
            return findmax(seq,n-1)

def findmin(seq, n):
    '''find the minimun value.
    seq:    the sequence of values.
    n:      the length of sequence.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return seq[0]
    else:
        if seq[n-1] < findmin(seq,n-1):
            return seq[n-1]
        else:
            return findmin(seq,n-1)

def maxmin(seq, n):
    '''Return max and min values in a squence.
    '''
    return [findmin(seq,n), findmax(seq,n)]


if __name__ in '__main__':
    seq = [1,3,3,26,4]
    n = 5
    print(maxmin(seq,n))
