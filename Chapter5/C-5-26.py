# Let B be an array of size n >= 6 containing integers from 1 to n-5, inclusive, with exactly five repeated. Describe a good algorithm for finding the five integers in B that are repeated.

def find_five(seq):
    "Find 5 repeated elements in the sequence."
    seq_sort = sorted(seq)
    result = []
    for i in range(len(seq_sort)-1):
        j = i+1
        if seq[i] == seq[j]:
            rep_el = seq[i]
    for i in range(len(seq)):
        if seq[i] == rep_el:
            result.append(i)
    return (rep_el,result)

if __name__ in "__main__":
    a = [1,23,4,12,4,15,9,10,4,20,349,39,3,4,4]
    out = find_five(a)
    print(out)
