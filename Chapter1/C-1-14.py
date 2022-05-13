#python function, takes a sequence of integer values. 
#determines if there is a distinct pair of numbers in the seq whose product is odd.

seq = [1,2,3,4,5]

def product_odd(seq):
    out = []
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            if (seq[i]*seq[j]) % 2 == 1:
                out.append((seq[i],seq[j]))
    if len(out) != 0:
        return (True,out)
    else:
        return None

print(product_odd(seq))