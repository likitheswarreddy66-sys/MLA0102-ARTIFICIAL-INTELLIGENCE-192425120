from collections import deque
def water_jug(cap1, cap2, target):
    queue = deque([((0, 0), [(0, 0)])])
    visited = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if x == target or y == target:
            print("Sequence of States:")
            for state in path:
                print(state)
            return
        next_states = [
            (cap1, y),                    
            (x, cap2),                     
            (0, y),                        
            (x, 0),                       
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            (x + min(y, cap1 - x), y - min(y, cap1 - x))   
        ]
        for state in next_states:
            if state not in visited:
                queue.append((state, path + [state]))
    print("Solution not possible.")
cap1 = int(input("Enter capacity of Jug1: "))
cap2 = int(input("Enter capacity of Jug2: "))
target = int(input("Enter target quantity: "))
water_jug(cap1, cap2, target)
