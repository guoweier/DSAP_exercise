# Write a python function that takes two three-dimentional numeric data sets and adds them componentwise.

def add_comp(data1,data2):
    if len(data1) != len(data2) or len(data1[0]) != len(data2[0]) or len(data1[0][0]) != len(data2[0][0]):
        print("Two datasets must in same length for each dimention.")
    else:
        outi = []
        for i in range(len(data1)):
            outj = []
            for j in range(len(data1[i])):
                outk = []
                for k in range(len(data1[i][j])):
                    outk.append(data1[i][j][k]+data2[i][j][k])
                outj.append(outk)
            outi.append(outj)
        return outi

if __name__ in "__main__":
    data1 = [[[1,2],[1,2]],[[1,2],[1,2]],[[1,2],[1,2]]]
    data2 = [[[3,4],[3,4]],[[3,4],[3,4]],[[3,4],[3,4]]]
    print(add_comp(data1,data2))
