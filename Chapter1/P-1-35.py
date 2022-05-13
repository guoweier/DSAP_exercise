#birthday paradox

from __future__ import unicode_literals
import random

def GetBirthday():  
    birthday = random.randint(1,365)
    return birthday

def CompareBirthdays(allBirthday, people):
    uniBirthday = []
    for birth in allBirthday:
        if birth not in uniBirthday:
            uniBirthday.append(birth)
    return uniBirthday
        

def BirthdayParadox():
    n = list(i*5 for i in range(1,21))
    for people in n:
        same = 0
        for text in range(1000):
            allBirthday = []
            for i in range(people):
                allBirthday.append(GetBirthday())
            uniBirthday = CompareBirthdays(allBirthday, people)
            if len(uniBirthday) < len(allBirthday):
                same += 1
        Prob = float(same/1000)
        print('{}, {}'.format(Prob, people))
    return




if __name__ in "__main__":
    BirthdayParadox()

