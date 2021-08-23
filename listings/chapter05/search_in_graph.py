from graph import Graph
from node_search import get_path, dfs, bfs

graph = Graph()
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
graph.add_edge('C', 'E')
graph.add_edge('D', 'E')

a_to_c_1 = dfs(
    'A',
    lambda vertex: vertex == 'C',
    lambda vertex: graph.neighbors(vertex)
)
print("Von A nach C mit Tiefensuche:")
print(get_path(a_to_c_1))
a_to_c_2 = bfs(
    'A',
    lambda vertex: vertex == 'C',
    lambda vertex: graph.neighbors(vertex)
)
print("Von A nach C mit Breitensuche:")
print(get_path(a_to_c_2))
