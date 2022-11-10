# Implement a function with signature transfer(S,T) that transfers all elements from stack S onto stack T, so that the element that starts at the botoom of S ends up at the top of T.

def transfer(S,T):
    for i in range(len(S)):
        v = S.pop()
        T.append(v)
    return S,T

if __name__ in "__main__":
    S = [1,2,3,4,5,6,7]
    T = []
    print(transfer(S,T))
