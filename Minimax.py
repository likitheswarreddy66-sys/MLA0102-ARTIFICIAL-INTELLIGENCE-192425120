import math
def minimax(depth, nodeIndex, isMax, values, height):
    if depth == height:
        return values[nodeIndex]
    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )
values = [3, 5, 6, 9, 1, 2, 0, -1]
height = int(math.log2(len(values)))
print("Leaf Nodes:", values)
print("Optimal Value:", minimax(0, 0, True, values, height))
