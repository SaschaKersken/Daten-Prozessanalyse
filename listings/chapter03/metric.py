class Metric:

    MILLIMETER = 0.001
    CENTIMETER = 0.01
    METER = 1
    KILOMETER = 1000

    DISPLAY_NAMES = {
        MILLIMETER: 'mm',
        CENTIMETER: 'cm',
        METER: 'm',
        KILOMETER: 'km'
    }

    def __init__(self, value, unit = METER):
        self._value = value
        self._unit = unit
        self._meters = value * unit

    def __str__(self):
        return f"{self.value}{self.DISPLAY_NAMES[self.unit]}"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self._meters = value * unit

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = unit
        self._meters = value * unit

    def __eq__(self, other):
        return self._meters == other._meters

    def __lt__(self, other):
        return self._meters < other._meters

    def __le__(self, other):
        return self._meters <= other._meters

    def __gt__(self, other):
        return self._meters > other._meters

    def __ge__(self, other):
        return self._meters >= other._meters


if __name__ == '__main__':
    length1 = Metric(50)
    length2 = Metric(2, Metric.KILOMETER)
    print(length1)
    print(length2)
    print(Metric(1000) == Metric(1, Metric.KILOMETER))
    print(Metric(999) < Metric(1, Metric.KILOMETER))
