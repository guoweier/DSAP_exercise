# Based on the discussion of page 207, develop an experiment to compare the efficiency of Python's list comprehension syntax versus the construction of a list by means of repeated calls to append.

from time import time

def exp_compreh(seq):
    "Experiment time elapse for list comprehension."
    ori = []
    t1 = time()
    list = [i for i in seq]
    t2 = time()
    elapse = t2 - t1
    return elapse

def exp_rep_append(seq):
    "Experiment time elapse for repeated calls to append to accomplish the equivalent task."
    ori = []
    t1 = time()
    for item in seq:
        ori.append(item)
    t2 = time()
    elapse = t2 - t1
    return elapse

if __name__ in "__main__":
    seq = [i for i in range(1000000)]
    print(exp_compreh(seq))
    print(exp_rep_append(seq))

# Results:
# list comprehension is about 3-folds faster than repeated append. 
