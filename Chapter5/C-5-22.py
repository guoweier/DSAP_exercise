# Develop an experiment to compare the relative efficiency of the extend method of Python's list class versus using repeated calls to append to accomplish the equivalent task.

from time import time

def exp_extend(seq):
    "Experiment time elapse for extend method of Python's list class."
    ori = []
    t1 = time()
    ori.extend(seq)
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
    seq = [i for i in range(100000)]
    print(exp_extend(seq))
    print(exp_rep_append(seq))

# Results:
# extend is about 10-folds faster than repeated append. 
