def binary_search(search_space, search_object):
    # Vorerst Endlosschleife
    while True:
        # Index des mittleren Elements (unter der Mitte bei gerader Anzahl)
        center = len(search_space) // 2
        # Aktuelles Element
        current = search_space[center]
        print(f"Suchraum: {search_space}, mittl. Element: {current} (Index {center})")
        # Gefunden?
        if current == search_object:
            return True
        # Kleiner als aktuelles Element, und gibt es noch kleinere?
        if search_object < current and center > 0:
            # Anfang bis ausschließlich Mitte ist neuer Suchraum
            search_space = search_space[0:center]
        # Größer als aktuelles Element, und gibt es noch größere?
        elif search_object > current and center < len(search_space) - 1:
            # Mitte + 1 bis Ende ist neuer Suchraum
            search_space = search_space[center + 1:]
        else:
            # Alles durchsucht, nichts gefunden
            return False

if __name__ == '__main__':
    list1 = [3, 7, 9, 13, 24, 37, 42, 49, 53]
    list2 = [3, 7, 9, 13, 24, 37, 42, 49, 53, 60]
    search_objects = [3, 53, 9, 49, 60, 61, 46]
    for search_object in search_objects:
        print(f"{search_object} in {list1}? {binary_search(list1, search_object)}")
        print(f"{search_object} in {list2}? {binary_search(list2, search_object)}")
