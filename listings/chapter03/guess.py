print("Denk dir eine Zahl zwischen 1 und 100, die ich erraten werde.")
# Anfangs-Ratewert: 50
guess = 50
# Endlosschleife, bis erraten oder Fehler
while True:
    print(f"{guess}. 1) korrekt, 2) zu groß, 3) zu klein, 4) Ende?")
    # Endlosschleife, bis 1-3 eingeben.
    while True:
        choice = input('> ')
        if choice in ['1', '2', '3', '4']:
            break
    if choice == '4':
        break
    if choice == '1':
        print("Hurra!")
        break
    if choice == '2':
        guess -= guess // 2
    else:
        guess += (100 - guess) // 2

