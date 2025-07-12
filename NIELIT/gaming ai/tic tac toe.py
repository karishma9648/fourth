import random
def evaluate(board):
# Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return 1 if row[0] == 'X' else -1
    return 0  # Draw or unfinished game

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 1 or score == -1:
        return score

    if is_maximizing:
        best = -float('inf')
        for move in get_moves(board):
            new_board = apply_move(board, move, 'X')
            best = max(best, minimax(new_board, depth + 1, False))
        return best
    else:
        best = float('inf')
        for move in get_moves(board):
            new_board = apply_move(board, move, 'O')
            best = min(best, minimax(new_board, depth + 1, True))
        return best

def best_move(board):
    best_value = -float('inf')
    best_move = None
    for move in get_moves(board):
        new_board = apply_move(board, move, 'X')
        move_value = minimax(new_board, 0, False)
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move
