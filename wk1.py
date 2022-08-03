# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 18:09:13 2022

@author: conno
"""

import numpy as np
import matplotlib.pyplot as plt

def fwd_diff(f, x, h):
    return (f(x+h) - f(x))/h

def bwd_diff(f, x, h):
    return (f(x) - f(x-h))/h

def ctl_diff(f, x, h):
    return (f(x+h) - f(x-h))/(2*h)

x = np.linspace(-5, 5, 100)

def f1(x):
    return x**3

def f2(x):
    return 3*(x**2) - 2*x

def f3(x):
    return np.sin(x)

def df1(x):
    return 3*(x**2)

def df2(x):
    return 6*x - 2

def df3(x):
    return np.cos(x)

fig, ax = plt.subplots()
for f, df in zip((f1, f2, f3), (df1, df2, df3)):
    fwds = fwd_diff(f, x, h = 0.1)
    ax.plot(x, fwds)
    ax.plot(x, df(x), 'k', linestyle = '--')
plt.show()

fig, ax = plt.subplots()
ax.plot(x, df3(x), 'k', label = 'Exact')
for diff in (fwd_diff, bwd_diff, ctl_diff):
    approx_sol = diff(f3, x, h = 0.1)
    ax.plot(x, approx_sol, label = diff.__name__)
ax.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(x, df3(x), 'k', label = 'Exact')
for h in np.geomspace(0.1, 1e-5, 5):
    approx_sol = ctl_diff(f3, x, h)
    ax.plot(x, approx_sol, label = f'h = {h:.1e}')
ax.legend()
plt.show()

fig, ax = plt.subplots()
step_sizes = np.geomspace(1E-01, 1E-05)
for diff in (fwd_diff, bwd_diff, ctl_diff):
    approx = diff(f3, x=1, h=step_sizes)  # Do at x=1 for now
    error = np.abs(approx - df3(x=1))
    ax.loglog(step_sizes, error, label=diff.__name__)
ax.loglog(step_sizes, step_sizes, "k--", label="O(h)")
ax.loglog(step_sizes, step_sizes**2, "k-.", label="O(h^2)")
ax.legend()
plt.show()