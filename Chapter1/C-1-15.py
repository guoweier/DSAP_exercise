#python function.
#takes a sequence of numbers and determines if all the numbers are different from each other. 


def unique(data):
    distinct = []
    for item in data:
        if item not in distinct:
            distinct.append(item)
    if len(distinct) == len(data):
        return True
    else:
        return False


seq = [1,2,3,4]

print(unique(seq))