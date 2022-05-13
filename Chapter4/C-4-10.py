def log2int(n):
    '''Return the integer part of teh base-two logarithm of n.'''
    if n//2 == 0:
        return 0
    else:
        return log2int(n//2) + 1

if __name__ in '__main__':
    n = 14
    print(log2int(n))
