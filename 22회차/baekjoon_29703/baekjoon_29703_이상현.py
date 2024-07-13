import sys
input = sys.stdin.readline

from collections import deque

def bfs(row, col):
    global min_

    q = deque()
    q.append((row, col, 0))
    visited = [[False] * M for _ in range(N)]
    visited[row][col] = True

    while q:
        row, col, time_ = q.popleft()

        if list_[row][col] == 'F':
            if (row, col) in dict_:
                min_ = min(min_, time_ + dict_[(row, col)])
            else:
                dict_[(row, col)] = time_

        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            if not (0 <= nrow < N and 0 <= ncol < M) or visited[nrow][ncol] or list_[nrow][ncol] == 'D':
                continue

            visited[nrow][ncol] = True
            q.append((nrow, ncol, time_ + 1))

N, M = map(int, input().split())
list_ = [list(input()) for _ in range(N)]
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
min_ = float('inf')
dict_ = {}

for row in range(N):
    for col in range(M):
        if list_[row][col] == 'S':
            bfs(row, col)
            continue

        if list_[row][col] == 'H':
            bfs(row, col)
            continue

print(min_ if min_ != float('inf') else -1)