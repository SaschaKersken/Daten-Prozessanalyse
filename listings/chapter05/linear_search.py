def linear_search(search_space, search_object, func = None, find_all = False):
    # Zähler zuerst auf 0 setzen
    counter = 0
    # Schleife über jedes Element mit Index
    for index, element in enumerate(search_space):
        # Ist das aktuelle Element das gesuchte Objekt?
        if search_object == element:
            # Zähler um 1 erhöhen
            counter += 1
            # Verarbeitungsfunktion (falls vorhanden) mit Index der Fundstelle aufrufen
            if func is not None:
                func(index)
            # Falls nur ein Vorkommen gesucht, True zurückgeben
            if not find_all:
                return True
    # Falls nur ein Vorkommen gesucht, False zurückgeben
    if not find_all:
        return False
    # Ansonsten Zähler zurückgeben
    return counter

# Konkrete Verarbeitungsfunktion, die nur den Index der Fundstelle ausgibt
def print_index(index):
    print(index)

# Hauptprogramm zum Test aller Anwendungsfälle
if __name__ == '__main__':
    search_space = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Existiert das Element?")
    print("7?")
    print(linear_search(search_space, 7))
    print("11?")
    print(linear_search(search_space, 11))
    print("Wie oft kommt das Element vor?")
    print("7?")
    print(linear_search(search_space, 7, find_all = True))
    print("10?")
    print(linear_search(search_space, 10, find_all = True))
    print("11?")
    print(linear_search(search_space, 11, find_all = True))
    print("Erstes Vorkommen von 7 bei Index?")
    linear_search(search_space, 7, func = print_index)
    print("Erstes Vorkommen von 11 (kommt nicht vor!) bei Index?")
    print(linear_search(search_space, 11, func = print_index))
    print("Alle Vorkommen von 7?")
    linear_search(search_space, 7, func = print_index, find_all = True)
