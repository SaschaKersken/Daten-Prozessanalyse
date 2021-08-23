import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1000, 5000)
y = x ** 2

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(linewidth=2)
plt.axvline(linewidth=2)
plt.show()
