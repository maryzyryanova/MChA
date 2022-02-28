'''Shturm Method'''
from sympy import * 
import numpy as np

def shturm_row():
    '''Create a shturm row'''
    x = Symbol('x')
    y = x**3 - 6.4951 * x**2 - 31.2543 * x + 23.1782
    print(y.diff())

shturm_row()
