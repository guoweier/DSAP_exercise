#python program generate out of range error message.

def out_index(data,n):
    out = []
    try:
        for k in range(len(data)):
            data[n] = data[k]
        a = "happy"
    except IndexError:
        a="Don't try buffer overflow attacks in Python!"
    return a

data = [1,2,3]
n=10
print(out_index(data,n))


