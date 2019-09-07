## FindDeterminant.py
## Elliot Treble
## 7/09/19


import random

'''
Find determinant of an n*n matrix
'''

print("Hello World")

def FindDet(matrix):
    print("-------------------------NEW MATRIX----------------------------")
    print(matrix)
    for row in matrix:
        if len(row) != len(matrix):
            print("matrix must be square")
            return -1
    return RecursiveHelper(matrix)


def RecursiveHelper(matrix):
    print("length of current matrix is ")
    print(len(matrix))
    if len(matrix) == 2:
        print(matrix)
        print("2 x 2 matrix has determinant ")
        print(matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]  ###base case
    else:
        result = 0
        for col in range(0, len(matrix)):
            print("iterating for column " + str(col) + " current matrix is " + str(matrix))
            result += matrix[0][col]*((-1)**col)*RecursiveHelper(BuildSubMatrix(matrix, col)) ## sum alternating sign of sub matrices
            print("last result is " + str(result))
        return result

def BuildSubMatrix(matrix, col):
    newMatrix = []
    for row in matrix[1:]:
        newRow = row.copy()
        print("removing " + str(newRow.pop(col)) + " from row " + str(row))
        print("new row is " + str(newRow))
        print("old row is " + str(row))
        print(newRow)
        newMatrix.append(newRow)
        print("new subMatrix is ")
        print(newMatrix)
    return newMatrix


def rdmSquareMatrixGenerator():
    ##randomize size of matrix
    print("GENERATING RANDOM MATRIX")
    size = random.randint(0,7)
    newMatrix = []
    for i in range(0, size):
        newRow = []
        for i in range(0, size):
            ##populate rows with random values
            newRow.append(random.randint(0,10))
        newMatrix.append(newRow)
    print("Matrix Generated")
    print(newMatrix)
    return newMatrix


print(FindDet(rdmSquareMatrixGenerator()))
