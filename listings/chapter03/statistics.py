# Minimum
def min(numbers):
    return sorted(numbers)[0]

# Maximum
def max(numbers):
    return sorted(numbers)[-1]

# Arithmetisches Mittel
def mean_arith(numbers):
    return sum(numbers) / len(numbers)

# Geometrisches Mittel
def mean_geom(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product ** (1 / len(numbers))

# Median
def median(numbers):
    sorted_numbers = sorted(numbers)
    m_index = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[m_index - 1] + sorted_numbers[m_index]) / 2
    else:
        return sorted_numbers[m_index]

# Varianz
def variance(numbers):
    n = len(numbers)
    m = mean_arith(numbers)
    s = 0
    for i in numbers:
        s += (i - m) ** 2
    return (1 / (n - 1)) * s

# Standardabweichung
def stdev(numbers):
    return variance(numbers) ** (1 / 2)

if __name__ == '__main__':
    numbers = []
    print("Bitte Zahlen eingeben (Enter für Ende)")
    while True:
        number = input("> ")
        if number == '':
            break
        numbers.append(float(number))
    print(f"Minimum = {min(numbers)}")
    print(f"Maximum = {max(numbers)}")
    print(f"Arithmetisches Mittel = {mean_arith(numbers)}")
    print(f"Geometrisches Mittel = {mean_geom(numbers)}")
    print(f"Median = {median(numbers)}")
    print(f"Varianz = {variance(numbers)}")
    print(f"Standardabweichung = {stdev(numbers)}")
