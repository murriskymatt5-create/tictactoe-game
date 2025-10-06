# TIC-TAC-TOE BOARD SETUP

# 1. Create a list to represent the 3x3 grid, initialized with numbers 1-9.
board = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9'
]

# 2. Function to display the board format
def display_board(board):
    print('\n')
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]}')
    print('\n')
