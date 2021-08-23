import math
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 1000)
y = []
for x_i in x:
    y.append(math.exp(-x_i ** 2))

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(linewidth=2)
plt.axvline(linewidth=2)
plt.show()
