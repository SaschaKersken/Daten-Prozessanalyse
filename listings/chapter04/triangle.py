import matplotlib.pyplot as plt

plt.xlabel('x')
plt.ylabel('y')
plt.scatter([-3, 3, 3], [-3, -3, 3])
plt.annotate('A', (-3, -3))
plt.annotate('B', (3, -3))
plt.annotate('C', (3, 3))
plt.plot([-3, 3], [-3, -3])
plt.plot([3, 3], [-3, 3])
plt.plot([3, -3], [3, -3])
plt.text(0, -3.2, 'c')
plt.text(3.1, 0, 'a')
plt.text(-0.2, 0, 'b')
plt.grid()
plt.axhline(linewidth=2)
plt.axvline(linewidth=2)
plt.show()