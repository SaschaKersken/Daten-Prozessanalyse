class CSP:

    def __init__(self, variables, domains, constraint_function):
        self.variables = variables
        self.domains = domains
        self.constraint_function = constraint_function

    def solve(self, assignment = {}):
        # Wenn alle Variablen zugeordnet sind, ist das die Lösung
        if len(assignment) == len(self.variables):
            return assignment
        # Noch nicht zugeordnete Variablen
        unassigned = [var for var in self.variables if var not in assignment]
        # Domänenwerte für erste nicht zugordnete Variable durchprobieren
        test_var = unassigned[0]
        for value in self.domains[test_var]:
            test_assignment = assignment.copy()
            test_assignment[test_var] = value
            # Bedingungen prüfen
            if self.constraint_function(test_assignment):
                # Erfüllt? Dann Rekursion
                result = self.solve(test_assignment)
                # Falls Ergebnis, zurückgeben - sonst Backtracking
                if result is not None:
                    return result
        # Keine Lösung gefunden
        return None


if __name__ == '__main__':
    # Bedingung: Jede Person braucht einen eigenen Termin
    def appointment_constraint(assignment):
        return len(assignment.values()) == len(set(assignment.values()))

    # Variablen = Personen, die Termine brauchen
    variables = ["Alfred", "Birte", "Cem", "Dana"]
    # Domänen = Uhrzeiten, zu denen die Personen Zeit haben
    domains = {
        "Alfred": ["9 Uhr", "15 Uhr"],
        "Birte": ["9 Uhr", "14 Uhr"],
        "Cem": ["14 Uhr", "15 Uhr", "17 Uhr"],
        "Dana": ["9 Uhr", "11 Uhr", "17 Uhr"]
    }
    # CSP-Instanz erstellen und Lösungsmethode aufrufen
    appointment_csp = CSP(variables, domains, appointment_constraint)
    print(appointment_csp.solve())    
