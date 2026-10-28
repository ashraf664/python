from collections import deque

def stations_4(graph):
    result = {}

    for s in graph:
        q = deque([(s, 0)])
        visited = {s}
        can_reach = set()

        while q:
            u, d = q.popleft()

            if d == 4:
                continue

            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    can_reach.add(v)
                    q.append((v, d + 1))

        result[s] = can_reach

    return result
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'A'],
}


print(stations_4(graph))
 
 
