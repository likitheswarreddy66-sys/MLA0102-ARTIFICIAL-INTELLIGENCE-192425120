import heapq
goal=(1,2,3,
      4,5,6,
      7,8,0)
start=(1,2,3,
       4,0,6,
       7,5,8)
def heuristic(state):
    count=0
    for i in range(9):
        if state[i]!=0 and state[i]!=goal[i]:
            count+=1
    return count
def solve():
    pq=[]
    heapq.heappush(
        pq,(0,start,[])
    )
    visited=set()
    while pq:
        cost,state,path=heapq.heappop(pq)
        if state==goal:
            return path+[state]
        if state in visited:
            continue
        visited.add(state)
        zero=state.index(0)
        moves=[-1,1,-3,3]
        for m in moves:
            new=zero+m
            if 0<=new<9:
                s=list(state)
                s[zero],s[new]=s[new],s[zero]
                s=tuple(s)
                heapq.heappush(
                    pq,
                    (cost+1+heuristic(s),
                     s,
                     path+[state])
                )
solution=solve()
for s in solution:
    print(s)
