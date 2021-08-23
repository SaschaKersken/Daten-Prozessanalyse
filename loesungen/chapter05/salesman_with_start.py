from random import randint, shuffle
from copy import deepcopy
from genetic import Chromosome, Genetic
from sys import argv, exit

# Entfernungen auch in Gegenrichtung erzeugen
def generate_distances():
    source_distances = {
        ("Berlin", "Kopenhagen"): 355, ("Berlin", "Warschau"): 517,
        ("Berlin", "Prag"): 280, ("Berlin", "Wien"): 524,
        ("Berlin", "Bern"): 753, ("Berlin", "Paris"): 878,
        ("Berlin", "Luxembourg"): 592, ("Berlin", "Brüssel"): 652,
        ("Berlin", "Amsterdam"): 578, ("Kopenhagen", "Warschau"): 672,
        ("Kopenhagen", "Prag"): 634, ("Kopenhagen", "Wien"): 870,
        ("Kopenhagen", "Bern"): 1033, ("Kopenhagen", "Paris"): 1027,
        ("Kopenhagen", "Luxembourg"): 802, ("Kopenhagen", "Brüssel"): 765,
        ("Kopenhagen", "Amsterdam"): 621, ("Warschau", "Prag"): 517,
        ("Warschau", "Wien"): 556, ("Warschau", "Bern"): 1138,
        ("Warschau", "Paris"): 1367, ("Warschau", "Luxembourg"): 1981,
        ("Warschau", "Brüssel"): 1160, ("Warschau", "Amsterdam"): 1094,
        ("Prag", "Wien"): 253, ("Prag", "Bern"): 621,
        ("Prag", "Paris"): 1031, ("Prag", "Luxembourg"): 597,
        ("Prag", "Brüssel"): 718, ("Prag", "Amsterdam"): 710,
        ("Wien", "Bern"): 684, ("Wien", "Paris"): 1034,
        ("Wien", "Luxembourg"): 764, ("Wien", "Brüssel"): 915,
        ("Wien", "Amsterdam"): 937, ("Bern", "Paris"): 435,
        ("Bern", "Luxembourg"): 312, ("Bern", "Brüssel"): 490,
        ("Bern", "Amsterdam"): 631, ("Paris", "Luxembourg"): 287,
        ("Paris", "Brüssel"): 264, ("Paris", "Amsterdam"): 430,
        ("Luxembourg", "Brüssel"): 187, ("Luxembourg", "Amsterdam"): 319,
        ("Brüssel", "Amsterdam"): 174    
    }    
    distances = {}
    for cities in source_distances:
        distances[cities] = source_distances[cities]
        distances[(cities[1], cities[0])] = source_distances[cities]
    return distances


# Chromosom (Lösungsvorschlag) für das Problem des Handlungsreisenden
class DistanceChromosome(Chromosome):

    CITIES = ["Berlin", "Kopenhagen", "Warschau", "Prag", "Wien", "Bern", "Paris", "Luxembourg", "Brüssel", "Amsterdam"]
    DISTANCES = generate_distances()

    def __init__(self, cities, start = None):
        self.cities = cities
        self.start = start

    # Summe der Entfernungen für die aktuelle Route berechnen
    def get_distance(self):
        sum = 0
        for index, city in enumerate(self.cities):
            if index < len(self.cities) - 1:
                next_city = self.cities[index + 1]
            else:
                next_city = self.cities[0]
            sum += self.DISTANCES[(city, next_city)]
        return sum

    # Fitnessfunktion (Kehrwert der Entfernung, da die Fitness maximiert wird)
    def fitness(self):
        return 1 / self.get_distance() 

    # Eine zufällige Instanz erzeugen und zurückgeben
    @classmethod
    def random_instance(cls, start = None):
        cities_copy = cls.CITIES[:]
        shuffle(cities_copy)
        if start:
            cities_copy.pop(cities_copy.index(start))
            cities_copy = [start] + cities_copy
        return DistanceChromosome(cities_copy, start)

    # Mutation: zwei zufällige Städte tauschen
    def mutate(self):
        min_index = 0
        if self.start:
            min_index = 1
        rand_index_1 = randint(min_index, len(self.cities) - 1)
        rand_index_2 = randint(min_index, len(self.cities) - 1)
        if rand_index_1 != rand_index_2:
            self.cities[rand_index_1], self.cities[rand_index_2] = (
                self.cities[rand_index_2], self.cities[rand_index_1]
            )

    # Crossover: die Position einer Stadt mit der Position
    # dieser Stadt in anderem Chromosom tauschen
    def crossover(self, other):
        child1 = deepcopy(self)
        child2 = deepcopy(other)
        rand_index = randint(0, len(child1.cities) - 1)
        city = child1.cities[rand_index]
        other_index = child2.cities.index(city)
        if rand_index != other_index:
            child1.cities[rand_index], child1.cities[other_index] = (
                child1.cities[other_index], child1.cities[rand_index]
            )
            child2.cities[rand_index], child2.cities[other_index] = (
                child2.cities[other_index], child2.cities[rand_index]
            )
        return [child1, child2]

    # String-Darstellung
    def __str__(self):
        result = " - ".join(self.cities)
        result += " - " + self.cities[0]
        result += ": " + str(self.get_distance())
        return result

if __name__ == '__main__':
    # Startort angegeben?
    start = None
    if len(argv) > 1:
        start = argv[1]
        if start not in DistanceChromosome.CITIES:
            print(f"{start} ist kein gültiger Startort.")
            exit()

    # Anfangspopulation erzeugen
    population = []
    for i in range(0, 100):
        population.append(DistanceChromosome.random_instance(start))
    # Genetischen Algorithmus initialisieren und laufen lassen
    genetic = Genetic(population, 0.0002525252525, 200, 0.7, 0.7)
    best = genetic.run()
    # Die Lösung ausgeben
    print("Beste gefundene Lösung:", best)    
