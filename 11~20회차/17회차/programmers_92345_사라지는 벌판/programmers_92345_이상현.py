drow, dcol = [0, 0, 1, -1], [1, -1, 0, 0]

def solution(board, aloc, bloc):
    global r, c
    r, c = len(board) - 1, len(board[0]) - 1
    answer = A_move(board, aloc, bloc, 0)
    return answer[1]


def A_move(board, a, b, turn):
    row, col = a
    if not board[row][col]:
        return (0, turn)

    flag = False
    win_t = []
    lose_t = []

    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]
        if 0 <= nrow <= r and 0 <= ncol <= c and board[nrow][ncol]:
            board[row][col] = 0

            win, t = B_move(board, [nrow, ncol], b, turn + 1)
            if not win:
                win_t.append(t)
            else:
                lose_t.append(t)

            board[row][col] = 1
            flag = True

    if flag:
        if win_t:
            return (1, min(win_t))
        else:
            return (0, max(lose_t))
    else:
        return (0, turn)


def B_move(board, a, b, turn):
    dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    row, col = b
    if not board[row][col]:
        return (0, turn)

    flag = False
    win_t = []
    lose_t = []
    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]
        if 0 <= nrow <= r and 0 <= ncol <= c and board[nrow][ncol]:
            board[row][col] = 0

            win, t = A_move(board, a, [nrow, ncol], turn + 1)
            if not win:
                win_t.append(t)
            else:
                lose_t.append(t)

            board[row][col] = 1
            flag = True

    if flag:
        if win_t:
            return (1, min(win_t))
        else:
            return (0, max(lose_t))
    else:
        return (0, turn)