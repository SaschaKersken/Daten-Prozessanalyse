from csp import CSP

# Bedingung: Alle Personen brauchen einen gemeinsamen Termin
def meeting_constraint(assignment):
    return len(set(assignment.values())) == 1

# Variablen = Personen, die Termine brauchen
variables = ["Alfred", "Birte", "Cem", "Dana"]
# Domänen = Uhrzeiten, zu denen die Personen Zeit haben
domains = {
    "Alfred": ["9 Uhr", "14 Uhr", "15 Uhr"],
    "Birte": ["9 Uhr", "14 Uhr"],
    "Cem": ["14 Uhr", "15 Uhr", "17 Uhr"],
    "Dana": ["9 Uhr", "11 Uhr", "14 Uhr"]
}
# CSP-Instanz erstellen und Lösungsmethode aufrufen
meeting_csp = CSP(variables, domains, meeting_constraint)
result = meeting_csp.solve()
if result:
    print(f"Das Meeting findet um {result['Alfred']} statt.")
else:
    print("Kein Zeitpunkt für ein gemeinsames Meeting gefunden.")
