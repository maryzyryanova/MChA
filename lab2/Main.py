import numpy as np
import SimpleIterations as si
import Zeydel as zeydel

def define():
    A = np.array([])
    b = np.array([[1.2], [2.2], [4.0], [0], [-1.2]])
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

def main():
    print("1. Simple iterations method: ")
    A, b = define()
    si.mainFunction(A, b)

    print("2. Zeydel method: ")
    A, b = define()
    zeydel.main_function(A, b)

main()
