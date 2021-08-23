def quicksort(unsorted):
    # Teillisten
    less = []
    equal = []
    greater = []

    # Mehr als ein Element in der aktuellen Teilliste
    if len(unsorted) > 1:
        # Vergleichselement (willkürlich)
        pivot = unsorted[0]
        for element in unsorted:
            if element < pivot:
                # Kleinere Elemente in eigene Liste
                less.append(element)
            elif element > pivot:
                # Größere Elememte in eigene Liste
                greater.append(element)
            else:
                # Gleiche Elemente in eigene Liste
                equal.append(element)
        # Teillisten sortieren und Gesamtliste zusammenstellen
        return quicksort(less) + equal + quicksort(greater)
    # Falls nur ein Element, einfach die Teilliste zurückgeben
    return unsorted

if __name__ == '__main__':
    list1 = [7, 2, 9, 1, 8, 4, 6, 3, 5, 0, 9]
    list2 = ['Katze', 'Hund', 'Elefant', 'Maus', 'Affe', 'Giraffe']
    quicksort(list1)
    print(list1)
    quicksort(list2)
    print(list2)    
