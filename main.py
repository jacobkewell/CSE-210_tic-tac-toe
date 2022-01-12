"""
Name: CSE 210 Tic-Tac-Toe Game
Author: Jacob Ewell
"""

# create a main function to run the tic-tac-toe game
def main():
    current_player = "x"
    board = make_board()
    while not (winner(board) or draw(board)):
        print_board(board)
        board = user_move(current_player, board)
        current_player = next_turn(current_player)
    print_board(board)
    print(f'Good Game! Thanks for Playing!')    

# creates the intital tic-tac-toe board
def make_board():
    board = []
    for space in range(9):
        board.append(space + 1)
    return board

# prints out the tic-tac-toe board
def print_board(board):
    print('')
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print("-+-+-")
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print("-+-+-")
    print(f'{board[6]}|{board[7]}|{board[8]}')
    print('')

# switches it to the next player, either x or o
def next_turn(player):
    if player == 'x':
        return 'o'
    else:
        return 'x'

# test all possible ways of winning tic-tac-toe and returns True if there is a winner
def winner(board):
    if board[0] == board[1] and board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True    
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    else:
        return False

# tests to see if all of the tic-tac-toe spaces have been filled with an x or an o
def draw(board):
    for i in range(9):
        if board[i] != 'x' and board[i] != 'o':
            return False
    else:
        return True

# requests input from the players as to which move they would like to do and updates the board
def user_move(player, board):
    move = int(input(f"{player}'s turn to chose a square (1-9): "))
    board[move - 1] = player
    return board

if __name__ == "__main__":
    main()