import sqlite3
import json
from sys import exit

irises = []
# Datei vorhanden?
try:
    json_file = open("iris.json", "r")
except FileNotFoundError:
    print("Datei iris.json nicht gefunden.")
    exit()

# JSON auslesen und umwandeln
try:
    irises = json.load(json_file, object_hook = lambda obj: list(obj.values()))
except json.JSONDecodeError as e:
    print(f"Fehler im JSON-Code: {e}")
    exit()

try:
    db = sqlite3.connect("data.db")
    # Dictionary für die Spezies-Zuordnung
    species = {}
    result = db.execute("SELECT species_name, species_id FROM iris_species")
    for line in result:
        species[line[0]] = line[1]
    # Daten einfügen
    for iris in irises:
        db.execute("""INSERT INTO iris_samples
            (sepal_length, sepal_width, petal_length, petal_width, species)
            VALUES (?, ?, ?, ?, ?)""",
            [iris[0], iris[1], iris[2], iris[3], species[iris[4]]])
    # Änderung permanent machen (Commit)
    db.commit()
    # Wie viele Datensätze wurden eingefügt?
    result = db.execute("SELECT COUNT(*) FROM iris_samples")
    number = result.fetchone()[0]
    print(f"{number} Datensätze eingefügt.")
except sqlite3.Error as e:
    print(f"Datenbankfehler: {e}")
    exit()
