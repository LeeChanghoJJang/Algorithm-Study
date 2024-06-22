def chk(player, board):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def solution(board):
    num_x = sum(row.count('X') for row in board)
    num_o = sum(row.count('O') for row in board)

    if num_x > num_o or abs(num_x - num_o) > 1:
        return 0

    x_wins = chk('X', board)
    o_wins = chk('O', board)

    if (x_wins and num_x != num_o) or (o_wins and num_x != num_o - 1):
        return 0

    return 1
