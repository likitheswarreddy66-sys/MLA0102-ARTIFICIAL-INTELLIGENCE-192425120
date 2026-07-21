import heapq
graph = {
    'A': [('B',1), ('C',3)],
    'B': [('D',3), ('E',1)],
    'C': [('F',5)],
    'D': [('G',2)],
    'E': [('G',4)],
    'F': [('G',1)],
    'G': []
}
heuristic = {
    'A':7,
    'B':6,
    'C':2,
    'D':1,
    'E':2,
    'F':1,
    'G':0
}
start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")
pq = []
heapq.heappush(pq, (heuristic[start], 0, start))
cost = {start: 0}
parent = {start: None}
while pq:
    f, g, node = heapq.heappop(pq)
    if node == goal:
        break
    for neighbor, weight in graph[node]:
        new_cost = g + weight
        if neighbor not in cost or new_cost < cost[neighbor]:
            cost[neighbor] = new_cost
            priority = new_cost + heuristic[neighbor]
            heapq.heappush(pq, (priority, new_cost, neighbor))
            parent[neighbor] = node
path = []
current = goal
while current:
    path.append(current)
    current = parent[current]
path.reverse()
print("Optimal Path:", " -> ".join(path))
print("Total Cost:", cost[goal])
