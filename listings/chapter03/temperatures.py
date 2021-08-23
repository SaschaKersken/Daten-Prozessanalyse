# Je nach Modus passende Konvertierungs-Lambda-Funktion zurückgeben
def converter(mode):
    if mode.upper() == 'C':
        return lambda temp: temp / 5 * 9 + 32
    else:
        return lambda temp: (temp - 32) / 9 * 5

# Modus abfragen und entsprechende Funktion abholen
mode = input("(C)elsius in Fahrenheit oder (F)ahrenheit in Celsius? ")
convert = converter(mode)

# Hauptschleife
while True:
    temp = input("Temperatur (Q für Ende)? ")
    if temp.upper() == 'Q':
        break
    print(convert(float(temp)))

