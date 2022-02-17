import GaussMethod as gauss_method
import WholeChoose as whole_choose
import PartlyChoose as partly_choose
import numpy as np

#defining matrix
b = [4.2 for i in range(5)]
C = np.array([
    [],
    [],
    [],
    [],
    []
])
D = np.array([
    [],
    [],
    [],
    [],
    []
])

#count matrix A
def countA(C, D):
    B = 10 * C
    print(f"\nMatrix C: \n{C}")
    print(f"\nMatrix B: \n{B}")
    print(f"\nMatrix D: \n{D}")
    A = B + D 
    return A

gauss_method.gaussMethod(count(C, D), b)