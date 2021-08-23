from csp import CSP

AGE = 0
HOUSE_COLOR = 1
HOUSE_NUMBER = 2

ages = [36, 37, 39, 42]
house_colors = ["rot", "grün", "blau", "gelb"]
house_numbers = [2, 4, 6, 8]
domain_template = []
for age in ages:
    for house_color in house_colors:
        for house_number in house_numbers:
            domain_template.append([age, house_color, house_number])
house_variables = ["Anna", "Filiz", "Hector", "Klaus"]
house_domains = {}
for variable in house_variables:
    house_domains[variable] = domain_template

def find(assignment, feature, value):
    for person in assignment:
        if assignment[person][feature] == value:
            return person
    return None

def house_constraint(assignment):
    # Zugeordnete Werte dürfen nicht identisch sein
    if len(assignment) > 1:
        for feature in [AGE, HOUSE_COLOR, HOUSE_NUMBER]:
            feature_list = []
            for person in assignment:
                feature_list.append(assignment[person][feature])
            if len(feature_list) != len(set(feature_list)):
                return False
    # Die jüngste Person wohnt im gelben Haus?
    youngest = find(assignment, AGE, 36)
    yellow = find(assignment, HOUSE_COLOR, "gelb")
    if youngest and yellow and youngest != yellow:
        return False
    # Klaus ist kein Nachbar von Hector?
    if "Klaus" in assignment and "Hector" in assignment:
        if abs(assignment["Klaus"][HOUSE_NUMBER] - assignment["Hector"][HOUSE_NUMBER]) == 2:
            return False
    # Das grüne Haus steht nicht neben dem gelben?
    green = find(assignment, HOUSE_COLOR, "green")
    if green and yellow:
        if abs(assignment[yellow][HOUSE_NUMBER] - assignment[green][HOUSE_NUMBER]) == 2:
            return False
    # Hector wohnt nicht in einem der äußeren Häuser?
    if "Hector" in assignment:
        hector = assignment["Hector"]
        if hector[HOUSE_NUMBER] == 2 or hector[HOUSE_NUMBER] == 8:
            return False
    # Die Person im grünen Haus ist 42 Jahre alt?
    if green:
        age42 = find(assignment, AGE, 42)
        if age42 and green != age42:
            return False
    # Anna wohnt nicht im roten Haus?
    if "Anna" in assignment:
        if assignment["Anna"][HOUSE_COLOR] == "rot":
            return False
    # Filiz ist nicht 39 Jahre alt?
    if "Filiz" in assignment:
        if assignment["Filiz"][AGE] == 39:
            return False
    # Das gelbe Haus steht ganz rechts?
    yellow = find(assignment, HOUSE_COLOR, "gelb")
    if yellow and assignment[yellow][HOUSE_NUMBER] != 8:
        return False
    # Anna oder Klaus wohnt in Hausnummer 4?    
    house4 = find(assignment, HOUSE_NUMBER, 4)
    if house4 and house4 != "Anna" and house4 != "Klaus":
        return False
    # Die 39-jährige Person wohnt ganz links?
    age39 = find(assignment, AGE, 39)
    if age39 and assignment[age39][HOUSE_NUMBER] != 2:
        return False
    # Das rote Haus steht weiter links als das blaue?
    red = find(assignment, HOUSE_COLOR, "rot")
    blue = find(assignment, HOUSE_COLOR, "blue")
    if red and blue and red > blue:
        return False
    # Anna ist älter als Hector, dessen Haus nicht rot ist?
    if "Hector" in assignment:
        if assignment["Hector"][HOUSE_COLOR] == "rot":
            return False
        if "Anna" in assignment and assignment["Anna"][AGE] < assignment["Hector"][AGE]:
            return False
    # Alle Bedingungen erfüllt
    return True

house_csp = CSP(house_variables, house_domains, house_constraint)
solution = house_csp.solve()
if solution:
    for person in sorted(solution.items(), key = lambda item: item[1][HOUSE_NUMBER]):
        #print(f"{person}: {solution[person]}")
        print(person)
else:
    print("Keine Lösung gefunden.")
