'''Splitting roots using graphics method'''
import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def plot():
    x = np.arange(-10, 10, 0.01)
    sp = plt.subplot(224)
    plt.plot(x, x**3, x, 6.4951 * x**2 + 31.2543 * x - 23.1782)
    sp.spines['left'].set_position('center')
    sp.spines['bottom'].set_position('center')
    plt.show()
