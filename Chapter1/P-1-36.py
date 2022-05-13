# count input words times

from collections import defaultdict
import unittest

def CountWords():
    words = input("Enter your list of words: ")
    wordsli = words.split(" ")
    uniWord = defaultdict(int)
    for word in wordsli:
        uniWord[word] += 1
    for key in uniWord:
        print('{} appears {} times'.format(key, uniWord[key]))
    return

if __name__ in "__main__":
    CountWords()
