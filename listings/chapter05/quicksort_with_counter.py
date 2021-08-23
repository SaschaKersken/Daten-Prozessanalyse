class Quicksorter:
    def __init__(self):
        self.counter = 0

    def quicksort(self, unsorted):
        # Teillisten
        less = []
        equal = []
        greater = []

        if len(unsorted) > 1:
            # Vergleichselement (willkürlich)
            pivot = unsorted[0]
            for element in unsorted:
                self.counter += 1
                if element < pivot:
                    less.append(element)
                elif element > pivot:
                    greater.append(element)
                else:
                    equal.append(element)
            return self.quicksort(less) + equal + self.quicksort(greater)
        return unsorted

if __name__ == '__main__':
    qs1 = Quicksorter()
    qs2 = Quicksorter()
    list1 = [7, 2, 9, 1, 8, 4, 6, 3, 5, 0, 9]
    list2 = ['Katze', 'Hund', 'Elefant', 'Maus', 'Affe', 'Giraffe']
    qs1.quicksort(list1)
    print(list1, qs1.counter)
    qs2.quicksort(list2)
    print(list2, qs2.counter)    
