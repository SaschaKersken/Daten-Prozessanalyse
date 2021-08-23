from sys import argv

numbers = []
for arg in argv[1:]:
    try:
        numbers.append(float(arg))
    except ValueError:
        print(f"{arg} ist keine Zahl.")

if len(numbers) > 0:
    s = sum(numbers)
    m = s / len(numbers)
    print(f"Summe: {s}")
    print(f"Mittelwert: {m}")
else:
    print(f"Verwendung: python3 {argv[0]} zahl [zahl ...]")
