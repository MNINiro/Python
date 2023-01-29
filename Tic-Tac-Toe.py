# Tic-Tac-Toe game in Python

# function to display the game board
def display_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("\n")


# function to check if someone won or if it's a draw
def check_game_over(board, player):
    # check rows
    if (board[0] == player and board[1] == player and board[2] == player) or \
            (board[3] == player and board[4] == player and board[5] == player) or \
            (board[6] == player and board[7] == player and board[8] == player):
        return True
    # check columns
    elif (board[0] == player and board[3] == player and board[6] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player):
        return True
    # check diagonals
    elif (board[0] == player and board[4] == player and board[8] == player) or \
            (board[2] == player and board[4] == player and board[6] == player):
        return True
    # check if it's a draw
    elif " " not in board:
        return "draw"
    else:
        return False


# function to check if a player's move is valid
def check_valid_move(board, move):
    return board[move] == " "


# main game loop
board = [" " for x in range(9)]
player = "X"
while True:
    display_board(board)
    print("Player " + player + ", make your move (1-9):")
    move = int(input()) - 1
    if check_valid_move(board, move):
        board[move] = player
        if check_game_over(board, player):
            display_board(board)
            print("Player " + player + " wins!")
            break
        elif check_game_over(board, player) == "draw":
            display_board(board)
            print("It's a draw!")
            break
        else:
            if player == "X":
                player = "O"
            else:
                player = "X"
    else:
        print("Invalid move, please try again.\n")
