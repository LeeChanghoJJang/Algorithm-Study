# 1600 말이 되고픈 원숭이
from collections import deque

K = int(input())
W, H = map(int, input().split())
grid = [input().split() for _ in range(H)]
dist = [[[0] * W for _ in range(H)] for _ in range(K+1)]
dist[0][0][0] = 1

dp = ((1, 0), (0, 1), (-1, 0), (0, -1))
dk = ((1, 2), (2, 1), (-2, 1), (-1, 2), (1, -2), (2, -1), (-1, -2), (-2, -1))
Q = deque([[0, 0, 0]])

# BFS
while Q:
    cnt, i, j = Q.popleft()
    
    # 도착점에 도달했을 경우
    if i == H-1 and j == W-1:
        exit(print(dist[cnt][i][j] - 1))

    # 기본 이동
    for di, dj in dp:
        ni, nj = i + di, j + dj

        if 0<=ni<H and 0<=nj<W and grid[ni][nj] != '1' and not dist[cnt][ni][nj]:
            dist[cnt][ni][nj] = dist[cnt][i][j] + 1
            Q.append([cnt, ni, nj])

    # 나이트 이동 가능 여부 확인
    if cnt == K: continue

    # 나이트 이동
    for di, dj in dk:
        ni, nj = i + di, j + dj

        if 0<=ni<H and 0<=nj<W and grid[ni][nj] != '1' and not dist[cnt+1][ni][nj]:
            dist[cnt+1][ni][nj] = dist[cnt][i][j] + 1
            Q.append([cnt+1, ni, nj])

print(-1)