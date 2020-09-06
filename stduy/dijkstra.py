import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])  # [weight, node]

    while queue:
        current_weight, current_node = heapq.heappop(queue)
        if distances[current_node] < current_weight:
            continue
        for adjacent, weight in graph[current_node].items():
            new_weight = current_weight + weight
            if new_weight < distances[adjacent]:
                distances[adjacent] = new_weight
                heapq.heappush(queue, [new_weight, adjacent])

    return distances


myGraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


print(dijkstra(myGraph, 'A'))
