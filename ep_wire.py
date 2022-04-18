# PHYS2160 Project Q1(a)
# Electric potential of a point above a
# uniformly charged of wire

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.constants import epsilon_0

z = np.linspace(0.1, 10, 100)
L = 2
Q = 1e-10
density = Q / L

numerical = []
# Use a variable to indicate which value of z is used
index = 0
constant = 1 / (4 * math.pi * epsilon_0) * density


def func(x):
    return 1 / math.sqrt(z[index] ** 2 + x ** 2)


for i in range(100):
    numerical.append(constant * quad(func, -L / 2, L / 2)[0])
    index += 1
# Convert list into numPy array
numerical = np.asarray(numerical)

analytical = []
for j in range(100):
    analytical.append(Q / (4 * math.pi * epsilon_0 * L) * math.log((math.sqrt(z[j] ** 2 + (L / 2) ** 2) + L / 2) /
                                                                   (math.sqrt(z[j] ** 2 + (L / 2) ** 2) - L / 2)))
analytical = np.asarray(analytical)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(z, numerical, c="b", label="Numerical solution")
ax.plot(z, analytical, c="r", ls=":", lw=5, label="analytical solution")
ax.set_xlabel("z")
ax.set_ylabel("V(z)")
ax.set_title("V(z) against z")
ax.legend(loc="upper right")
plt.show()
