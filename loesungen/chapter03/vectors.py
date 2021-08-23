class Vector:

    def __init__(self, values):
        self.values = values

    # Addition
    def __add__(self, other):
        if type(other) != Vector:
            raise TypeError("Can only add vectors to each other!")
        if len(self.values) != len(other.values):
            raise ValueError("Vectors need to have identical dimensions!")
        result_values = []
        for i, value in enumerate(self.values):
            result_values.append(value + other.values[i])
        return Vector(result_values)

    # Subtraktion
    def __sub__(self, other):
        if type(other) != Vector:
            raise TypeError("Can only subtract vectors from each other!")
        if len(self.values) != len(other.values):
            raise ValueError("Vectors need to have identical dimensions!")
        result_values = []
        for i, value in enumerate(self.values):
            result_values.append(value - other.values[i])
        return Vector(result_values)

    # Multiplikation
    def __mul__(self, other):
        if type(other) == Vector:
            # Zwei Vektoren: Skalarprodukt
            if len(self.values) != len(other.values):
                raise ValueError("Vectors need to have identical dimensions!")
            result = 0
            for i, value in enumerate(self.values):
                result += value * other.values[i]
            return result
        else:
            # Skalarmultiplikation
            result_values = []
            for value in self.values:
                result_values.append(value * other)
            return Vector(result_values)

    # Betrag
    def magnitude(self):
        s = 0
        for value in self.values:
            s += value ** 2
        return s ** (1 / 2)

    # String-Darstellung
    def __str__(self):
        return f"({' '.join(str(value) for value in self.values)})"


if __name__ == '__main__':
    v1 = Vector([1, -2, 3])
    v2 = Vector([-2, 4, -6])
    print(f"Addition: {v1} + {v2} = {v1 + v2}")    
    print(f"Subtraktion: {v1} - {v2} = {v1 - v2}")
    print(f"Skalarprodukt: {v1} * {v2} = {v1 * v2}")
    print(f"Skalarmultiplikation: {v1} * 4 = {v1 * 4}")
    print(f"Betrag: |{v1}| = {v1.magnitude()}")
