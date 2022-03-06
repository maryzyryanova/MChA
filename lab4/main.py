from sympy import * 

x = Symbol('x')
y = Symbol('y')
eps = 1e-4
f1 = tan(x*y + 0.1) - x
f2 = 0.8*x**x + 2*y**2 - 1

