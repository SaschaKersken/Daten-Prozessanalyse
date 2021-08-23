class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # Vorzeichen (Minus)
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    # Addition
    def __add__(self, other):
        if type(other) == int:
            other = Fraction(other * self.denominator, self.denominator)
        if type(other) == Fraction:
            if self.denominator == other.denominator:
                return Fraction(self.numerator + other.numerator,
                    self.denominator)
            print("Identische Nenner für +/- benötigt")
        else:
            print("Falscher Typ")
        return None

    # Subtraktion
    def __sub__(self, other):
        return self + (-other)

    # Multiplikation
    def __mul__(self, other):
        if type(other) == int:
            return Fraction(self.numerator * other, self.denominator)
        if type(other) == Fraction:
            return Fraction(self.numerator * other.numerator,
                self.denominator * other.denominator)
        print("Falscher Typ")
        return None

    # Division
    def __truediv__(self, other):
        if type(other) == int:
            if other == 0:
                print("Division durch Null ist verboten")
                return None
            return Fraction(self.numerator, self.denominator * other)
        if type(other) == Fraction:
            return self * Fraction(other.denominator, other.numerator)
        print("Falscher Typ")
        return None

    # Dezimalwert
    def decimal(self):
        return self.numerator / self.denominator

    # Ausgabe
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# Hauptprogramm
if __name__ == '__main__':
    f1 = Fraction(1, 3)
    f2 = Fraction(3, 4)
    f3 = Fraction(1, 5)
    f4 = Fraction(2, 5)
    print(f"{f1} + 1 = {f1 + 1}")
    print(f"{f2} + 1.0 = {f2 + 1.0}")
    print(f"{f1} + {f2} = {f1 + f2}")
    print(f"{f3} + {f4} = {f3 + f4}")
    print(f"{f1} * {f3} = {f1 * f3}")    
    print(f"{f3} - {f4} = {f3 - f4}")
    print(f"{f1} / {f2} = {f1 / f2}")
    print(f"Dezimalwert von {f3} = {f3.decimal()}")

