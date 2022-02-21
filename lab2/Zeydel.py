#Solving SLAE using Zeydel's method 
import numpy as np
import SimpleIterations as si

def method(A, b, epsilon = 0.0001):
    n = len(A)
    x = np.empty((A.shape[0], 1), dtype = "float32")
    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= epsilon
        x = x_new
    return x

def main_function(A, b):
    roots = method(A, b)
    print(roots)