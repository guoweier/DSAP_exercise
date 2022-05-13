# pyhton function that remove punctuations

import string

def remove_punc(s):
    punc = string.punctuation
    out_s = ""
    nopunc_s = [char for char in s if char not in punc]
    for item in nopunc_s:
        out_s += item
    return out_s

s = "Happy Birthday, Baibey!"
print(remove_punc(s))
