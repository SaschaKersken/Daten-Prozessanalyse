import math
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1000, 10000)
y = []
for x_i in x:
    y.append(math.sqrt(x_i))

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(linewidth=2)
plt.axvline(linewidth=2)
plt.show()
