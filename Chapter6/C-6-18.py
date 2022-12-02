# Show how to use the transfer function, described in Exercise R-6-3, and two temporary stacks, to replace the contents of a given stack S with those same elements, but in reversed order.

def transfer(S,T):
    for i in range(len(S)):
        v = S.pop()
        T.append(v)
    return S,T

if __name__ in "__main__":
    S = [1,2,3,4,5,6,7]
    T1 = []
    T2 = []
    S,T1 = transfer(S, T1)
    T1,T2 = transfer(T1, T2)
    T2,S = transfer(T2, S)
    print(S)

    
