#Gauss Method for solving SLAE
import numpy as np

#defining matrixes 
C = np.array([
    [0.2, 0, 0.2, 0, 0], 
    [0, 0.2, 0, 0.2, 0], 
    [0.2, 0, 0.2, 0, 0.2],
    [0, 0.2, 0, 0.2, 0],
    [0, 0, 0.2, 0, 0.2]
])
D = np.array([
    [2.33, 0.81, 0.67, 0.92, -0.53], 
    [-0.53, 2.33, 0.81, 0.67, 0.92], 
    [0.92, -0.53, 2.33, 0.81, 0.67], 
    [0.67, 0.92, -0.53, 2.33, 0.81], 
    [0.81, 0.67, 0.92, -0.53, 2.33]
])
b = np.array([
    [4, 2], 
    [4, 2],
    [4, 2],
    [4, 2],
    [4, 2]
])

#main function
def main():
    matrixA = countA()
    print(matrixA)  
    straight_stroke(matrixA)

#find matrix A
def countA():
    B = 10 * C
    B.shape == D.shape #check the equality of matrixes
    A = B + D 
    return A

#main koeff q
def count_q(i, j, matrixA):
    q = matrixA[j][i-1] / matrixA[i-1][i-1] #counting the main koeff
    return q

#straight stroke
def straight_stroke(matrixA):
    for i in range(1, 5):
        for j in range(i, 5):
            q = count_q(i, j, matrixA)
            for k in range(6):
                matrixA[j][k] = matrixA[j][k] - q * matrixA[i-1][k]
    return matrixA

#invert stroke
def invert_stroke(matrixA):
    x = [0 for i in range(5)] #the list of the koeffs
    for i in range(4, -1, -1):
        x[i] = matrixA[i][4]/matrixA[i][i]
        for j in range(4, -1, -1):
            x[i] = x[i] - matrixA[i][j] * x[j] / matrixA[i][i]
    return x


main()