board=[
' ',' ',' ',
' ',' ',' ',
' ',' ',' '
]


def show():

    print(board[0:3])
    print(board[3:6])
    print(board[6:9])


def check():

    win=[
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8)
    ]

    for a,b,c in win:

        if board[a]==board[b]==board[c]!=' ':
            return board[a]

    return None



while True:

    show()

    pos=int(input("Enter position 0-8: "))

    board[pos]='X'


    if check():
        print("You Win")
        break


    for i in range(9):

        if board[i]==' ':
            board[i]='O'
            break


    if check():
        show()
        print("AI Wins")
        break