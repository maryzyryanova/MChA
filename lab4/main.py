from sympy import *
import iterations_method as iterations

x = Symbol('x')
y = Symbol('y')
eps = 1e-4
f1 = lambda x,y: tan(x*y + 0.1) - x
f2 = lambda x,y: 0.8*x**x + 2*y**2 - 1
iterations.plot(f1(x,y), f2(x,y))