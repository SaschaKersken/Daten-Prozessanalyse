import csv
import sqlite3

# Ein Abfrageergebnis ausgeben
def print_result(result):
    for line in result:
        print(', '.join(map(str, line)))
    print()

# Eine Datenbankoperation jeweils gruppiert
# und insgesamt ausführen
def queries(db, base_sql):
    sql = base_sql + ", rooms FROM rent GROUP BY rooms"
    print("Gruppiert nach Zimmeranzahlen:")
    print_result(db.execute(sql))
    sql = base_sql + " FROM rent"
    print("Insgesamt:")
    print_result(db.execute(sql))
         
# Datenbankverbindung; Datendatei rent.db
db = sqlite3.connect('rent.db')
# Tabelle löschen, falls sie existiert
db.execute("""
DROP TABLE IF EXISTS rent
""")
# Tabelle erstellen
db.execute("""
CREATE TABLE rent (
id INTEGER PRIMARY KEY,
rooms INTEGER,
size INTEGER,
rent INTEGER
)
""")
# Daten importieren/einfügen
with open('size-rent.csv', 'r', newline = '') as rent_file:
    reader = csv.reader(rent_file, quoting = csv.QUOTE_NONNUMERIC)
    next(reader, None)
    data = list(reader)
for line in data:
    db.execute(
        """
        INSERT INTO rent (rooms, size, rent)
        VALUES (?, ?, ?)
        """,
        [line[1], line[0], line[2]]
    )
print("1. Höchste Miete")
print()
queries(db, "SELECT MAX(rent)")
print("2. Niedrigste Miete")
print()
queries(db, "SELECT MIN(rent)")
print("3. Durchschnittsmiete")
print()
queries(db, "SELECT AVG(rent)")
print("4. Anzahl der Wohnungsangebote")
print()
queries(db, "SELECT COUNT(id)")
