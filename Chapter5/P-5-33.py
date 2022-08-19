# Write a python program for a matrix class that can add and multiply two-dimentional arrays of numbers, assuming the dimentions agree appropriately for the opertation.

class MatrixOperation:

    def __init__(self, matrix):
        "Create a matrix."
        self._matrix = matrix
        self._n1 = len(matrix)      # get matrix first dimention length
        self._n2 = len(matrix[0])   # get matrix second dimention length

    def AddMatrix(self):
        "Add all the numbers in matrix."
        sum = 0
        for i in range(self._n1):
            for j in range(self._n2):
                sum = sum + self._matrix[i][j]
        return sum

    def MultiplyMatrix(self):
        "multiply all the numbers in matrix."
        product = 1
        for i in range(self._n1):
            for j in range(self._n2):
                product = product * self._matrix[i][j]
        return product

if __name__ in "__main__":
    m = MatrixOperation([[1,2],[3,4],[2,3]])
    print(m.AddMatrix())
    print(m.MultiplyMatrix())
