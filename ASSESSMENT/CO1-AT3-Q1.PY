from collections import deque

maze = [
['S',' ','#',' '],
['#',' ',' ',' '],
[' ',' ','#',' '],
[' ','#',' ','G']
]

rows=len(maze)
cols=len(maze[0])

moves=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs():

    queue=deque()
    queue.append((0,0,[]))

    visited=set()

    while queue:

        x,y,path=queue.popleft()

        if (x,y) in visited:
            continue

        visited.add((x,y))

        path=path+[(x,y)]

        if maze[x][y]=='G':
            return path

        for dx,dy in moves:

            nx=x+dx
            ny=y+dy

            if 0<=nx<rows and 0<=ny<cols:
                if maze[nx][ny]!='#':
                    queue.append((nx,ny,path))

path=bfs()

print("Shortest Path:")
print(path)

print("Number of Steps:",len(path)-1)