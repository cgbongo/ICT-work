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
def df(f, x, h, i):
    if i == 1:
        return (f(x+h) - f(x-h))/(2*h) 
    if i == 2:
        return (f(x+h) - 2*f(x) + f(x-h))/(h**2)
    if i == 3:
        return (f(x+2*h) - 2*f(x+h) + 2*f(x-h) - f(x-2*h))/(2*(h**3))

x = np.linspace(-1, 5, 200)
a = 1

    #exact
def log_func(x):
    return np.log(1+x)

    #auto taylor
def taylor_log(x, n, h):
    taylor_sum = log_func(a)
    for i in range(1, n+1):
        term = df(log_func, a, h, i)
        taylor_sum += term/factorial(i) * (x-a)**i
    return taylor_sum
