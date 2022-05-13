def findfirst(S,k,start,stop):
    '''Return False if not find; Return first num if find.

    S:      the ascending sequence.
    k:      the target value for first number.
    start:  the first index.
    stop:   the last index.
    '''
    if k < S[start] or start >= stop:
        return False
    else:
        mid = (start+stop)//2
        if S[mid] <= k:
            k2 = k-S[mid]
            return [k2,mid]
        else:
            return findfirst(S,k,start,mid-1)

def findsecond(S,k,start,stop):
    '''Return False if not find; Return two nums if find.'''
    if k < S[start] or start >= stop:
        return False
    else:
        mid = (start+stop)//2
        if S[mid] == k:
            return S[mid]
        elif k < S[mid]:
            return findsecond(S,k,start,mid-1)
        else:
            return findsecond(S,k,mid+1,stop)



def findsum(S,k,start,stop):
    '''final working function.'''
    firstnum = findfirst(S,k,start,stop)
    if firstnum == False:
        print("There is no such pair exist.")
    else:
        secondnum = findsecond(S,firstnum[0],firstnum[1],stop)
        if secondnum == False:
            print("There is no such pair exist.")
        else:
            print("The two numbers are "+str(S[firstnum[1]])+' and '+str(secondnum)+'.')

if __name__ in '__main__':
    S=[1,2,3,4,5,6]
    k=10
    findsum(S,k,0,len(S))
