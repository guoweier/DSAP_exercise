def lessgofirst(S,k,n,less=list(),more=list()):
    '''Return a sequence with less than k values come before larger than k values.

    S:      input sequence, containing integers.
    k:      input value.
    n:      the length of sequence S.
    less:   the temp list for storing smaller values.
    more:   the temp list for storing larger values.
    '''
    if n > 0:
        if S[n-1] <= k:
            less.append(S[n-1])
        else:
            more.append(S[n-1])
        lessgofirst(S,k,n-1,less,more)

    result = less+more
    return result


if __name__ in '__main__':
    S = [23,4,13,6,32,36,4,1,10,5]
    k = 8
    print(lessgofirst(S,k,len(S)))
