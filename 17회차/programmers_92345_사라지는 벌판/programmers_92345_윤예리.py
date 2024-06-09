n = m = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check(x, y):
    return x < 0 or x >= n or y < 0 or y >= m

visited = [[0]*5 for _ in range(5)]
block = [[0]*5 for _ in range(5)]

def game(x1, y1, x2, y2):
    global visited, block

    if visited[x1][y1]:
        return 0

    tmp = 0
    for d in range(4):
        nx = x1 + dx[d]
        ny = y1 + dy[d]
        if check(nx, ny) or visited[nx][ny] or block[nx][ny] == 0:
            continue

        visited[x1][y1] = 1
        value = game(x2, y2, nx, ny) + 1
        visited[x1][y1] = 0

        # 1. 지금 패배, 새 턴 승리
        if tmp % 2 == 0 and value % 2 == 1:
            tmp = value
        # 2. 둘 다 패배 > 최대한 늦게 지기
        elif tmp % 2 == 0 and value % 2 == 0:
            tmp = max(tmp, value)
        # 3. 모두 승리 > 빨리 이기기
        elif tmp % 2 == 1 and value % 2 == 1:
            tmp = min(tmp, value)
    return tmp

def solution(board, aloc, bloc):
    global n, m
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            block[i][j] = board[i][j]

    return game(aloc[0], aloc[1], bloc[0], bloc[1])