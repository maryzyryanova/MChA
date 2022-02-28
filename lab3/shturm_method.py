'''Shturm Method'''
from sympy import * 
import numpy as np

def shturm_row():
    '''Create a shturm row'''
    x = Symbol('x')
    y = x**3 - 6.4951 * x**2 - 31.2543 * x + 23.1782
    output_row = []
    output_row.append(y)
    output_row.append(y.diff())
    count = len(output_row)
    for i in range(0, count, 1):
        new_element = div(output_row[i], output_row[i+1])[1]
        output_row.append(new_element)
        count += 1
    print(output_row)

shturm_row()
