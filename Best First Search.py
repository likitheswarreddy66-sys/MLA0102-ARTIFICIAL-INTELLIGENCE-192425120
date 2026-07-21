from queue import PriorityQueue
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}
start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")
pq = PriorityQueue()
visited = set()
pq.put((heuristic[start], start))
print("Best First Search Traversal:")
while not pq.empty():
    h, node = pq.get()
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        if node == goal:
            print("\nGoal Reached!")
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))
