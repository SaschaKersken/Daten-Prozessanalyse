import csv

# Sniffer-Instanz erzeugen
sniffer = csv.Sniffer()
# Schleife über die zu prüfenden Dateien
csv_filename = 'iris-semicolon.csv'
print(csv_filename)
with open(csv_filename, 'r', newline = '') as csv_file:
    # Die ersten 1024 Byte der Datei lesen
    chunk = csv_file.read(1024)
    # Prüfen, ob die Datei einen Hedaer hat
    header = sniffer.has_header(chunk)
    print(f"- Header: {header}")
    # CSV-Konfiguration (Dialect) ermitteln
    dialect = sniffer.sniff(chunk)
    # Beispielhaft das ermittelte Trennzeichen ausgeben
    print(f"- Trennzeichen: {repr(dialect.delimiter)}")
    # Wichtig: Datei "zurückspulen"
    csv_file.seek(0)
    # Reader mit dem ermittelten Dialect initialisieren
    reader = csv.reader(csv_file, dialect)
    # Falls Header vorhanden, überspringen (oder wegspeichern)
    if header:
        header_data = next(reader, None)
        print("- Spaltentitel:", header_data)
    iris_data = list(reader)
    print(f"{len(iris_data)} Datensätze importiert.")
    print(iris_data[0])
    print(iris_data[50])
    print(iris_data[100])
