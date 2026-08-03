N=12

board=[-1]*N


def safe(row,col):

    for i in range(row):

        if board[i]==col:
            return False

        if abs(board[i]-col)==abs(i-row):
            return False

    return True


def solve(row):

    if row==N:
        return True

    for col in range(N):

        if safe(row,col):

            board[row]=col

            if solve(row+1):
                return True

    return False


solve(0)


print("12 Queens Solution")

for r in range(N):

    line=""

    for c in range(N):

        if board[r]==c:
            line+=" Q "
        else:
            line+=" . "

    print(line)