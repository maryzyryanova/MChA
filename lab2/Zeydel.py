#Solving SLAE using Zeydel's method 
import numpy as np
import SimpleIterations as si

def method(alfa, beta, eps):
    x = np.zeros(alfa.shape[0])  
    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(alfa.shape[0]):
            s1 = sum(alfa[i][j] * x_new[j] for j in range(i))
            s2 = sum(alfa[i][j] * x[j] for j in range(i + 1, alfa.shape[0]))
            x_new[i] = (beta[i] - s1 - s2) / alfa[i][i]
        converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(alfa.shape[0]))) <= eps
        x = x_new
    return x

def main_function(A, b):
    si.checkZero(A)
    if(si.check(A) is True):
        alfa = np.empty((A.shape[0], A.shape[0]), dtype = "float32")
        beta = np.empty((A.shape[0], 1), dtype = "float32")
        alfa, beta = si.findAlfaBeta(A, b, alfa, beta)
        