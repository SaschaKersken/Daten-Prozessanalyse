import time, os, platform
from sys import argv

class Grid:

    def __init__(self, cells = None):
        if cells:
            self.cells = cells
        else:
            self.cells = set()
        self.global_min_x = 0
        self.global_min_y = 0
        self.history = []
        self.period_start = -1
        self.period_length = 0
        self.auto_scroll = False
        self.show_grid = False

    # Lebende Zelle hinzufügen
    def add(self, x, y):
        self.cells.add((x, y))

    # Population aus Liste von Strings parsen
    def parse(self, data):
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char in 'Xx':
                    self.add(x, y)

    # Existiert an Position x, y eine lebende Zelle?
    def cell_at(self, x, y):    
        if (x, y) in self.cells:
            return 1
        return 0

    # Anzahl lebender Nachbarn eines Feldes
    def alive_neighbours(self, x, y):
        return sum([
            self.cell_at(x - 1, y - 1),
            self.cell_at(x, y - 1),
            self.cell_at(x + 1, y - 1),
            self.cell_at(x - 1, y),
            self.cell_at(x + 1, y),
            self.cell_at(x - 1, y + 1),
            self.cell_at(x, y + 1),
            self.cell_at(x + 1, y + 1)
        ])

    # Dimensionen der aktuellen Population
    def dimensions(self):
        min_x = None
        max_x = None
        min_y = None
        max_y = None
        for cell in self.cells:
            x, y = cell
            if min_x is None or min_x > x:
                min_x = x
            if max_x is None or max_x < x:
                max_x = x
            if min_y is None or min_y > y:
                min_y = y
            if max_y is None or max_y < y:
                max_y = y
            if min_x < self.global_min_x:
                self.global_min_x = min_x
            if min_y < self.global_min_y:
                self.global_min_y = min_y
        return {
            'min_x': min_x, 'max_x': max_x, 'min_y': min_y, 'max_y': max_y
        }

    # Generationswechsel
    def tick(self):
        # Falls noch keine Periode, akt. Generation zur History hinzufügen
        if self.period_start == -1:
            self.history.append(self.cells)
        # Nächste Geneation zuerst leer, damit Änderungen einander nicht beeinflussen
        next_generation = set()
        dimensions = self.dimensions()
        # Die bekannten Regeln auf alle betroffenen Felder anwenden
        for y in range(dimensions['min_y'] - 1, dimensions['max_y'] + 2):
            for x in range(dimensions['min_x'] - 1, dimensions['max_x'] + 2):
                if self.cell_at(x, y) == 0:
                    if self.alive_neighbours(x, y) == 3:
                        next_generation.add((x, y))
                else:
                    alive_neighbours = self.alive_neighbours(x, y)
                    if alive_neighbours in (2, 3):
                        next_generation.add((x, y))
        # Generation ersetzen
        self.cells = next_generation
        # Statisch oder periodisch?
        if self.period_start == -1:
            for generation, old_cells in enumerate(self.history):
                if old_cells == self.cells:
                    self.period_start = generation
                    self.period_length = len(self.history) - generation
                    self.history = None # Speicher der History freigeben
        # Die aktuelle Populationsgröße zurückgeben
        return len(self.cells)
            
    def __str__(self):
        # String-Darstellung
        dimensions = self.dimensions()
        result = ""
        if self.auto_scroll:
            # auto_scroll: nur bevölkerten Bereich betrachten
            start_x = dimensions['min_x']
            start_y = dimensions['min_y']
        else:
            # Kein auto_scroll: an kleinster bisheriger Position beginnen
            start_x = self.global_min_x
            start_y = self.global_min_y
        # Ausgabe mit oder ohne Gitternetz (show_grid)
        for y in range(start_y - 1, dimensions['max_y'] + 2):
            line = ''
            for x in range(start_x - 1, dimensions['max_x'] + 2):
                if self.cell_at(x, y):
                    line += '#'
                elif self.show_grid and x % 5 == 0 and y %5 == 0:
                    line += '+'
                elif self.show_grid and x % 5 == 0:
                    line += '|'
                elif self.show_grid and y % 5 == 0:
                    line += '-'
                else:
                    line += ' '
            result += line + "\n"
        return result

    # Formale Darstellung (für Debugging)
    def __repr__(self):
        return str(self.cells)


# Bildschirm löschen (systemabhängig)
def clear():
    if platform.system == 'Windows':
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)


# Anfangspopulation per Eingabe
def input_data():
    data = []
    print("Gitter eingeben (X = lebende Zelle, Q in Zeile = Ende.")
    line = input().lower()
    while 'q' not in line:
        data.append(line)
        line = input()
    return data


# Hauptprogramm
if __name__ == '__main__':
    # Voreinstellungen
    stop_on_period = False
    max_generations = 0
    generation = 0
    sleeper = 1
    grid = Grid()
    # Kommandozeilenargumente verarbeiten
    for arg in argv[1:]:
        print(arg)
        if arg == 'oscillator':
            grid.parse(['XXX'])
        elif arg == 'pentomino':
            grid.parse([' XX', 'XX', ' X'])
            print(len(grid.cells))
        elif arg == 'glider':
            grid.parse([' X', '  X', 'XXX'])
        elif arg == 'pentadecathlon':
            grid.parse(['  X    X', 'XX XXXX XX', '  X    X'])
        elif arg == 'autoscroll':
            grid.auto_scroll = True
        elif arg == 'showgrid':
            grid.show_grid = True
        elif arg == 'stop':
            stop_on_period = True
        elif arg[0] == 'g':
            try:
                max_generations = int(arg[1:])
            except ValueError:
                pass # Irrelevant
        else:
            try:
                sleeper = float(arg)
            except ValueError:
                print(f"Unbekanntes Argument {arg}")
    # Population eingeben, falls nicht als Argument angegeben
    if len(grid.cells) == 0:
        data = input_data()
        grid.parse(data)
        if len(grid.cells) == 0:
            print("No starting pattern.")
            exit()
    again = 1
    max_cells = 0
    # Hauptschleife
    while True:
        clear()
        if again > 0:
            print(grid)
        num_cells = len(grid.cells)
        if num_cells > max_cells:
            max_cells = num_cells
        print(f"Generation: {generation} ({num_cells}, max: {max_cells})")
        if grid.period_start > -1:
            print(f"Periodenbeginn: {grid.period_start}, Periodendauer: {grid.period_length}")
            if stop_on_period:
                exit()
        if again == 0:
            exit()
        if max_generations > 0 and generation >= max_generations:
            exit()
        time.sleep(sleeper)
        previous = grid.cells
        again = grid.tick()
        generation += 1
