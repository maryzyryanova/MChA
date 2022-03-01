'''Half Method'''
from sympy import *

def f(x):
    return x**3 - 6.4951 * x**2 - 31.2543 * x + 23.1782

def half_div():
    a, b = -10, 10
    f1 = f(a)
    f2 = f(b)
    if f1 * f2 >= 0:
        print("There is no roots")
    else:
        n = 1
        x = (a+b)/2
        f3 = f(x)
        iterations = 0
        while abs(f3) > 0.0001:
            x = (a+b)/2
            f3 = f(x)
            if f1 * f3 < 0:
                b = x
            else:
                a = x
                n += 1
            iterations += 1
    print(f"Iterations: {iterations}")
    print(f"Min root: {int(x * 10000) / 10000}")


