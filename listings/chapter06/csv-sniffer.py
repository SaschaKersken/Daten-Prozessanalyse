import csv

# Sniffer-Instanz erzeugen
sniffer = csv.Sniffer()
# Schleife über die zu prüfenden Dateien
files = ["iris.csv", "iris-tabs.csv"]
for csv_filename in files:
    print(csv_filename)
    csv_file = open(csv_filename, "r")
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
        next(reader, None)
    # Als Test nur die Zeilen zählen
    line_count = 0
    for line in reader:
        line_count += 1
    print(f"- Datensätze: {line_count}")
    csv_file.close()
