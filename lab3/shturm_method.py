'''Shturm Method'''
from sympy import * 
import numpy as np

def shturm_row():
    '''Create a shturm row'''
    output_row = []
    input_function = np.poly1d([1, -6.4951, -31.2543, 23.1782])
    first_difference = np.diff([1, -6.4951, -31.2543, 23.1782])
    output_row.append(input_function)
    output_row.append(np.poly1d(first_difference))
    for i in range(len(output_row)):
        if i != len(output_row) - 1:
            new_element = np.polydiv(output_row[i], output_row[i+1])[0]
            output_row.append(new_element)
        else:
            break
    for rows_elements in output_row:
        print(rows_elements)

shturm_row()
