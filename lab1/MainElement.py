#Method of removing main element for solving SLAE
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
    mainElement(matrixA, b)

#find matrix A
def countA():
    B = 10 * C
    print(f"\nMatrix C: \n{C}")
    print(f"\nMatrix B: \n{B}")
    print(f"\nMatrix D: \n{D}")
    B.shape == D.shape #check the equality of matrixes
    A = B + D 
    return A

#main element method
def mainElement(matrixA, b):
    max = 0
    str = 0
    for i in range(matrixA.shape[0] - 1): 
        for j in range(i, matrixA.shape[0]): 
            if(matrixA[i][j] > max):
                max = matrixA[i][j]
                str = i
        
        #changing rows in a matrix A
        changing = np.repeat(matrixA[i], 1)
        matrixA[i] = matrixA[str]
        matrixA[str] = changing

        #changing rows in a matrix b
        changing = np.repeat(b[i], 1)
        b[i] = b[str]
        b[str] = changing

        #dividing on the max element
        matrixA[i] /= max
        b[i] /= max

        


main()