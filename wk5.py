# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:21:56 2022

@author: Owner
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi, e


#Q1
x, f = np.loadtxt("data_points.txt", unpack = True)

X = np.atleast_2d(x).T
F = np.atleast_2d(f).T

p0 = X**0
p1 = X**1
p2 = X**2

P = np.column_stack((p0, p1, p2))

a = np.linalg.inv(P.T @ P) @ (P.T @ F)
smooth_x = np.linspace(0, 3)
fitted_trend = a[0] + a[1] * smooth_x + a[2] * smooth_x**2
fig, ax = plt.subplots()
ax.scatter(x, f)
ax.plot(smooth_x, fitted_trend, 'r')

plt.show()

#Q2
x = np.linspace(-2*pi, 2*pi)
f = x*(pi-x)
a = [8/pi, 0, 8/(27*pi)]
poly = 0

for i in range(1, 4):
    poly += a[i-1]*np.sin((i*x))

fig, ax = plt.subplots()
ax.plot(x, f)
ax.plot(x, poly)
plt.show()
                     
#Q3
x = np.linspace(0, 1)
f = e*x
p = [1, 2*x-1, 6*x**2 - 6*x +1]
