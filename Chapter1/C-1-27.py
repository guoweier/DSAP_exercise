# modify the generator to import factors in an increasing order.



def factors_self(n):
    k = 1
    a = []
    while k*k < n:
        if n%k == 0:
            yield k
            yield n//k
        k += 1
    if k*k == n:
        yield k

out = list(factors_self(100))
out.sort()
print(out)
