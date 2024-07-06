# 2638 치즈

import sys
from collections import deque
sys.stdin = open('input.txt')

go = ((0, 1), (1, 0), (0, -1), (-1, 0))
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
time = 0

def melt():
    will_melt = []
    # 가장자리 제외한 그래프 순회
    for i in range(1, N-1):
        for j in range(1, M-1):
            # 치즈가 아니거나 방문한 곳이라면 패스
            if grid[i][j] != 1: continue
            cnt = 0

            for di, dj in go:
                ni, nj = i + di, j + dj

                # 외부공기와 접촉하면 카운트
                if grid[ni][nj] != 2: continue
                cnt += 1

            # 외부 접촉면이 두면 이상이면 녹음
            if cnt < 2: continue
            will_melt.append([i, j])

    for i, j in will_melt: grid[i][j] = 2

def spread_air():
    visit = [[0] * M for _ in range(N)]
    Q = deque([[0, 0]])

    while Q:
        i, j = Q.popleft()

        for di, dj in go:
            ni, nj = i + di, j + dj

            if (0<=ni<N and 0<=nj<M and
                not visit[ni][nj] and grid[ni][nj] != 1):
                Q.append([ni, nj])
                visit[ni][nj] = 1
                grid[ni][nj] = 2

while True:
    for row in grid:
        if 1 in row: break
    else: exit(print(time))

    spread_air()
    melt()
    time += 1