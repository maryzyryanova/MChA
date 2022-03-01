from email import iterators
from sympy import *

def newtonsMethod(a,b):
        try:
            xn = (a+b)/2
            xn1 = xn - f(xn) / derrirative(xn)
            iterations = 0
            while abs(xn1-xn) > 1e-4:
                xn = xn1
                xn1 = xn - f(xn) / derrirative(xn)
                iterations += 1
            print(f"Iterations: {iterations}")
            print(f"Min root: {int(xn1 * 10000) / 10000}")
            return xn1
        except:
            print("Error!")
 
def derrirative(x) :
    return 3*x**2 - 12.9902*x - 31.2543
 
def f(x) :
    return x**3 - 6.4951 * x**2 - 31.2543 * x + 23.1782
 