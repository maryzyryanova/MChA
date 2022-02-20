#Solving SLAE using method of simple iteration

import numpy as np
def define():
    A = np.array([])
    b = np.array([4.2 for i in range(5)])
    C = np.array([
        [0.01, 0, -0.02, 0, 0],
        [0.01, 0.01, -0.02, 0, 0],
        [0, 0.01, 0.01, 0, -0.02],
        [0, 0, 0.01, 0.01, 0],
        [0, 0, 0, 0.01, 0.01]
    ])
    D = np.array([
        [1.33, 0.21, 0.17, 0.12, -0.13],
        [-0.13, -1.33, 0.11, 0.17, 0.12],
        [0.12, -0.13, -1.33, 0.11, 0.17],
        [0.17, 0.12, -0.13, -1.33, 0.11],
        [0.11, 0.67, 0.12, -0.13, -1.33]
    ])
    A = 10*C + D
    return A, b

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

def main():
    print("1. Method of simple iteration: ")
    A, b = define()
    checkZero(A)
    if(check(A) != 0):
        alfa = np.empty((A.shape[0], A.shape[0]), dtype = "float32")
        beta = np.empty((A.shape[0]), dtype = "float32")
        for i in range(A.shape[0]):
            for j in range(A.shape[0]):
                if(i == j):
                    alfa[i][j] = 0
                else:
                    alfa[i][j] = - int(A[i][j] / A[i][i] * 100000) / 10000
            beta[i] = int(b[i] / A[i][i] * 10000) / 10000
        print(alfa)
        print("\n")
        print(beta)

            
#x[k] = alfa + beta * x[k-1] 

main()