'''Main part of the lab'''
from sympy import *
import shturm_method as sm
import split_roots as sr
import half_method as hm
import chord_method as cm
import newton_method as nm

def main():
    x = Symbol('x')
    current_row = sm.shturm_row(hm.f(x))
    amount_of_variables = sm.find_n(current_row, -10, x) - sm.find_n(current_row, 10, x)
    print(f"\nAmount of variables, using Shturm Method: {amount_of_variables}")    
    print("\n1. Half division method: ")
    hm.half_div()
    print("\n2. Chord method: ")
    cm.chord_method()
    print("\n3. Newton method: ")
    nm.newtonsMethod(-10, 0)
    sr.plot()

main()