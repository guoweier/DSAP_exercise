# The syntax data.remove(value) for Python list data removes only the first occurence of element value from the list. Give an implementation of a function, with signature remove_all(data, value), that removes all occurrences of value from the given list, such that the worst-case running time of the function is O(n) on a list with n elements. Not that it is not efficient enough in general to rely on repeated calls to remove.

def remove_all(data,value):
    "Remove all occurences of value from the given data."
    new_data = []
    for i in range(len(data)):
        if data[i] != value:
            new_data.append(data[i])
    return new_data


if __name__ in "__main__":
    data = [i for i in range(10)]
    data = data*3
    value = 3
    print(remove_all(data,value))
    print(data)
