# Question
# Provide a nonrecursive implementation of the _draw_interval_ function for the English ruler project.

# Output examples
# ---- 0
# -
# --
# -
# ---
# -
# --
# -
# ---- 1

# logic
# if c = the length of the center tick, then there are 2**c-1 lines.
# for instance: c = 3, to draw 2**3-1 = 7 lines.
# Index   Dash      Condition               Example
# 0       -         i % 2**1 == i % 2**0    0 % 2 == 0 % 1 = 0
# 1       --        i % 2**2 == i % 2**1    1 % 4 == 1 % 2 = 1
# 2       -         i % 2**1 == i % 2**0    2 % 2 == 2 % 1 = 0
# 3       ---       i % 2**3 == i % 2**2    3 % 8 == 3 % 4 = 3
# 4       -         i % 2**1 == i % 2**0    4 % 2 == 4 % 1 = 0
# 5       --        i % 2**2 == i % 2**1    5 % 4 == 5 % 2 = 1
# 6       -         i % 2**1 == i % 2**0    6 % 2 == 6 % 1 = 0
# for each index, for c in range(1,center_length),
# if i % 2**c == i % 2**(c-1), draw_line(c)


def draw_line(tick_length, tick_label=''):
    '''Draw one line with given tick length (followed by optional label).'''
    line = '-'*tick_length
    if tick_label:
        line += ' '+tick_label
    print(line)

def draw_interval(center_length):
    '''Draw tick interval based upon a central tick length.'''
    for i in range(2**center_length-1):
        for c in range(1,center_length+1):
            if i%(2**c) == i%(2**(c-1)):
                draw_line(c)
                break


def draw_ruler(num_inches, major_length):
    '''Draw English ruler with give number of inches, major tick length.'''
    draw_line(major_length, '0')
    for j in range(1, 1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length,str(j))


if __name__ in '__main__':
    num_inches = 2
    major_length = 3
    draw_ruler(num_inches,major_length)
