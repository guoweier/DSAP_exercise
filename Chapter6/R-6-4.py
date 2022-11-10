# Give a recursive method for removing all the elements from a stack.

def rm_stack(S):
    if len(S) == 0:
        return S
    else:
        S.pop()
        return rm_stack(S)

if __name__ in "__main__":
    S = [1,2,3,4,5,6]
    print(rm_stack(S))
