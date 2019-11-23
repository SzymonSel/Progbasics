board = [['.','.','.'],
         ['X','O','X'],
         ['.','.','.']]

def print_board(my_board):
    for i in range(len(my_board)):
        for j in range(len(my_board)):
            temp = my_board[i][j] 
            print(temp, end="")
        print()

print_board(board)  