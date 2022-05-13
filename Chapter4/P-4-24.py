def PuzzleSolve(k,S,U,target):
    for value in U:
        S.append(value)
        U.remove(value)
        if k == 1:
            Sstr = ''
            for v in S:
                Sstr += v
            if Sstr == target:
                print(Sstr)
        else:
            PuzzleSolve(k-1,S,U,target)
        S.remove(value)
        U.add(value)

if __name__ in '__main__':
    k = 3
    S = list()
    U = {'a','b','c'}
    target = 'cab'
    PuzzleSolve(k,S,U,target)
