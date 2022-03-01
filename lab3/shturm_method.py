'''Shturm Method'''
from sympy import *
import numpy as np

def shturm_row(y, x):
    '''Create a shturm row'''
    output_row = []
    output_row.append(y)
    output_row.append(y.diff())
    count = len(output_row)
    for i in range(0, count, 1):
        new_element = -div(output_row[i], output_row[i+1])[1]
        output_row.append(new_element)
        count += 1
    return output_row

def find_n(output_row, interval_border, x):
    '''Find N(a) and N(b)'''
    temp_array = []
    count = 0
    for row_element in output_row:
        temp_array.append(row_element.subs(x, interval_border))
    for i in range(1, len(temp_array)):
        if np.sign(temp_array[i-1]) != np.sign(temp_array[i]):
            count += 1
    return count