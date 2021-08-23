import math
from node_search import get_path, dfs, bfs, a_star

sample_maze = """+++++++++
+S      +
+ +++++ +
+       +
+ ++ ++ +
+       +
+ +++++ +
+      G+
+++++++++"""

def input_maze():
    print("""Geben Sie das Labyrinth zeilenweise ein; mit leerer Zeile beenden.
Verwenden Sie + für Wände, Leerzeichen für offene Stellen,
S für das Startfeld und G für das Zielfeld.""")
    maze = ""
    while True:
        line = input()
        if line == "":
            break
        maze += line + "\n"
    return maze

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

def find_successors(maze, line, column):
    successors = []
    if line < len(maze) - 1:
        if maze[line + 1][column] != '+':
            successors.append((line + 1, column))
    if line > 0:
        if maze[line - 1][column] != '+':
            successors.append((line - 1, column))
    if column < len(maze[0]) - 1:
        if maze[line][column + 1] != '+':
            successors.append((line, column + 1))
    if column > 0:
        if maze[line][column - 1] != '+':
            successors.append((line, column - 1))
    return successors

def print_maze(maze, start_location, goal_location, path = None):
    if path:
        for location in path:
            if location != start_location and location != goal_location:
                maze[location[0]][location[1]] = "X"
    for line in maze:
        print("".join(line))
    if path:
        for location in path:
            if location != start_location and location != goal_location:
                maze[location[0]][location[1]] = " "

print("Möchten Sie (1) ein eigenes Labyrinth erstellen, oder (2) das Beispiel verwenden?")
decision = input("> ")
if decision == "1":
    maze, start_location, goal_location = parse_maze(input_maze())
else:
    maze, start_location, goal_location = parse_maze(sample_maze)
    print_maze(maze, start_location, goal_location)

goal = dfs(
    start_location,
    lambda location: location == goal_location,
    lambda location: find_successors(maze, location[0], location[1])
)
print()
print("Tiefensuche:")
if (goal):
    print_maze(maze, start_location, goal_location, get_path(goal))
else:
    print("Keine Lösung gefunden.")
goal = bfs(
    start_location,
    lambda location: location == goal_location,
    lambda location: find_successors(maze, location[0], location[1])
)
print()
print("Breadth-first search:")
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
