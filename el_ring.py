# PHYS2160 Project Q1(b)
# Electric potential of an arbitrary point above a
# uniformly charged of sphere

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import epsilon_0

z = np.linspace(-5, 5, 10)
x = np.linspace(-5, 5, 10)
R = 1
Q = 1e-10
result = []


for i in range(10):
    for j in range(10):
        result.append(Q / ((4 * math.pi * epsilon_0) * math.sqrt(math.sqrt(z[i] ** 2 + x[j] ** 2) ** 2 + R ** 2)))
result = np.asarray(result)
result.resize(10, 10)


x, z = np.meshgrid(x, z)
fig = plt.figure()
ax = fig.add_subplot(111)
el = ax.contour(x, z, result, 11, colors="k", linewidths =1)
ax.clabel(el, inline=True, fontsize=5)
ax.set_xlabel("x(m)")
ax.set_ylabel("z(m)")
ax.set_title("Equipotential lines")
plt.show()
