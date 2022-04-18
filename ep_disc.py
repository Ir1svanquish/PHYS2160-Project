# PHYS2160 Project Q1(a)
# Electric potential of a point above a
# uniformly charged of disc

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.constants import epsilon_0

z = np.linspace(0.1, 10, 100)
R = 1
Q = 1e-10
density = Q / (math.pi * R ** 2)

numerical = []
index = 0
constant = density / (2 * epsilon_0)


def func(x):
    return x / math.sqrt(x ** 2 + z[index] ** 2)


for i in range(100):
    numerical.append(constant * quad(func, 0, R)[0])
    index += 1
numerical = np.asarray(numerical)

analytical = []
for j in range(100):
    analytical.append(Q / (2 * math.pi * epsilon_0 * R ** 2) * (math.sqrt(z[j] ** 2 + R ** 2) - z[j]))
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
