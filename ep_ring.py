# PHYS2160 Project Q1(a)
# Electric potential of a point above a
# uniformly charged of ring

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.constants import epsilon_0

z = np.linspace(0.1, 10, 100)
R = 1
Q = 1e-10
density = Q / (2 * math.pi * R)

numerical = []


def func(x):
    return 1


for i in range(100):
    constant = 1 / (4 * math.pi * epsilon_0) * density * R / math.sqrt(R ** 2 + z[i] ** 2)
    numerical.append(constant * quad(func, 0, 2 * math.pi)[0])
numerical = np.asarray(numerical)

analytical = []
for j in range(100):
    analytical.append(Q / ((4 * math.pi * epsilon_0) * math.sqrt(z[j] ** 2 + R ** 2)))
analytical = np.asarray(analytical)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(z, numerical, c="b", label="Numerical solution")
ax.plot(z, analytical, c="r", ls=":", lw=5, label="analytical solution")
ax. set_xlabel("z")
ax. set_ylabel("V(z)")
ax. set_title("V(z) against z")
ax. legend(loc="upper right")
plt.show()
