from itertools import permutations

# Brute-Force-Ansatz für das Problem des Handlungsreisenden

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

def get_distance(route, distances):
    sum = 0
    for index, city in enumerate(route):
        if index < len(route) - 1:
            next_city = route[index + 1]
        else:
            next_city = route[0]
        sum += distances[(city, next_city)]
    return sum

cities = ["Berlin", "Kopenhagen", "Warschau", "Prag", "Wien", "Bern", "Paris", "Luxembourg", "Brüssel", "Amsterdam"]
distances = generate_distances()

all_routes = permutations(cities)
shortest = 100000
result = []
round = 0
for route in all_routes:
    round += 1
    if round % 10000 == 0:
        print(round)
    current_distance = get_distance(route, distances)
    if current_distance < shortest:
        shortest = current_distance
        result = route

print(result, shortest)
