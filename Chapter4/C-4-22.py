def power(x,n):
    '''Compute the value x**n for integer n.'''
    # n is even
    if n == 0:
        return 1
    else:
        result = 1
        if n%2 == 0:
            for i in range(n/2):
                result *= x**2
        else:
            for i in range((n-1)/2):
                result *= x**2
            result *= x
        return result


if __name__ in '__main__':
    x = 3
    n = 0
    print(power(x,n))
