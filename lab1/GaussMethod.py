import numpy as np

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
    k = 1
    for i in 5:
        for j in 5:
            matrixA[i][j] = matrixA[i][j] - count_q(i, k, matrixA) 
        k += 1

#find matrix A
def countA():
    B = 10 * C
    B.shape == D.shape #check the equality of matrixes
    A = B + D 
    return A

#main koeff q
def count_q(i, k, matrixA):
    q = np.array()
    q[i][k] = matrixA[i][k] / matrixA[k][k] #counting the main koeff
    return q[i][k]

main()