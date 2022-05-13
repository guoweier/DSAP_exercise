vowels = ['a','e','i','o','u']

def vowelvsconsonant(string,n,vownum=0,connum=0):
    '''Count the number of vowels and consonants.

    string:     the input string.
    n:          the string length.
    '''
    if n == 0:
        if vownum > connum:
            print("The string has more vowels than consonants.")
        elif vownum == connum:
            print("The string has same number of vowels and consonants.")
        else:
            print("The string has more consonants than vowels.")
    else:
        if string[n-1] in vowels:
            vownum += 1
        else:
            connum += 1
        vowelvsconsonant(string,n-1,vownum,connum)

if __name__ in '__main__':
    string = 'baibey'
    vowelvsconsonant(string,len(string))
