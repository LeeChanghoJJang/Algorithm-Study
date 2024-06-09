def solution(board, aloc, bloc):
    global r, c
    r, c = len(board) - 1, len(board[0]) - 1
    answer = A_move(board, aloc, bloc, 0)
    return answer[1]


def A_move(board, a, b, turn):
    dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x, y = a
    if not board[x][y]:
        return (0, turn)

    flag = False
    win_t = []
    lose_t = []

    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= r and 0 <= ny <= c and board[nx][ny]:
            board[x][y] = 0

            win, t = B_move(board, [nx, ny], b, turn + 1)
            if not win:
                win_t.append(t)
            else:
                lose_t.append(t)

            board[x][y] = 1
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
    x, y = b
    if not board[x][y]:
        return (0, turn)

    flag = False
    win_t = []
    lose_t = []
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= r and 0 <= ny <= c and board[nx][ny]:
            board[x][y] = 0

            win, t = A_move(board, a, [nx, ny], turn + 1)
            if not win:
                win_t.append(t)
            else:
                lose_t.append(t)

            board[x][y] = 1
            flag = True

    if flag:
        if win_t:
            return (1, min(win_t))
        else:
            return (0, max(lose_t))
    else:
        return (0, turn)


board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]
print(solution(board, aloc, bloc))
