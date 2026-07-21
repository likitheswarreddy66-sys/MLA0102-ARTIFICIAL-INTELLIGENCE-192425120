import heapq
graph = {
    'A': [('B',1), ('C',1)],
    'B': [('D',1), ('E',1)],
    'C': [('F',1)],
    'D': [],
    'E': [('G',1)],
    'F': [],
    'G': []
}
heuristic = {
    'A':6,
    'B':4,
    'C':5,
    'D':3,
    'E':2,
    'F':4,
    'G':0
}
start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")
visited = set()
heap = []
heapq.heappush(heap, (heuristic[start], start))
print("Greedy Best First Search:")
while heap:
    h, node = heapq.heappop(heap)
    if node in visited:
        continue
    visited.add(node)
    print(node, end=" ")
    if node == goal:
        print("\nGoal Reached!")
        break
    for neighbor, cost in graph[node]:
        if neighbor not in visited:
            heapq.heappush(heap, (heuristic[neighbor], neighbor))
