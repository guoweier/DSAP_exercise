import itertools

def zip(*args, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = itertools.repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield list(values)

def pairwise(iterable):
	a,b = itertools.tee(iterable)
	next(b, None)
	return zip(a,b)

def get_allele(a,b):
	if a == b:
		allele = a
	elif a == "NA" or b == "NA":
		allele = "NA"
	elif (a == "1" and b == "2") or (a == "2" and b == "1"):
		allele = "1.5"
	return allele

if __name__ in "__main__":
    
