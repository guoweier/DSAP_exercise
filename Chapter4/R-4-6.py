def harmonic(n):
    '''Compute the nth harmonic number'''
    if n == 0:
        return 0
    else:
        return 1/n + harmonic(n-1)


if __name__ in '__main__':
    print(harmonic(4))
