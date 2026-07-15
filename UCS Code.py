import heapq
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 6)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}
def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = {}
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node == goal:
            return cost, path
        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for neighbor, edge_cost in graph[node]:
                heapq.heappush(
                    priority_queue,
                    (cost + edge_cost, neighbor, path + [neighbor])
                )
    return None
start = input("Enter Source Node: ")
goal = input("Enter Destination Node: ")
result = uniform_cost_search(graph, start, goal)
if result:
    cost, path = result
    print("\nLeast Cost Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")
