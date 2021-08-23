class Graph:

    def __init__(self):
        self.vertices = []
        self.edges = []

    # Knoten hinzufügen
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)

    # Kante hinzufügen
    def add_edge(self, vertex_from, vertex_to):
        # Knoten hinzufügen, falls noch nicht vorhanden
        self.add_vertex(vertex_from)
        self.add_vertex(vertex_to)
        # Kanten in beide Richtungen, falls noch nicht vorhanden
        if (vertex_from, vertex_to) not in self.edges:
            self.edges.append((vertex_from, vertex_to))
        if (vertex_to, vertex_from) not in self.edges:
            self.edges.append((vertex_to, vertex_from))

    # Alle von einem Knoten ausgehenden Kanten ermitteln
    def edges_from_vertex(self, vertex):
        result = []
        if vertex in self.vertices:
            result = list(
                filter(
                    lambda edge: edge[0] == vertex,
                    self.edges
                )
            )
        return result

    # Alle direkt mit einem Knoten verbundenen Nachbarn ermitteln
    def neighbors(self, vertex):
        result = []
        for edge in self.edges_from_vertex(vertex):
            result.append(edge[1])
        return result

    # Kante entfernen
    def remove_edge(self, edge):
        # In beide Richtungen
        if edge in self.edges:
            self.edges.remove(edge)
        reverse = (edge[1], edge[0])
        if reverse in self.edges:
            self.edges.remove(reverse)

    # Knoten (und alle mit ihm verbundenen Kanten) entfernen
    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            removable_edges = self.edges_from_vertex(vertex)
            for edge in removable_edges:
                self.remove_edge(edge)
            self.vertices.remove(vertex)

    # String-Darstellung
    def __str__(self):
        result = ""
        for vertex in self.vertices:
            result += f"{vertex}: {self.neighbors(vertex)}\n"
        return result

if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'D')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('D', 'E')
    print(graph)
    print("Von A ausgehende Kanten:")
    print(graph.edges_from_vertex('A'))
    print("Nachbarknoten von A:")
    print(graph.neighbors('A'))
    print("Entferne Knoten D")
    graph.remove_vertex('D')
    print(graph)
    print("Von A ausgehende Kanten:")
    print(graph.edges_from_vertex('A'))
    print("Nachbarknoten von A:")
    print(graph.neighbors('A'))
