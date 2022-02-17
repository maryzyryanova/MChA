#Gauss Method of choosing main element in the whole matrix for solving SLAE
import numpy as np

#main element method
def mainElement(matrixA, b):
    for i in range(matrixA.shape[0] - 1): 
        max = 0
        str = 0
        for j in range(i, matrixA.shape[0]): 
            if(abs(matrixA[j][i]) > abs(max)):
                max = matrixA[j][i]
                str = j
        
        #changing rows in a matrix A
        matrixA[i], matrixA[str] = matrixA[str], matrixA[i]

        #changing rows in a matrix b
        b[i], b[str] = b[str], b[i]

        #dividing on the max element
        matrixA[i] /= max
        b[i] /= max

        #counting new elements
        for k in range(i+1, matrixA.shape[0]):
            temp = matrixA[k][i]
            matrixA[k] -= matrixA[i] * temp 
            b[k] -= b[i] * temp
    
    #finding roots
    matrixA = np.array(matrixA)
    roots = [b[b.shape[0] - 1] / (matrixA[matrixA.shape[0] - 1][matrixA.shape[0] - 1])]
    for i in range(matrixA.shape[0] - 2, -1, -1):
        temp = b[i]
        for j in range(len(roots)):
            temp -= roots[j] * matrixA[i][matrixA.shape[0] - 1 - j]
        roots.append(temp)
    
    #reverting the list
    x = []
    for i in reversed(roots) : 
        x.append(i)
    print("\nThe result: ")
    for i in range(len(x)):
        print(f"x[{i+1}] = {round(x[i], 4)}")