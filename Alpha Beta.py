import math
def alphabeta(depth, nodeIndex, isMax, values, alpha, beta, height):
    if depth == height:
        return values[nodeIndex]
    if isMax:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth + 1,nodeIndex * 2 + i,False,values,alpha,beta,height)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1,nodeIndex * 2 + i,True,values,alpha,beta,height)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
values = [3, 5, 6, 9, 1, 2, 0, -1]
height = int(math.log2(len(values)))
result = alphabeta(0, 0, True, values, -math.inf, math.inf, height)
print("Leaf Nodes:", values)
print("Optimal Value:", result)
