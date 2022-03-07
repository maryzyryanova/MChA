from sympy import symbols
import numpy
import sympy

def get_x(x, y):
    return numpy.tan(x*y + 0.1) - x

def get_y(x, y):
    return 0.8*x**2 + 2*y**2 - 1

def diff_matrix(x, y):
    return numpy.array([
        [y/(numpy.cos(x*y+0.1))**2-1, x/(numpy.cos(x*y+0.1))**2], 
        [2*0.8*x, 4*y]
    ])

def newton_method(first_approximation, eps):
    matrix_result = numpy.asarray([0.0, 0.0])
    temp, iterations = 1, 0
    while temp > eps:
        matrix_empty = diff_matrix(*first_approximation)
        matrix_x = [[get_x(*first_approximation), matrix_empty[0][1]],
                    [get_y(*first_approximation), matrix_empty[1][1]]]
        matrix_y = [[matrix_empty[0][0], get_x(*first_approximation)],
                    [matrix_empty[0][1], get_y(*first_approximation)]]
        det_matrix_empty = numpy.linalg.det(matrix_empty)
        det_matrix_x = numpy.linalg.det(matrix_x)
        det_matrix_y = numpy.linalg.det(matrix_y)
        matrix_result[0] = first_approximation[0] - det_matrix_x/det_matrix_empty
        matrix_result[1] = first_approximation[1] - det_matrix_y/det_matrix_empty
        temp = numpy.max(numpy.abs(first_approximation - matrix_result))
        first_approximation = matrix_result
        iterations += 1
    return first_approximation, iterations

def print_result(first_approximation, eps):
    result_to_print, iterations_counter = newton_method(first_approximation, eps)
    x_variable = int(result_to_print[0] * 10000)/10000
    y_variable = int(result_to_print[1] * 10000)/10000
    print(f"x = {x_variable}\ny = {y_variable}\nIterations: {iterations_counter}")
    
