# generate sentences multiple times.

import string 
import random

def CheatingForKids():
    sentence = input("Enter the sentence: ")
    times = int(input("Enter the total repeat times you need to write: "))
    n = int(input("Enter the number of typos for each time: "))


    for j in range(times):
        elements = list(sentence)
        used = []
        for i in range(n):
            typoi = random.randint(0,len(elements)-1)
            if typoi not in used:
                if elements[typoi] in list(string.ascii_letters):
                    elements[typoi] = random.choice(list(string.ascii_letters))
                    used.append(typoi)
                else:
                    continue
            else:
                continue
        newSentence = ""
        for item in elements:
            newSentence += item
        PrintOut(newSentence,j)

def PrintOut(sentence,j):
    print('{}: {}'.format(j+1, sentence))
    return

if __name__ in "__main__":
    CheatingForKids()