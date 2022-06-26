# Experimentally evaluate the efficiency of the pop method of Python's list class when using varying indices as a parameter, as we did for insert on page 205. Report your results akin to Table 5.5.

from time import time

def check_pop(data, n):
    "Check the pop method of Python's list."
    t1 = time()
    for j in range(n):
        data.pop(len(data)-1)
    t2 = time()
    elapse = t2-t1
    return elapse

if __name__ in "__main__":
    data = list(i for i in range(100))
    n = 100
    print(check_pop(data,n))

# pop(0)
# n=100: 2.09e-5
# n=1,000: 0.000242
# n=10,000: 0.01399
# n=100,000: 1.9718
# n=1,000,000: 412.545

# pop(len(data)-1)
# n=100: 2.19e-5
# n=1,000: 0.000232
# n=10,000: 0.00289
# n=100,000: 0.02488
# n=1,000,000: 0.269
