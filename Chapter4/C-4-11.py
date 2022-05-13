def uniqueness(S,n,k):
    '''return True if there is no duplicate elements in sequence S.
    S:  the checking sequence;
    n:  the first value waiting for comparison;
    k:  the second (nested) value for comparison (k in range(n-1));
    '''
    if n == 1:
        return True
    else:
        if k == 0:
            return uniqueness(S,n-1,n-2)
        else:
            if S[n-1] == S[k-1]:
                return False
            else:
                return uniqueness(S,n,k-1)

if __name__ in '__main__':
    S = [1,2,3,4,5]
    n = 5
    k = 4
    print(uniqueness(S,n,k))
