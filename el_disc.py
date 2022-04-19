# PHYS2160 Project Q1(b)
# Electric potential of an arbitrary point above a
# uniformly charged of disc

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.constants import epsilon_0

z = np.linspace(-5, 5, 10)
x = np.linspace(-5, 5, 10)
R = 1
Q = 1e-10
density = Q / (math.pi * R ** 2)
index_1 = 0
index_2 = 0
constant = density / (2 * epsilon_0)
result = []

def func(s):
    return s / math.sqrt((s - abs(x[index_1])) ** 2 + z[index_2] ** 2)


for i in range(10):
    for j in range(10):
        result.append(constant * quad(func, 0, R)[0])
        index_1 += 1
    index_1 = 0
    index_2 += 1
result = np.asarray(result)
result.resize(10, 10)

x, z = np.meshgrid(x, z)
fig = plt.figure()
ax = fig.add_subplot(111)
el = ax.contour(x, z, result, 10, colors="k", linewidths =1)
ax.clabel(el, inline=True, fontsize=5)
ax.set_xlabel("x(m)")
ax.set_ylabel("z(m)")
ax.set_title("Equipotential lines")
plt.show()
