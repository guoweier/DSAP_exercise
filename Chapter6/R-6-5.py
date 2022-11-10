# Implement a function that reverses a list of elements by pushing them onto a stack in one order, and writing them back to the list in reversed order.

def reverse(L, S=list()):
    for i in range(len(L)):
        v = L.pop()
        S.append(v)
    for i in range(len(S)):
        L.append(S[i])
    return L

if __name__ in "__main__":
    L = [1,2,3,4,5,6]
    print(reverse(L))
