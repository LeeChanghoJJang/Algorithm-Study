# 1012 / 유기농 배추 / 실버2

from collections import deque

dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def BFS(i, j):
    Q = deque([[i, j]])
    while Q:
        i, j = Q.popleft()
        for di, dj in dr:
            ni = i + di
            nj = j + dj
            if (0 <= ni < N and 0 <= nj < M) and field[ni][nj]:
                field[ni][nj] = 0
                Q.append([ni, nj])
    field[i][j] = 0

for tc in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    cnt = 0

    # 배추 심기
    for _ in range(K):
        j, i = map(int, input().split())
        field[i][j] = 1

    # 배추흰지렁이 배치
    for i in range(N):
        for j in range(M):
            if field[i][j]:
                BFS(i, j)
                cnt += 1

    print(cnt)

"""
34072KB / 72ms
"""
