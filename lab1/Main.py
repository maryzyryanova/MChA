import GaussMethod as gauss_method
import WholeChoose as whole_choose
import PartlyChoose as partly_choose
import numpy as np

#defining matrix
def define():
    A = np.array([])
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
    A = 10*C + D
    return A, b


print("\n1. Using Gauss method:")
A, b = define()
gauss_method.gaussMethod(A, b)

print("\n2. Using method of choosing in columns: ")
A, b = define()
whole_choose.mainElement(A, b)

print("\n3. Using method of choosing in the whole matrix: ")
A, b = define()
partly_choose.findMainElement(A, b)
