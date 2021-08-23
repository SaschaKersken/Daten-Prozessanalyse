def is_fever_celsius(t):
    return t >= 38

def is_fever_fahrenheit(t):
    return t >= 100.4

def fever_tester(scale):
    if scale.upper() == 'C':
        return is_fever_celsius
    else:
        return is_fever_fahrenheit

# Temperaturskala erfragen
config = input("Temperaturen in (C)elsius oder (F)ahrenheit? ")

# Konkrete Funktion für Fiebertest je nach Konfiguration
is_fever = fever_tester(config)

# Schleife für Tests
while True:
    temp = input('Körpertemperatur (0 für Ende)? ')
    if temp == '0':
        break
    fever = is_fever(float(temp))
    if fever:
        print("Fieber!")
    else:
        print("Kein Fieber.")

