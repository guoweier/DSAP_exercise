def move_direction(n,k):
    '''if n is odd, forward; if n is even, reverse.'''
    if k%2 == 1:
        if n%2 == 1:
            direct = [c,b,a]
        else:
            direct = [b,c,a]
    else:
        if n%2 == 1:
            direct = [b,c,a]
        else:
            direct = [c,b,a]
    return direct

def current_peg(n):
    '''locate the current peg of disk n.'''
    for peg in [a,b,c]:
        if n in peg:
            cur_peg = peg
    return cur_peg

def next_peg(n):
    '''decide the next moving peg for disk n.'''
    direct = move_direction(n,k)
    cur_peg = current_peg(n)
    for j in range(len(direct)):
        if cur_peg == direct[j]:
            if j == 2:
                next_peg = direct[0]
            else:
                next_peg = direct[j+1]
    return next_peg


def move_disk(n):
    '''move disks between pegs.'''
    nextpeg = next_peg(n)
    curpeg = current_peg(n)
    curpeg.remove(n)
    nextpeg.append(n)
    curpeg.sort()
    nextpeg.sort()
    print(str(a)+'\t'+str(b)+'\t'+str(c))

def hanoi(n):
    '''moving n disks:
    1. moving (n-1) disks to the temporary peg;
    2. move nth disk to the final peg;
    3. move (n-1) disks to the final peg.
    '''
    if n > 0:
        hanoi(n-1)
        move_disk(n)
        hanoi(n-1)


if __name__ in '__main__':
    k = 3
    a = []
    b = []
    c = []
    for i in range(k):
        a.append(i+1)
    print(str(a)+'\t'+str(b)+'\t'+str(c))
    print(hanoi(k))
