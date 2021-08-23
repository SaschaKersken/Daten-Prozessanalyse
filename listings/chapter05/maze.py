import math
from node_search import get_path, dfs, bfs, a_star

# Das Beispiel-Labyrinth
maze_source = """+++++++++
+S      +
+ +++++ +
+       +
+ ++ ++ +
+       +
+ +++++ +
+      G+
+++++++++"""

# Den String zu einem verschachtelten Array parsen, mit Fehlerbehandlung
def parse_maze(maze_str):
    maze = []
    lines = maze_str.splitlines()
    length = -1
    start_location = ()
    goal_location = ()
    for line_index, line in enumerate(lines):
        if length == -1:
            length = len(line)
        else:
            if length != len(line):
                raise ValueError(f"Alle Zeilen benötigen die Länge {length}.")
        cells = list(line)
        for char_index, char in enumerate(cells):
            if char not in ['+', ' ', 'S', 'G']:
                raise ValueError(f"Ungültiges Zeichen {char}.")
            if char == 'S':
                start_location = (line_index, char_index)
            elif char == 'G':
                goal_location = (line_index, char_index)
        maze.append(cells)
    if ((not start_location) or (not goal_location)):
        raise ValueError("Start und/oder Ziel fehlt.")
    return (maze, start_location, goal_location)

# Nachfolger finden
def find_successors(maze, line, column):
    successors = []
    # Nachfolger unten?
    if line < len(maze) - 1 and maze[line + 1][column] != '+':
        successors.append((line + 1, column))
    # Nachfolger oben?
    if line > 0 and maze[line - 1][column] != '+':
        successors.append((line - 1, column))
    # Nachfolger rechts?
    if column < len(maze[0]) - 1 and maze[line][column + 1] != '+':
        successors.append((line, column + 1))
    # Nachfolger links?
    if column > 0 and maze[line][column - 1] != '+':
        successors.append((line, column - 1))
    return successors

# Das Labyrinth ausgeben, optional mit Pfad
def print_maze(maze, start_location, goal_location, path = None):
    # Wenn Pfad vorhanden, alle Positionen markieren
    if path:
        for location in path:
            if location != start_location and location != goal_location:
                maze[location[0]][location[1]] = "X"
    # Die eigentliche Ausgabe durchführen
    for line in maze:
        print("".join(line))
    # Wenn Pfad vorhanden, Markierung rückgängig machen
    if path:
        for location in path:
            if location != start_location and location != goal_location:
                maze[location[0]][location[1]] = " "

# Labyrinth-String parsen, um Labyrinth, Start- und Zielposition zu erhalten
maze, start_location, goal_location = parse_maze(maze_source)

# Tiefensuche durchführen
goal = dfs(
    start_location,
    lambda location: location == goal_location,
    lambda location: find_successors(maze, location[0], location[1])
)
print()
print("Tiefensuche:")
# Lösung ausgeben, falls vorhanden
if (goal):
    print_maze(maze, start_location, goal_location, get_path(goal))
else:
    print("Keine Lösung gefunden.")

# Breitensuche durchführen
goal = bfs(
    start_location,
    lambda location: location == goal_location,
    lambda location: find_successors(maze, location[0], location[1])
)
print()
print("Breitensuche:")
# Lösung ausgeben, falls vorhanden
if (goal):
    print_maze(maze, start_location, goal_location, get_path(goal))
else:
    print("Keine Lösung gefunden.")

# Euklidischer Abstand als Heuristik
def euclidian_distance(location1, location2):
    rows = location1[0] - location2[0]
    cols = location1[1] - location2[1]
    return math.sqrt(rows ** 2 + cols ** 2)

# A* durchführen
goal = a_star(
    start_location,
    lambda location: location == goal_location,
    lambda location: find_successors(maze, location[0], location[1]),
    lambda location: euclidian_distance(location, goal_location)
) 
print()
print("A*-Suche:")
# Lösung ausgeben, falls vorhanden
if (goal):
    print_maze(maze, start_location, goal_location, get_path(goal))
else:
    print("Keine Lösung gefunden.")

# Manhattan-Abstand als Heuristik
def manhattan_distance(location1, location2):
    rows = abs(location1[0] - location2[0])
    cols = abs(location1[1] - location2[1])
    return rows + cols

# A* durchführen
goal = a_star(
    start_location,
    lambda location: location == goal_location,
    lambda location: find_successors(maze, location[0], location[1]),
    lambda location: manhattan_distance(location, goal_location)
)
print()
print("A*-Suche mit Manhattan-Abstand:")
# Lösung ausgeben, falls vorhanden
if (goal):
    print_maze(maze, start_location, goal_location, get_path(goal))
else:
    print("Keine Lösung gefunden.")
