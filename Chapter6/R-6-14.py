# Repeat the Question R-6-13 using the deque D and an initially empty stack S.

def order_deque_s(D=[1,2,3,4,5,6,7,8], S=[]):
    # move 1-5 into S
    for i in range(5):
        S = [D[0]] + S
        D.pop(0)
    # move 5 to the end of D.
    # add 4 to the beginning of D.
    D.append(S[0])
    S.pop(0)
    D = [S[0]]+D
    S.pop(0)
    # transfer 5 to the beginning of D.
    S = [D[-1]]+S
    D.pop()
    D = [S[0]]+D
    S.pop(0)
    # move 1,2,3 back to the D.
    for i in range(3):
        D = [S[0]] + D
        S.pop(0)

    return D 

if __name__ in "__main__":
    print(order_deque_s())
