#Gauss Method for solving SLAE
import numpy as np

#defining matrixes 
b = np.array([4.2 for i in range(5)])
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

#main function
def main():
    matrixA = countA()
    print(f"\nMatrix b: \n{b}")
    print(f"\nMatrix A: \n{matrixA}")  
    matrixA = straight_stroke(matrixA)
    print(f"\nMatrix A after the straight stroke: \n{matrixA}")
    print(f"\nMatrix b after the straight stroke: \n{b}\n")
    invert_stroke(matrixA)

#find matrix A
def countA():
    B = 10 * C
    print(f"\nMatrix C: \n{C}")
    print(f"\nMatrix B: \n{B}")
    print(f"\nMatrix D: \n{D}")
    B.shape == D.shape #check the equality of matrixes
    A = B + D 
    return A

#main koeff q
def count_q(i, j, matrixA):
    q = matrixA[j][i-1] / matrixA[i-1][i-1] #counting the main koeff
    return q

#straight stroke
def straight_stroke(matrixA):
    for i in range(1, matrixA.shape):
        for j in range(i, matrixA.shape):
            q = count_q(i, j, matrixA)
            for k in range(matrixA.shape):
                matrixA[j][k] = matrixA[j][k] - q * matrixA[i-1][k]
                b[k] -= q * b[i]
    return matrixA

#invert stroke (something wrong here)
def invert_stroke(matrixA):
    x = [0 for i in range(matrixA.shape)] #the list of the koeffs
    for i in range(matrixA.shape - 1, -1, -1):
        x[i] = b[i] - sum([matrixA[i][j] * x[j] for j in range(i+1, matrixA.shape - 1)])/matrixA[i][i]
    print("The result:")
    for i in range(matrixA.shape):
        print(f"x[{i+1}] = {x[i]}")

main()