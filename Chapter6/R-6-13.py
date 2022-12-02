# Suppose you have deque D containing the numbers (1,2,3,4,5,6,7,8), in this order. Suppose further that you have an initially empty queue Q. Give a code fragment that uses only D and Q (and no other variables) and results in D storing the elements in the order (1,2,3,5,4,6,7,8)

def order_deque(D=[1,2,3,4,5,6,7,8],Q=[]):
    # move 1,2,3,4,5 from D to Q.
    for i in range(5):
        Q.append(D[0])
        D.pop(0)
    # move 1,2,3 to the end of D
    for i in range(3):
        D.append(Q[0])
        Q.pop(0)
    # add 4 and 5 to the beginning of D, with reversed order.
    for i in range(2):
        D = [Q[0]]+D
        Q.pop(0)
    # transfer 1,2,3 back to the beginning of D.
    for i in range(3):
        Q.append(D[-1])
        D.pop()
        D = [Q[0]]+D
        Q.pop()
    return D

if __name__ in "__main__":
    print(order_deque())
