# python function, reverse a list of n integers.

seq = [1,2,3,4,5,6]

def reverse(seq):
    reverse = []
    for i in range(1,len(seq)):
        reverse.append(seq[-i])
    reverse.append(seq[0])
    return reverse

print(reverse(seq))