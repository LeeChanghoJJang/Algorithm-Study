import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
from copy import deepcopy

dx = [-1, 0, 1]
dy = [0, -1, 0]

def check(c):
    board = deepcopy(arr)
    visited = [[0] * m for _ in range(n)]
    cnt = 0

    for i in range(n-1, -1, -1):
        die = []
        for v in c:
            q = deque()
            q.append([i, v, 1])

            while q:
                y, x, z = q.popleft()
                if board[y][x]:
                    die.append([y, x])
                    if not visited[y][x]:
                        visited[y][x] = 1
                        cnt += 1
                    break

                if z < d:
                    for k in range(3):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < m and 0 <= ny < n:
                            q.append([ny, nx, z+1])

        for y, x in die:
            board[y][x] = 0

    return cnt


n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

for comb in combinations([i for i in range(m)], 3):
    result = max(result, check(comb))
print(result)