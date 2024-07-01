import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append((nx, ny))

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
q = deque([])

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))

bfs()
result = 0
for i in range(n):
    for j in range(m):
        if not tomato[i][j]:
            # print(tomato)
            exit(print(-1))
        else:
            if result < tomato[i][j]:
                result = tomato[i][j]

print(result-1)
# print(tomato)


