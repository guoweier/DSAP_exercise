# python program generate all possible strings formed by using the characters:
# c,a,t,d,o,g exactly once.


def printAllKLength(set, k):
 
    n = len(set)
    printAllKLengthRec(set, "", n, k)

def printAllKLengthRec(set, prefix, n, k):
    if k==0:
        print(prefix)
        return
    for i in range(n):
        if set[i] not in prefix:
            newPrefix = prefix+set[i]
            printAllKLengthRec(set, newPrefix, n, k-1)

if __name__ == "__main__":
    set1 = ["c","a","t","d","o","g"]
    k = 6
    printAllKLength(set1, k)
