import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
 
h = {
    'A': 10,
    'B': 6,
    'C': 4,
    'D': 8,
    'E': 5,
    'F': 2,
    'G': 0
}

def best_first_search(start):
    visited = set()
    pq = []
 
    heapq.heappush(pq, (h[start], start))

    while pq:
        heuristic, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor))

print("Best First Search")
best_first_search('A')