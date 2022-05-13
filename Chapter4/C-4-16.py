def convertlist(string):
    '''convert string to a list object.'''
    Svector = list(string)
    return Svector

def reverse(Svector,start,stop):
    '''Return the reverse of the input string.
    string:     the input string.
    start:      the forward index.
    stop:       the backward index.
    '''
    if start < stop-1:
        Svector[start],Svector[stop-1] = Svector[stop-1],Svector[start]
        reverse(Svector,start+1,stop-1)


def reversestring(string,start,stop):
    '''final working function'''
    Sv = convertlist(string)
    reverse(Sv,start,stop)
    reString = ''
    for k in Sv:
        reString += k
    return reString


if __name__ in '__main__':
    string = 'pots&pans'
    print(reversestring(string,0,len(string)))
