import numpy as np
import sympy

def get_x(x, y):
    return sympy.tan(x*y + 0.1) 

def get_y(x, y):
    return sympy.sqrt((1-0.8*x**2)/2)

def simple_iterations(first_approximation, eps):
    result_array = np.array(first_approximation)
    temp = 1
    while temp > eps:
        new_x = np.copy(result_array)
        new_x[0] = get_x(*new_x)
        new_x[1] = get_y(*new_x)
        temp = np.max(np.abs(result_array - new_x))
        result_array = new_x
    print(result_array)