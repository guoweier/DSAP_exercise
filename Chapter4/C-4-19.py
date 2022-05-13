def evenodd(seq,n,even=list(),odd=list()):
    '''Arrange all the even values in front of odd values

    seq:    input sequence.
    n:      the length of seq.
    even:   the even temp list.
    odd:    the odd temp list.
    '''
    if n > 0:
        if seq[n-1]%2 == 0:
            even.append(seq[n-1])
        else:
            odd.append(seq[n-1])
        evenodd(seq,n-1,even,odd)

    result = even+odd
    return result

if __name__ in '__main__':
    seq = [1,3,2,2,24]
    print(evenodd(seq,len(seq)))
