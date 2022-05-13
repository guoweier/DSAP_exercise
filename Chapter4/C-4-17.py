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
        if Svector[start] == Svector[stop-1]:
            reverse(Svector,start+1,stop-1)
        else:
            return False
    return True


def palindrome(string,start,stop):
    '''final working function'''
    Sv = convertlist(string)
    result = reverse(Sv,start,stop)
    if result == True:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ in "__main__":
    string = 'happy'
    print(palindrome(string,0,len(string)))
