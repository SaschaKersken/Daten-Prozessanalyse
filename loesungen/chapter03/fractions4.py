class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ZeroDivisionError("Nenner darf nicht 0 sein!")

    # Vorzeichen (Minus)
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    # Addition
    def __add__(self, other):
        if type(other) == int:
            other = Fraction(other * self.denominator, self.denominator)
        if type(other) == Fraction:
            if self.denominator == other.denominator:
                return Fraction(self.numerator + other.numerator, self.denominator)
            lcm = self.least_common_multiple(self.denominator, other.denominator)
            e_self = self.expand(lcm // self.denominator)
            e_other = other.expand(lcm // other.denominator)
            return Fraction(e_self.numerator + e_other.numerator, lcm)
        raise TypeError("Falscher Typ")

    # Subtraktion
    def __sub__(self, other):
        return self + (-other)

    # Multiplikation
    def __mul__(self, other):
        if type(other) == int:
            return Fraction(self.numerator * other, self.denominator)
        if type(other) == Fraction:
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        raise TypeError("Falscher Typ")

    # Division
    def __truediv__(self, other):
        if type(other) == int:
            if other == 0:
                raise ZeroDivisionError("Division durch Null ist verboten")
            return Fraction(self.numerator, self.denominator * other)
        if type(other) == Fraction:
            return self * Fraction(other.denominator, other.numerator)
        raise TypeError("Falscher Typ")

    # Vergleichsoperationen
    def __eq__(self, other):
        if type(other) == Fraction:
            return self.decimal() == other.decimal()
        return self.decimal() == other

    def __lt__(self, other):
        if type(other) == Fraction:
            return self.decimal() < other.decimal()
        return self.decimal() < other

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        if type(other) == Fraction:
            return self.decimal() > other.decimal()
        return self.decimal() > other

    def __ge__(self, other):
        return self == other or self > other

    # Größter gemeinsamer Teiler (fürs maximale Kürzen)
    # Euklidscher Algorithmus
    def greatest_common_divider(self, number1, number2):
        while number2 != 0:
            (number1, number2) = (number2, number1 % number2)
        return number1

    # Kleinstes gemeinsames Vielfaches (für Addition/Subtraktion)
    def least_common_multiple(self, number1, number2):
        return abs(number1 * number2) // self.greatest_common_divider(number1, number2)

    # Kürzen
    def shorten(self, factor = None):
        if factor == None:
            factor = self.greatest_common_divider(self.numerator, self.denominator)
        return Fraction(self.numerator // factor, self.denominator // factor)

    # Erweitern
    def expand(self, factor):
        return Fraction(self.numerator * factor, self.denominator * factor)

    # Dezimalwert
    def decimal(self):
        return self.numerator / self.denominator

    # Ausgabe
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# Operatoren und zugehörige Operationen als Lambda-Funktionen
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b,
    '<': lambda a, b: a < b,
    '<=': lambda a, b: a <= b,
    '>': lambda a, b: a > b,
    '>=': lambda a, b: a >= b
}

# Hilfsfunktionen
def get_operand(operand):
    components = operand.split('/')
    numerator = int(components[0])
    if len(components) > 1:
        denominator = int(components[1])
    else:
        denominator = 1
    return Fraction(numerator, denominator)

def get_operator(operator):
    if operator in operations:
        return operator
    raise ValueError("Ungültiger Operator!")

# Hauptprogramm
if __name__ == '__main__':
    # Hauptschleife
    while True:
        try:
            operand1 = get_operand(input("1. Operand (Zahl oder Zähler/Nenner): "))
            operand2 = get_operand(input("2. Operand (Zahl oder Zähler/Nenner): "))
            operator = get_operator(input("Operator (+, -, *, /, ==, !=, <, <=, >, >=): "))
            operation = operations[operator]
            result = operation(operand1, operand2)
            shortened = None
            if type(result) == Fraction:
                shortened = result.shorten()
            shortened_output = f" = {shortened}" if shortened else ''
            print(f"{operand1} {operator} {operand2} = {operation(operand1, operand2)}{shortened_output}")
        except (ZeroDivisionError, TypeError, ValueError) as err:
            print(f"Fehler: {err}")
        again = input("Noch eine Berechnung (j/n)? ")
        if again.upper() == 'N':
            break

