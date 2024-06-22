def check(board, s):
    # 가로
    for i in range(3):
        if board[i] == [s, s, s]: return True

    # 세로
    for j in range(3):
        tmp = []
        for i in range(3):
            tmp.append(board[i][j])
        if tmp == [s, s, s]: return True

    # 대각선
    if [board[0][0], board[1][1], board[2][2]] == [s, s, s]: return True
    if [board[2][0], board[1][1], board[0][2]] == [s, s, s]: return True

    return False

def solution(board):
    board = [list(i) for i in board]

    o_cnt = x_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O': o_cnt += 1
            elif board[i][j] == 'X': x_cnt += 1

    if not (o_cnt == x_cnt or o_cnt == x_cnt+1): return 0

    # O 가 이기면
    if check(board, 'O'):
        # X 도 이기면 안됨
        if check(board, 'X'): return 0
        # O 턴에서 끝나야 함
        if o_cnt != x_cnt + 1: return 0

    # X 가 이기면 X 턴에서 끝나야 함
    if check(board, 'X') and o_cnt != x_cnt: return 0

    return 1

print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
