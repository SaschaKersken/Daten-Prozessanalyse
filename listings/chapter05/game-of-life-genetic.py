from random import random, randint
from genetic import Chromosome, Genetic
from game_of_life import Grid

# Chromosom (mögliche Anfangspopulation) für Game of Life
class GoLChromosome(Chromosome):

    def __init__(self, start):
        self.start = start
        self.score = -1
        self.string = None

    # Zufällige Instanz
    @classmethod
    def random_instance(cls):
        pattern = set()
        while len(pattern) == 0:
            for x in range(0, 4):
                for y in range(0, 4):
                    if random() < 0.3:
                        pattern.add((x, y))
        return GoLChromosome(pattern)

    # Fitness: höchste Population in bis zu 100 Ticks
    def fitness(self):
        if self.score == -1:
            grid = Grid(self.start)
            current = 0
            for i in range(0, 100):
                if len(grid.cells) == 0:
                    break
                current = grid.tick()
                if current > self.score:
                    self.score = current
                if current == 0 or grid.period_start >= 0:
                    break
        return self.score

    # Mutation: 2 bis 8 Felder ein-/ausschalten
    def mutate(self):
        for i in range(0, randint(2, 8)):
            x = randint(0, 3)
            y = randint(0, 3)
            if random() < 0.5:
                if (x, y) in self.start:
                    self.start.remove((x, y))
            else:
                if (x, y) not in self.start:
                    self.start.add((x, y))
        # Reset
        self.string = None
        self.score = -1
        self.fitness()

    # Crossover: 2 bis 8 Felder zweier Chromosomen vertauschen
    def crossover(self, other):
        child1 = set(self.start)
        child2 = set(other.start)
        for i in range(0, randint(2, 8)):
            x = randint(0, 3)
            y = randint(0, 3)
            if (x, y) in child1 and (x, y) not in child2:
                child1.remove((x, y))
            elif (x, y) not in child1 and (x, y) in child2:
                child1.add((x, y))
            if (x, y) in child2 and (x, y) not in child1:
                child2.remove((x, y))
            elif (x, y) not in child2 and (x, y) in child1:
                child2.add((x, y))
        return [GoLChromosome(child1), GoLChromosome(child2)]

    # String-Darstellung
    def __str__(self):
        if self.string is None:
            grid = Grid(self.start)
            self.string = str(grid)
        return self.string + str(self.fitness())


if __name__ == '__main__':
    # Anfangspopulation erzeugen
    population = []
    for i in range(0, 100):
        population.append(GoLChromosome.random_instance())
    # Genetischen Algorithmus initialisieren und laufen lassen
    genetic = Genetic(population, 1000, 30, 0.7, 0.5)
    best = genetic.run()
    # Die Lösung ausgeben
    print("Beste gefundene Lösung:")
    print(best)
