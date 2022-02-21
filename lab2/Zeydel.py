#Solving SLAE using Zeydel's method 
import numpy as np
import SimpleIterations as si

def method(A, b):
    

def main_function(A, b):
    si.checkZero(A)
    if(si.check(A) != 0):
        alfa = np.empty((A.shape[0], A.shape[0]), dtype = "float32")
        beta = np.empty((A.shape[0], 1), dtype = "float32")
        alfa, beta = si.findAlfaBeta(A, b, alfa, beta)
        