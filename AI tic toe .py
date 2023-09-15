import math

# Constants for the players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_cells.append((i, j))
    return empty_cells

def minimax(board, depth, maximizing_player):
    if is_winner(board, PLAYER_X):
        return -1
    if is_winner(board, PLAYER_O):
        return 1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_O
            eval = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_X
            eval = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_eval = -math.inf
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = PLAYER_O
        eval = minimax(board, 0, False)
        board[i][j] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
    return best_move

def main():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    print("Tic-Tac-Toe - AI vs. Human")
    print_board(board)

    while True:
        row, col = best_move(board)
        board[row][col] = PLAYER_O
        print("\nAI's move:")
        print_board(board)

        if is_winner(board, PLAYER_O):
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))

        if board[row][col] != EMPTY:
            print("Invalid move. Try again.")
            continue

        board[row][col] = PLAYER_X
        print_board(board)

        if is_winner(board, PLAYER_X):
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()


                    
                                 
                 
