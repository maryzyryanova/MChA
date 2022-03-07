import numpy as np
import sympy

def get_x(x, y):
    return np.tan(x*y + 0.1) 

def get_y(x):
    return np.sqrt((1-0.8*(x**2))/2)

def simple_iterations(first_approximation, eps):
    result_array = np.asarray(first_approximation)
    temp = 1
    iterations_counter = 0
    while temp > eps:
        new_x = result_array.copy()
        new_x[0], new_x[1] = get_x(result_array[0], result_array[1]), get_y(result_array[0])
        temp = np.max(np.abs(result_array - new_x))
        result_array = new_x.copy()
        iterations_counter += 1
    return result_array, iterations_counter

def print_result(first_approximation, eps):
    result_to_print, iterations_counter = simple_iterations(first_approximation, eps)
    x_variable = int(result_to_print[0] * 10000)/10000
    y_variable = int(result_to_print[1] * 10000)/10000
    print(f"x = {x_variable}\ny = {y_variable}\nIterations: {iterations_counter}")