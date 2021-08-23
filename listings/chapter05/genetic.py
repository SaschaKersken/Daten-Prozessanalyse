from random import choices, random
from heapq import nlargest
from copy import deepcopy

# Elternklasse für Chromosomen
class Chromosome:

    # Eine zufällig generierte Instanz erhalten
    @classmethod
    def random_instance(cls):
        return Chromosome()

    # Wie gut ist die von diesem Chromosom repräsentierte Lösung?
    def fitness(self):
        return 1

    # Mutation: zufällige Veränderung von Eigenschaften
    def mutate(self):
        return self

    # Crossover: zufällig Eigenschaften zweier Chromosomen kombinieren
    def crossover(self, other):
        return [self, other]


# Der genetische Algorithmus
class Genetic:

    def __init__(self, population, expected, max_generations,
            crossover_chance, mutation_chance):
        self.population = population
        self.expected = expected
        self.max_generations = max_generations
        self.crossover_chance = crossover_chance
        self.mutation_chance = mutation_chance

    # Eltern auswählen
    def select_parents(self):
        pool = choices(self.population, k = len(self.population) // 4)
        return nlargest(2, pool, key = lambda chromosome: chromosome.fitness())

    # Fortpflanzungszyklus für eine Generation
    def procreate(self):
        new_population = []
        # Durchführen, bis die neue Generation so groß wie die alte ist
        while len(new_population) < len(self.population):
            # Eltern auswählen
            parents = self.select_parents()
            # Crossover mit gewähler Wahrscheinlichkeit
            if random() < self.crossover_chance:
                [child1, child2] = parents[0].crossover(parents[1])
                new_population.append(child1)
                new_population.append(child2)
            else:
                new_population.append(parents[0])
                new_population.append(parents[1])
        # Gerade/ungerade Anzahl ausgleichen
        if len(new_population) > len(self.population):
            new_population.pop()
        # Mutationen mit gewähler Wahrscheinlichkeit
        for chromosome in new_population:
            if random() < self.mutation_chance:
                chromosome.mutate()
        # Generationsübergang
        self.population = new_population

    # Den Evolutionsprozess durchlaufen
    def run(self):
        # Bestes Chromosom der ersten Generation
        best = deepcopy(
            max(self.population, key = lambda chromosome: chromosome.fitness())
        )
        # Generationenschleife
        for i in range(0, self.max_generations):
            # Bereits optimales Ergebnis? Dann vorzeitig zurückgeben
            if best.fitness() >= self.expected:
                return best
            # Fortpflanzungszyklus
            self.procreate()
            # Bestes Chromosom der neuen Generation
            current_best = deepcopy(
                max(self.population, key = lambda chromosome: chromosome.fitness())
            )
            # Übernehmen, falls besser als bisher bestes Chromosom
            if current_best.fitness() > best.fitness():
                best = current_best
            print(i, best)
        # Bestes gefundenes Chromosom zurückgeben
        return best
