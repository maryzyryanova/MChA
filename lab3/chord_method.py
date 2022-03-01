'''Chord Method'''
from sympy import *

def f(x):
    return x**3 - 6.4951 * x**2 - 31.2543 * x + 23.1782

def chord_method():
    try:
        a, b = -10, 10
        iterations = 0
        while abs(b - a) > 0.0001:
            a = b - (b - a) * f(b)/ (f(b) - f(a))
            b = a - (a - b) * f(a)/ (f(a) - f(b))
            iterations += 1
            
        print(f"Iterations: {iterations}")
        print(f"Min root: {int(b * 10000) / 10000}")
    except ValueError:
        print("Value is invalidate")