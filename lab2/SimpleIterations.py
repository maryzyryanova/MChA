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
        for j in range(i, A.shape[0]):
            if(i != j):
                temp += abs(A[i][j])
        if(abs(A[i]) > temp):
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
        alfa, beta, x = []
        for k in range(1, A.shape[0] - 1):
            x[k] = alfa + beta * x[k-1]

    
main