def strtoint(string,n):
    '''converting a string of digits to integer

    string: prepared string for converting;
    n: the length of string;
    '''
    if n == 0:
        return 0
    else:
        return int(string[n-1])*(10**(len(string)-n)) + strtoint(string,n-1)

if __name__ in '__main__':
    string = '150420'
    print(strtoint(string,6))
