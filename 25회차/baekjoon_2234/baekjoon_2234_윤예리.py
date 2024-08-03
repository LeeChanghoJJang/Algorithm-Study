import sys
# input = sys.stdin.readline
from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(n)]

def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = 1
    room = 1

    while q:
        x, y = q.popleft()
        wall = 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if ((s[x][y] & wall) != wall):
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    room += 1
                    visited[nx][ny]= 1
                    q.append([nx, ny])

            wall *= 2

    return room

cntRoom = maxRoom = delRoom = 0

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            cntRoom += 1
            maxRoom = max(maxRoom, bfs(i, j))

for i in range(m):
    for j in range(n):
        num = 1
        while num < 9:
            if num & s[i][j]:
                visited = [[0] * n for _ in range(m)]
                s[i][j] -= num
                delRoom = max(delRoom, bfs(i, j))
                s[i][j] += num
            num *= 2

print(cntRoom)
print(maxRoom)
print(delRoom)


