import matplotlib.pyplot as plt

plt.xlabel('x')
plt.ylabel('y')
plt.scatter([3, -3, -3, 3], [3, 3, -3, -3])
plt.annotate('A', (3, 3))
plt.annotate('B', (-3, 3))
plt.annotate('C', (-3, -3))
plt.annotate('D', (3, -3))
plt.grid()
plt.axhline(linewidth=2)
plt.axvline(linewidth=2)
plt.show()
