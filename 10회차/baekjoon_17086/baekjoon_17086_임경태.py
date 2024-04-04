# 17086 아기 상어

from collections import deque

def BFS(sea, i, j):
    dist = [[0] * M for _ in range(N)]
    Q = deque([[i, j]])
    while Q:
        i, j = Q.popleft()
        for di, dj in go:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not dist[ni][nj]:
                dist[ni][nj] = dist[i][j] + 1
                if sea[ni][nj]: return dist[ni][nj]
                Q.append([ni, nj])

go = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if not sea[i][j]:
            ans = max(ans, BFS(sea, i, j))
print(ans)