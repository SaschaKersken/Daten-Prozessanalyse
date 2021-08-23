import matplotlib.pyplot as plt
import numpy as np
import csv

theta0 = -469.29515105
theta1 = np.linspace(0, 32, 1000)
# Daten importieren
filename = 'size-rent-4.csv'
data = []
with open(filename, 'r') as data_file:
    reader = csv.reader(data_file)
    for line in reader:
        data.append([float(line[0]), float(line[1])])
x = np.array([row[0] for row in data])
y = np.array([row[1] for row in data])
n = len(data)

j = []
for h_theta1 in theta1:
    j.append(1 / (2 * n) * sum(theta0 + h_theta1 * x - y) ** 2)

plt.plot(theta1, j)
plt.xlabel('θ1')
plt.ylabel('J(θ)')
plt.grid()
plt.axhline(linewidth=2)
plt.axvline(linewidth=2)
plt.show()
