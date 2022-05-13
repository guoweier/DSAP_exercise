def excludevalue(data,i):
    '''exclude ith value in data.'''
    if 1 <= i <= len(data)-1:
        newdata = data[0:i]+data[(i+1):len(data)]
    elif i == 0:
        newdata = data[1:len(data)]
    elif i == len(data):
        newdata = data[0:(len(data)-1)]

    return newdata




def subset(data,dataset):
    '''Return all the subset of data.

    data:       the vector with numbers.
    dataset:    store subsets (unrepeated). 
    '''
    if len(data) == 1:
        if data not in dataset:
            dataset.append(data)
    elif len(data) > 1:
        for i in range(len(data)):
            newdata = excludevalue(data,i)
            if newdata not in dataset:
                dataset.append(newdata)
            dataset = subset(newdata, dataset)

    return dataset


if __name__ in '__main__':
    dataset = []
    data = [1,1,1,4]
    result = subset(data,dataset)
    result.sort()
    for item in result:
        print(item)
