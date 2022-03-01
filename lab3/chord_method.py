'''Chord Method'''
from sympy import *

def f(x):
    return x**3 - 6.4951 * x**2 - 31.2543 * x + 23.1782

def f1(x):
    return f(x).diff()

def chord_method():
    try:
        a, b = -10, 10
        x0 = (a + b) / 2
        xn = f(x0)
        xn1 = xn - f(xn) / f1(xn)
        iterations = 0
        while abs(xn1 - xn) > 0.0001:
            xn = xn1
            xn1 = xn - f(xn) / f1(xn)
            iterations += 1
        print(f"Iterations: {iterations}")
        print(f"Min root: {int(xn1 * 10000) / 10000}")
    except ValueError:
        print("Value is invalidate")