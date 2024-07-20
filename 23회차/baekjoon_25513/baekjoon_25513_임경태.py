# 25513 빠른 오름차순 숫자 탐색
from collections import deque

def bfs(r, c):
    Q = deque([[r, c, 0, 0]])
    visit[r][c][0] = 1

    while Q:
        i, j, idx, cnt = Q.popleft()

        if idx == 6:
            return cnt

        for dir in range(4):
            ni, nj = i+di[dir], j+dj[dir]

            if not (0<=ni<5 and 0<=nj<5 and board[i][j] != -1 and not visit[ni][nj][idx]):
                continue

            visit[ni][nj][idx] = 1

            if board[ni][nj] == idx+1:
                idx += 1

            Q.append([ni, nj, idx, cnt+1])

    return -1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
visit = [[[0] * 7 for _ in range(5)] for _ in range(5)]
print(bfs(r, c))