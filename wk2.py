# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:43:46 2022

@author: Owner
"""
import numpy as np
import matplotlib.pyplot as plt
from math import e

#factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

#exponential taylor
def better_exp(n, x):
    term = 1
    exp = term
    for i in range(1, n+1):
        term *= x / i
        exp += term
    return exp

x = np.linspace(-2, 2, 100)
n = 4
exp = e**x
fig, ax = plt.subplots()
ax.plot(x, exp, label = 'Exact')
ax.plot(x, better_exp(n, x), label = 'Taylor')
ax.legend()
plt.show()

#Circle stuff
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
F = X**2 + Y**2 - 1
plt.contour(X, Y, F, [0])
plt.gca().set_aspect('equal')
plt.show()

#Log function
def ctl_diff(f, x, h):
    return (f(x+h) - f(x-h))/(2*h)

x = np.linspace(-1, 3, 100)
a = 1

def log_func(x):
    return np.log(1+x)

def df(f, x, h):
    return ctl_diff(f, x, h)

def taylor_log(x, n):
    term = log_func(x)
    output = term
    for i in range(1, n+1):
        term = ctl_diff(log_func, a, 0.01)
        output += term/factorial(i) * (x-a)**i
    return output

plt.plot(x, log_func(x))
plt.plot(x, taylor_log(x, 3))
plt.show()
