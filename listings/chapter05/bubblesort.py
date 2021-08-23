def bubblesort(unsorted):
    # Vorerst Endlosschleife
    while True:
        # Bis auf Weiteres gilt die Liste als sortiert
        is_sorted = True
        # Erstes bis vorletztes Element
        for i in range(0, len(unsorted) - 1):
            # Aktuelles Element größer als sein Nachfolger?
            if unsorted[i] > unsorted[i + 1]:
                # Elemente vertauschen
                unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                # Feststellung: Liste ist noch nicht sortiert
                is_sorted = False
        # Falls hier sortiert, Ende
        if is_sorted:
            break

if __name__ == '__main__':
    list1 = [7, 2, 9, 1, 8, 4, 6, 3, 5, 0, 9]
    list2 = ['Katze', 'Hund', 'Elefant', 'Maus', 'Affe', 'Giraffe']
    bubblesort(list1)
    print(list1)
    bubblesort(list2)
    print(list2)
