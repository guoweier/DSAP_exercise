# Perform experiments to evaluate the efficiency of the remove method of Python's list class, as we did for insert on page 205. Use known values so that all removals occur either at the beginning, middle, or end of the list. Report your results akin to Table 5.5.

from time import time

def exp_rem_begin(seq):
    "Experiment time elapse for remove() the value at beginning."
    t1 = time()
    for i in range(len(seq)):
        seq.remove(seq[0])
    t2 = time()
    e = t2-t1
    return e

def exp_rem_middle(seq):
    "Experiment time elapse for remove() the value in middle."
    t1 = time()
    for i in range(len(seq)):
        seq.remove(seq[(len(seq)-1)//2])
    t2 = time()
    e = t2-t1
    return e

def exp_rem_end(seq):
    "Experiment time elapse for remove() the value at end."
    t1 = time()
    for i in range(len(seq)):
        seq.remove(seq[len(seq)-1])
    t2 = time()
    e = t2-t1
    return e

if __name__ in "__main__":
    seq = [None for i in range(200000)]
    print(exp_rem_begin(seq))
    print(exp_rem_middle(seq))
    print(exp_rem_end(seq))


# Results
# Remove the element at beginning is the slowest.
# Remove the element at middle and at end are with similar speed, the end may be slightly faster.
