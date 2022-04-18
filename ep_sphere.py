# PHYS2160 Project Q1(a)
# Electric potential of a point above a
# uniformly charged of sphere

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.constants import epsilon_0

z = np.linspace(0.1, 10, 100)
R = 1.25
Q = 1e-10

numerical = []
index = 0
constant = 1 / (4 * math.pi * epsilon_0) * Q


def func1(x):
    return x / R ** 3


def func2(x):
    return 1 / x ** 2


for i in range(100):
    if z[index] < R:
        numerical.append(constant * (-quad(func2, math.inf, R)[0] - quad(func1, R, z[index])[0]))
        index += 1
    elif z[index] > R:
        numerical.append(constant * -quad(func2, math.inf, z[index])[0])
        index += 1
numerical = np.asarray(numerical)

analytical = []
for j in range(100):
    if z[j] < R:
        analytical.append(Q / (8 * math.pi * epsilon_0 * R) * (3 - z[j] ** 2 / R ** 2))
    elif z[j] > R:
        analytical.append(Q / (4 * math.pi * epsilon_0 * z[j]))
analytical = np.asarray(analytical)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(z, numerical, c="b", label="Numerical solution")
ax.plot(z, analytical, c="r", label="analytical solution")
ax.set_xlabel("z")
ax.set_ylabel("V(z)")
ax.set_title("V(z) against z")
ax.legend(loc="upper right")
plt.show()
