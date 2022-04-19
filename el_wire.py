# PHYS2160 Project Q1(b)
# Electric potential of an arbitrary point above a
# uniformly charged of wire

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.constants import epsilon_0

z = np.linspace(-5.0, 5, 10)
x = np.linspace(-5.0, 5, 10)
L = 2
Q = 1e-10
density = Q / L
index = 0
constant = 1 / (4 * math.pi * epsilon_0) * density
result = []


def func(s):
    return 1 / math.sqrt(z[index] ** 2 + s ** 2)


for i in range(10):
    for j in range(10):
        result.append(constant * quad(func, -L / 2 - x[j], L / 2 - x[j])[0])
    index += 1
# Convert list into suitable numPy array
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
