from collections import deque


cap1=11
cap2=9
goal=8


def water_jug():

    queue=deque([(0,0,[])])

    visited=set()


    while queue:

        a,b,path=queue.popleft()


        if (a,b) in visited:
            continue

        visited.add((a,b))


        if a==goal or b==goal:
            return path+[(a,b)]


        states=[

        (cap1,b,"Fill 11L"),
        (a,cap2,"Fill 9L"),
        (0,b,"Empty 11L"),
        (a,0,"Empty 9L"),

        ]


        pour=min(a,cap2-b)
        states.append((a-pour,b+pour,"Pour 11L to 9L"))

        pour=min(b,cap1-a)
        states.append((a+pour,b-pour,"Pour 9L to 11L"))


        for x,y,action in states:

            queue.append((x,y,path+[action]))



solution=water_jug()

for s in solution:
    print(s)