import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(N):
    line = input().strip()
    s = line.find('S')
    h = line.find('H')
    if s != -1:
        start = (i, s)
    if h != -1:
        home = (i, h)
    arr.append(list(line))

dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(v, t):
    que = deque([v])
    visited = [[0] * M for _ in range(N)]
    visited[v[0]][v[1]] = 1
    while que:
        x, y = que.popleft()
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != 'D' and not visited[nx][ny]:
                    if arr[nx][ny] == 'F':
                        dp[t][nx][ny] = visited[x][y]
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

dp = [[[0] * M for _ in range(N)] for _ in range(2)]

bfs(start, 0)
bfs(home, 1)

result = 1e9

for i in range(N):
    for j in range(M):
        if dp[0][i][j] != 0 and dp[1][i][j] != 0:
            result = min(result, dp[0][i][j] + dp[1][i][j])

print(result if result!= 1e9 else -1)