'''Chord Method'''
from sympy import *
import numpy as np
import shturm_method as sm

def get_f_from_polinom(polinom):
    def f(x):
        val = polinom[0]
        for i in range(len(polinom)-1):
            val = val*x+polinom[i+1]
        return val
    return f

P = [1, -6.4951, -31.2543, 23.1782]
phi = get_f_from_polinom(P)

def N(interval_border):
    x = Symbol('x')
    output_row = sm.shturm_row(x**3 - 6.4951 * x**2 - 31.2543 * x + 23.1782)
    temp_array = []
    count = 0
    for row_element in output_row:
        temp_array.append(row_element.subs(x, interval_border))
    for i in range(1, len(temp_array)):
        if np.sign(temp_array[i-1]) != np.sign(temp_array[i]):
            count += 1
    return count

def get_bounds(a, b):
    if N(a) - N(b) == 0:
        return []
    if N(a) - N(b) == 1:
        return [(a, b)]
    m = a + (b - a) / (1.5 + np.random.random())
    return get_bounds(a, m) + get_bounds(m, b)

def dihotomia(l, r):
    iters=0
    while(abs(l-r)>0.0001):
        m=(r+l)/2
        if phi(l)*phi(m)<0:
            r = m
        else:
            l = m
        iters += 1

def hord(polinom, l, r):
        P0 = np.polyder(polinom).tolist()
        P00 = np.polyder(P0).tolist()
        der_der_phi = get_f_from_polinom(P00)
        iters=0
        if phi(r)*der_der_phi(r)>0:
            def get_next(xn_1):
                return xn_1-phi(xn_1)*(r-xn_1)/(phi(r)-phi(xn_1))
            x0 = l
            while abs(get_next(x0)-x0)>1e-4:
                x0 = get_next(x0)
                iters+=1
        else:
            def get_next(xn_1):
                return xn_1-phi(xn_1)*(l-xn_1)/(phi(l)-phi(xn_1))
            x0 = -6.4951
            while abs(get_next(x0)-x0)>1e-4:
                x0 = get_next(x0)
                iters+=1
        print(f"hord = {iters} iters, x0 = {x0}")

def chord_method():
    bounds = get_bounds(-10, 10)
    print(bounds)
    l=bounds[0][0]
    r=bounds[0][1]
    dihotomia(l, r)
    hord(P, l, r)