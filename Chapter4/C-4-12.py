def product(m,n):
    '''Compute the product of two positive integers.
    m:  the first integer;
    n:  the second integer;
    '''
    if n == 0:
        return 0
    else:
        return m + product(m,n-1)

if __name__ in '__main__':
    print(product(8,0))
