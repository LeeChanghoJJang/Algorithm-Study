# 7576 토마토

from collections import deque

ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

# 초기 익은 토마토 큐에 추가
Q = deque([[i, j, 0] for i in range(N) for j in range(M) if tomato[i][j] == 1])

# BFS
while Q:
    i, j, d = Q.popleft()

    for di, dj in ds:
        ni, nj = i + di, j + dj

        if 0<=ni<N and 0<=nj<M and tomato[ni][nj] == 0:
            tomato[ni][nj] = 1
            Q.append([ni, nj, d+1])

# 익지 않은 토마토가 있다면 -1 출력 그렇지 않으면 최소 일수 출력
if any(0 in row for row in tomato): print(-1)
else: print(d)