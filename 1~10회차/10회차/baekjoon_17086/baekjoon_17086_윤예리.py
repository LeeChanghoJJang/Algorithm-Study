# 상어를 먼저 q에 다 찾아서 넣어줘야 함
# 상어들이 동시에 움직이므로

from collections import deque

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y]+1
                q.append((nx, ny))

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            q.append((i, j))

bfs()
result = 0
for k in range(n):
    if result < max(arr[k]):
        result = max(arr[k])
print(result-1)