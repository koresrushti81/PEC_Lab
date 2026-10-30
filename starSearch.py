import heapq

def a_star(graph, start, goal, h):
 
    pq = [(h[start], 0, start, [start])]

    visited = set()

    while pq:

        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:

            if neighbour not in visited:

                new_g = g + cost
                new_f = new_g + h[neighbour]

                new_path = path + [neighbour]

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbour, new_path)
                )

    print("No path found")
 
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}
 
h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

a_star(graph, 'A', 'D', h)