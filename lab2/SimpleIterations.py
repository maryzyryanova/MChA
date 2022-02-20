#Solving SLAE using method of simple iteration
import numpy as np

def check(A):
    for i in range(A.shape[0]):
        temp = 0
        for j in range(i, A.shape[0]):
            if(i != j):
                temp += abs(A[i][j])
        if(abs(A[i][i]) > temp):
            continue
        else:
            print(f"Convergence condition isn't keep! String with error: {i}")
            return 0
    return 1
            
def checkZero(A):
    for i in range(A.shape[0]):
        if(A[i][i] == 0):
            print(f"Element A[{i}][{i}] = 0!")

def findAlfaBeta(A, b, alfa, beta):
    for i in range(A.shape[0]):
            for j in range(A.shape[0]):
                if(i == j):
                    alfa[i][j] = 0
                else:
                    alfa[i][j] = - int(A[i][j] / A[i][i] * 10000) / 10000
            beta[i][0] = int(b[i] / A[i][i] * 10000) / 10000
    return alfa, beta

def findRoots(A, alfa, beta, x0):
    for i in range(A.shape[0]):
        x0 = beta + alfa.dot(x0)
    for i in range(len(x0)):
        x0[i] = int(x0[i] * 10000) / 10000
    print(x0)

def mainFunction(A, b):
    checkZero(A)
    if(check(A) != 0):
        alfa = np.empty((A.shape[0], A.shape[0]), dtype = "float32")
        beta = np.empty((A.shape[0], 1), dtype = "float32")
        alfa, beta = findAlfaBeta(A, b, alfa, beta)
        x0 = b.copy()
        findRoots(A, alfa, beta, x0)