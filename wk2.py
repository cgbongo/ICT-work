# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:43:46 2022

@author: Owner
"""
import numpy as np
import matplotlib.pyplot as plt
from math import e

def factorial(n):
    ftrl = 1
    for i in range(0, n):
        ftrl *= i+1
    return ftrl

def exptaylor(n, x):
    exptaylor = 0
    for i in range(0, n):
        exptaylor += (x**i)/factorial(i)
    return exptaylor

x = np.linspace(-2, 1, 100)
e_1 = e**x

plt.plot(x, e_1)
plt.show()
