import matplotlib.pyplot as plt
import numpy as np
import re
from sys import argv, exit

def func(coefficients, x):
    y = 0
    for exponent in coefficients:
        y += coefficients[exponent] * x ** exponent
    return y

def formula(coefficients):
    result = ''
    for i in sorted(coefficients.keys(), reverse=True):
        if coefficients[i] == 0:
            continue
        if len(result) > 0 and coefficients[i] >= 0:
            result += ' + '
        if abs(coefficients[i]) != 1:
            result += f' {coefficients[i]}'
        elif coefficients[i] == -1:
            result += ' -'
        else:
            result += ' '
        if i > 1:
            result += f'x^{i}'
        elif i == 1:
            result += 'x'
    return 'f(x) = ' + result

# Coefficients and coordinates
coefficients = {}
x_min = -10
x_max = 10

# Parse command line arguments
coefficient_pattern = re.compile("(\d+):(-?\d+(\.\d+)?)$")
coordinates_pattern = re.compile("(-?\d+),(-?\d+)$")
for arg in argv[1:]:
    coefficient_match = coefficient_pattern.match(arg)
    coordinates_match = coordinates_pattern.match(arg)
    if coefficient_match:
        data = coefficient_match.groups()
        coefficients[int(data[0])] = float(data[1])
    elif coordinates_match:
        data = coordinates_match.groups()
        x_min = float(data[0])
        x_max = float(data[1])
        if x_min >= x_max:
            print("Minimum x coordinate must be less than maximum x coordinate")
            exit()
    else:
        print(f"Invalid argument '{arg}'")
        exit()
if len(coefficients.keys()) == 0:
    print(f"No function data found.")
    exit()


x = np.linspace(x_min, x_max, 1000)
y = np.array([func(coefficients, xi) for xi in x])

plt.plot(x,y)
plt.title(formula(coefficients))
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(linewidth=2)
plt.axvline(linewidth=2)
plt.show()
