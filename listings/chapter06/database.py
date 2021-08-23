import sqlite3
import json

# Ein Abfrageergebnis ausgeben
def print_result(result):
    for line in result:
        print(', '.join(map(str, line)))
    print()

# Datenbankverbindung, Datendatei data.db
db = sqlite3.connect("data_test.db")

# Eventuell vorhandene Tabellen löschen
db.execute("""
DROP TABLE IF EXISTS iris_species
""")
db.execute("""
DROP TABLE IF EXISTS iris_samples
""")

# Tabellen erstellen
db.execute("""
CREATE TABLE iris_species (
    species_id INTEGER PRIMARY KEY,
    species_name TEXT
)
""")
db.execute("""
CREATE TABLE iris_samples (
    sepal_length REAL,
    sepal_width REAL,
    petal_length REAL,
    petal_width REAL,
    species INTEGER
)
""")
result = db.execute("""
SELECT name FROM sqlite_master WHERE type='table'
""")
print("Erzeugte Tabellen:")
print_result(result)

# Daten einfügen
iris_species = ["Iris-setosa", "Iris-virginica", "Iris-versicolor"]
for species in iris_species:
    db.execute("""
        INSERT INTO iris_species (species_name)
        VALUES (?)""",
        [species]
    )
irises = []
# JSON importieren und einfügen
with open('iris.json', 'r', newline='') as json_file:
    irises = json.load(json_file,
        object_hook = lambda obj: list(obj.values())
    )
# Dictionary für die Spezies-Zuordnung
species = {}
result = db.execute("SELECT species_name, species_id FROM iris_species")
for line in result:
    species[line[0]] = line[1]
# Daten einfügen
for iris in irises:
    db.execute("""
        INSERT INTO iris_samples
        (sepal_length, sepal_width, petal_length, petal_width, species)
        VALUES (?, ?, ?, ?, ?)""",
        [iris[0], iris[1], iris[2], iris[3], species[iris[4]]])
print("Eingefügte Daten:")
result = db.execute("""
SELECT species_id, species_name
  FROM iris_species
""")
print_result(result)
result = db.execute("""
SELECT COUNT(*) FROM iris_samples
""")
number = result.fetchone()[0]
print(f"{number} Datensätze importiert und eingefügt.")
print()
print("Die ersten 5:")
result = db.execute("""
SELECT sepal_length, sepal_width, petal_length, petal_width, species_name
  FROM iris_samples
 INNER JOIN iris_species ON species_id = species
 LIMIT 5
""")
print_result(result)
