def bubblesort(unsorted):
    counter = 0
    # Vorerst Endlosschleife
    while True:
        # Bis auf Weiteres gilt die Liste als sortiert
        is_sorted = True
        # Erstes bis vorletztes Element
        for i in range(0, len(unsorted) - 1):
            counter += 1
            # Aktuelles Element größer als sein Nachfolger?
            if unsorted[i] > unsorted[i + 1]:
                # Elemente vertauschen
                unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                # Feststellung: Liste ist noch nicht sortiert
                is_sorted = False
        # Falls hier sortiert, Ende
        if is_sorted:
            break
    return counter

if __name__ == '__main__':
    list1 = [7, 2, 9, 1, 8, 4, 6, 3, 5, 0, 9]
    list2 = ['Katze', 'Hund', 'Elefant', 'Maus', 'Affe', 'Giraffe']
    list3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    s1 = bubblesort(list1)
    print(f"{list1}: {s1} Durchläufe")
    s2 = bubblesort(list2)
    print(f"{list2}: {s2} Durchläufe")
    s3 = bubblesort(list3)
    print(f"{list3}: {s3} Durchläufe")
