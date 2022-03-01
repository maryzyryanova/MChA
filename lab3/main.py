'''Main part of the lab'''
from sympy import *
import shturm_method as sm
import split_roots as sr

def main():
    x = Symbol('x')
    y = x**3 - 6.4951 * x**2 - 31.2543 * x + 23.1782
    current_row = sm.shturm_row(y, x)
    amount_of_variables = sm.find_n(current_row, -10, x) - sm.find_n(current_row, 10, x)
    print(amount_of_variables)
    sr.plot()
main()