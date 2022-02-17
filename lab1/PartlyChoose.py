#Gauss Method of choosing main element in the columns matrix for solving SLAE
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

def main():
    matrixA = countA()
    print(f"\nMatrix b: \n{b}")
    print(f"\nMatrix A: \n{matrixA}")
    findMainElement(matrixA, b)

def countA():
    B = 10 * C
    print(f"\nMatrix C: \n{C}")
    print(f"\nMatrix B: \n{B}")
    print(f"\nMatrix D: \n{D}")
    A = B + D 
    return A

def findMainElement(matrixA, b):
    for i in range(0, matrixA.shape[0]):

        #find max element and max index
        max_index = i
        max_element = matrixA[i][i]
        for j in range(i+1, matrixA.shape[0]):
            if(abs(max_element) < abs(matrixA[j][i])):
                max_index = j
                max_element = matrixA[j][i]

        #swapping strings
        if(i != max_index):
            b[i], b[max_index] = b[max_index], b[i]
            for j in range(i, matrixA.shape[0]):
                matrixA[i][j], matrixA[max_index][j] = matrixA[max_index][j], matrixA[i][j]
        
        #to triangle form
        for j in range(i+1, matrixA.shape[0]):
            if(matrixA[i][i] != 0):
                temp = matrixA[j][i] / matrixA[i][i]
                b[j] -= temp * b[i]
                matrixA[j][i] = 0
                for k in range(i + 1, matrixA.shape[0]):
                    matrixA[j][k] -= temp * matrixA[i][k]      
    print(f"\nMatrix in a triangle form: \n{matrixA}")  
    print(f"\nMatrix b: {b}")    

    #finding roots
    x = [0 for i in range(matrixA.shape[0])]
    for i in range(matrixA.shape[0] - 1, -1, -1):
        for j in range(i, matrixA.shape[0]):
            if(j == matrixA.shape[0] - 1): 
                break
            else:
                b[i] -= matrixA[i][j+1] * x[j+1]
        if(matrixA[i][i] != 0):
            x[i] = b[i] / matrixA[i][i]

    #printing roots
    print("\nThe result: ")
    for i in range(len(x)):
        print(f"x[{i+1}] = {x[i]}")

main()