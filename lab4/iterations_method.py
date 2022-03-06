import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def plot(f1(x,y), f2(x,y)):
    x = np.arange(-10, 10, 0.01)
    sp = plt.subplot(224)
    plt.plot(f1)
    plt.plot(f2)
    sp.spines['left'].set_position('center')
    sp.spines['bottom'].set_position('center')
    plt.show()