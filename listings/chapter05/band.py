from sys import exit
from csp import CSP

"""Bonus:
Lösung des Logikrätsels "Die Band" von Jonas Sandrock
https://www.logisch-gedacht.de/logikraetsel/band/
"""

# Konstanten zum einfachen Zugriff auf die 4 Elemente der Tupel
AGE = 0
INSTRUMENT = 1
POSITION = 2
PANTS_COLOR = 3

# Die möglichen Einzelwerte der Domänen
ages = [27, 29, 32, 33, 35]
instruments = ["Bass", "Gitarre", "Keyboard", "Schlagzeug", "Violine"]
positions = [1, 2, 3, 4, 5]
pants_colors = ["blau", "gelb", "grün", "pink", "rot"]
# Alle Kombinationsmöglichkeiten generieren
domain_template = []
for age in ages:
    for instrument in instruments:
        for position in positions:
            for pants_color in pants_colors:
                domain_template.append((age, instrument, position, pants_color))

# Die Variablen sind die Namen der Bandmitglieder
band_variables = ["Harald", "Lara", "Olivia", "Sara", "Udo"]
# Die Domäne für jede Variable sind alle Kombinationsmöglichkeiten
band_domains = {}
for variable in band_variables:
    band_domains[variable] = domain_template
# Hilfsfunktion, um ein Mitglied der Zuordnung anhand eines Merkmals zu finden
def find_member(assignment, feature, value):
    for member in assignment:
        if assignment[member][feature] == value:
            return member
    return None

# Bedingungen
def band_constraints(assignment):
    # Vorbedingung: keine Doppelbelegungen
    if len(assignment) > 1:
        for feature in [AGE, INSTRUMENT, POSITION, PANTS_COLOR]:
            feature_list = []
            for member in assignment:
                feature_list.append(assignment[member][feature])
            if len(feature_list) != len(set(feature_list)):
                return False
    # 1. Das zweite Bandmitglied von rechts spielt Violine?
    member4 = find_member(assignment, POSITION, 4)
    if member4 and assignment[member4][INSTRUMENT] != "Violine":
        return False
    # 2. Der/die Bassist(in) hat eine rote Hose an?
    bass = find_member(assignment, INSTRUMENT, "Bass")
    if bass and assignment[bass][PANTS_COLOR] != "rot":
        return False
    # 3. Der/die Träger(in) der grünen Hose ist 29 Jahre alt und
    # befindet sich zwei Plätze weiter links als der/die Keyboarder(in)?
    green = find_member(assignment, PANTS_COLOR, "grün")
    if green:
        if assignment[green][AGE] != 29:
            return False
        keyboard = find_member(assignment, INSTRUMENT, "Keyboard")
        if keyboard and assignment[green][POSITION] != assignment[keyboard][POSITION] - 2:
            return False
    # 4. Udo befindet sich auf dem Platz links außen?
    if "Udo" in assignment and assignment["Udo"][POSITION] != 1:
        return False
    # 5. Der/die Schlagzeuger(in) sitzt direkt links neben Lara?
    drums = find_member(assignment, INSTRUMENT, "Schlagzeug")
    if drums and "Lara" in assignment and assignment[drums][POSITION] != assignment["Lara"][POSITION] - 1:
        return False
    # 6. Der/die Gitarrist(in) steht auf einem der äußeren Plätze?
    guitar = find_member(assignment, INSTRUMENT, "Gitarre")
    if guitar and assignment[guitar][POSITION] != 1 and assignment[guitar][POSITION] != 5:
        return False
    # 7. Die älteste Person befindet sich direkt rechts neben der Person, die die gelbe Hose an hat?
    oldest = find_member(assignment, AGE, 35)
    yellow = find_member(assignment, PANTS_COLOR, "gelb")
    if oldest and yellow and assignment[oldest][POSITION] != assignment[yellow][POSITION] + 1:
        return False
    # 8. Lara hat eine blaue Hose an?
    if "Lara" in assignment and assignment["Lara"][PANTS_COLOR] != "blau":
        return False
    # 9. Die Person mit der pinken Hose befindet sich weiter rechts als Olivia?
    pink = find_member(assignment, PANTS_COLOR, "pink")
    if pink and "Olivia" in assignment and assignment[pink][POSITION] <= assignment["Olivia"][POSITION]:
        return False
    # 10. Harald, der 32 Jahre alt ist, hat keine rote Hose an?
    if "Harald" in assignment:
        if assignment["Harald"][AGE] != 32 or assignment["Harald"][PANTS_COLOR] == "rot":
            return False
    # 11. Der/die Gitarrist(in) steht weiter links als die Person, die die blaue Hose an hat?
    guitar = find_member(assignment, INSTRUMENT, "Gitarre")
    blue = find_member(assignment, PANTS_COLOR, "blau")
    if guitar and blue and assignment[guitar][POSITION] > assignment[blue][POSITION]:
        return False
    # 12. Die zweite Person von links ist jünger als 30 Jahre?
    member2 = find_member(assignment, POSITION, 2)
    if member2 and assignment[member2][AGE] >= 30:
        return False
    # Alle Bedingungen der aktuellen Zuordnung erfüllt
    return True

# CSP konstruieren und lösen
band_csp = CSP(band_variables, band_domains, band_constraints)
solution = band_csp.solve()
if solution:
    # Lösung nach Position auf der Bühne ausgeben
    for position in positions:
        member = find_member(solution, POSITION, position)
        print(member, solution[member])
else:
    print("Unlösbar.")
