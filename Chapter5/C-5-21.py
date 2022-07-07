# In Section 5.4.2, we described four different ways to compose a long string: (1) repeated concatenation, (2) appending to a temporary list and then joining, (3) using list comprehension with join, and (4) using generator comprehension with join. Develop an experiment to test the efficiency of all four of these approaches and report your findings.

from time import time

def method1(document):
    "Experiment time elapse for repeated concatenation."
    letter = ""
    t1 = time()
    for c in document:
        if c.isalpha():
            letter += c
    t2 = time()
    elapse = t2-t1
    return elapse

def method2(document):
    "Experiment time elapse for appending to a temporary list and then joining."
    temp = []
    t1 = time()
    for c in document:
        if c.isalpha():
            temp.append(c)
        letters = ''.join(temp)
    t2 = time()
    elapse = t2-t1
    return elapse

def method3(document):
    "Experiment time elapse for using list comprehension with join."
    t1 = time()
    letters = ''.join([c for c in document if c.isalpha()])
    t2 = time()
    elapse = t2-t1
    return elapse

def method4(document):
    "Experiment time elapse for generator comprehension with join."
    t1 = time()
    letter = ''.join(c for c in document if c.isalpha())
    t2 = time()
    elapse = t2-t1
    return elapse

if __name__ in "__main__":
    doc = "Baibey is my little cat. She is a domestic shorthair tabby. She eats a lot, and she makes noise every single minute."
    document = doc * 100000
    print(method1(document))
    #print(method2(document))
    print(method3(document))
    print(method4(document))


# Results:
# List comprehension with join (Method 3) is the fastest.
# Generator comprehension with join (Method 4) is the second fast.
# Repeated concatenation (Method 1) is the third.
# Temporary list and join (Method 2) is the worst. 
