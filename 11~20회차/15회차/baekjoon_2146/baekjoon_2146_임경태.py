# 2146 다리만들기

from collections import deque

go = ((0, 1), (1, 0), (-1, 0), (0, -1))
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
islands = []
ans = 200

def check_island(i, j):
    island = [(i, j)]
    Q = deque([(i, j)])
    board[i][j] = 2

    while Q:
        i, j = Q.popleft()

        for di, dj in go:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 1:
                island.append((ni, nj))
                Q.append((ni, nj))
                board[ni][nj] = 2
    
    return island

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            islands.append(check_island(i, j))

def calc_min_dist(a, b):
    dist = 200
    for ai, aj in islands[a]:
        for bi, bj in islands[b]:
            dist = min(dist, (abs(ai - bi) + abs(aj - bj) - 1))
            if dist == 1: exit(print(1))

    return dist

for i in range(len(islands)):
    for j in range(i+1, len(islands)):
        ans = min(ans, calc_min_dist(i, j))

print(ans)