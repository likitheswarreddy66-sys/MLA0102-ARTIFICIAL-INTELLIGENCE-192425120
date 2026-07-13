graph = {}
n = int(input("Enter number of vertices: "))
for i in range(n):
    vertex = input("Enter vertex: ")
    neighbours = input(f"Enter neighbours of {vertex} separated by space: ").split()
    graph[vertex] = neighbours
start = input("Enter starting vertex: ")
visited = set()
def dfs(node):
    visited.add(node)
    print(node, end=" ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)
print("DFS Traversal:")
dfs(start)
