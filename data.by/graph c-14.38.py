class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = {}

    def add_edge(self, u, v, weight=None):
        self.graph[u][v] = weight
        if not self.directed:
            self.graph[v][u] = weight

    def remove_edge(self, u, v):
        if v in self.graph[u]:
            del self.graph[u][v]
        if not self.directed and u in self.graph[v]:
            del self.graph[v][u]
G = Graph(directed=False)
G.add_vertex('A')
G.add_vertex('B')
G.add_vertex('C')

G.add_edge('A', 'B', 10)
G.add_edge('A', 'C', 5)

print(G.graph)

G.remove_edge('A', 'B')

print(G.graph)
