# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:13:01 2022

@author: Owner
"""

import numpy as np
import matplotlib.pyplot as plt

#I.C.'s
L = 10
x = np.linspace(0, L, 51)
u_0 = 1

fig, ax = plt.subplots()
f = np.where(x < L/2, 2*u_0/L * x, 2*u_0/L * (L-x))
ax.plot(x, f)
plt.show()

#3d plots

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
x, t = np.meshgrid(np.linspace(0, 10, 51), np.linspace(0, 5, 31), indexing = 'ij')
f = np.where(x < L/2, 2*u_0/L * x, 2*u_0/L * (L-x))
u = u_0/2 - 16*u_0/(np.pi**2)*()

ax.plot_surface(x, t, f)
