class Graph:
    def __init__(self, directed=False):
        self._outgoing = {}
        self._directed = directed
        if directed:
            self._incoming = {}
        else:
            self._incoming = self._outgoing

    def insert_vertex(self, v):
        if v not in self._outgoing:
            self._outgoing[v] = {}
            if self._directed:
                self._incoming[v] = {}

    def insert_edge(self, u, v, weight=None):
        self._outgoing[u][v] = weight
        self._incoming[v][u] = weight

    def remove_vertex(self, v):

        for u in list(self._incoming[v].keys()):
            del self._outgoing[u][v]

        for w in list(self._outgoing[v].keys()):
            del self._incoming[w][v]

        del self._outgoing[v]
        if self._directed:
            del self._incoming[v]
G = Graph(directed=True)
G.insert_vertex('A')
G.insert_vertex('B')
G.insert_vertex('C')

G.insert_edge('A','B')

G.insert_edge('B','C')

G.insert_edge('A','C')

print(G._outgoing)

G.remove_vertex('A')

print(G._outgoing)

