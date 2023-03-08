import numpy as np

turn = 0
winner = False
possible_to_insert = 0
rows = 6
columns = 7

def generate_board(rows, columns):
    board = np.zeros((rows, columns), dtype=int)
    return board


def switch_player(turn):
    player = (turn % 2 + 1)
    print(f"Player {player} turn.")
    return turn + 1


def mark_board(possible_to_insert, column):
    current_player = turn % 2 + 1
    board[possible_to_insert][column] = current_player
    print(board)


def make_turn():
    while True:
        try:
            column = int(input(f"Choose column form 1 to {columns}: ")) - 1
            if column >= 0 and column < columns:
                for i in range(rows):
                    if board[rows - 1 - i][column] == 0:
                        possible_to_insert = rows - 1 - i
                        break
                else:
                    raise ValueError("Chosen column is full. Choose another one.")
            else:
                raise ValueError("Chosen column is outside the board. Choose another one.")
        except ValueError as e:
            print(e)
        else:
            break

    mark_board(possible_to_insert, column)


def check_winner(board, player):
    for j in range(columns - 3):
        for i in range(rows):
            if board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player and board[i][j + 3] == player:
                return True

    for j in range(columns):
        for i in range(rows - 3):
            if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][j] == player:
                return True

    for j in range(columns - 3):
        for i in range(rows - 3):
            if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and board[i + 3][j + 3] == player:
                return True

    for j in range(columns - 3):
        for i in range(3, rows):
            if board[i][j] == player and board[i - 1][j + 1] == player and board[i - 2][j + 2] == player and board[i - 3][j + 3] == player:
                return True

    return False


board = generate_board(rows, columns)
print(board)

while not winner:
    if turn > rows * columns:
        break
    turn = switch_player(turn)
    make_turn()
    winner = check_winner(board, turn % 2 + 1)

if winner:
    winner_number = turn % 2 + 1
    print(f"Player {winner_number} wins.")
else:
    print("Draw")
