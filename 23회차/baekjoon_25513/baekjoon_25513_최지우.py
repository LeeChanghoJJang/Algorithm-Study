import sys
from collections import deque
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]

x, y = map(int, input().split())
dr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y, k):
    que = deque([(x, y, 0)])
    visited = [[0] * 5 for _ in range(5)]
    visited[x][y] = 1

    while que:
        x, y, d = que.popleft()

        if arr[x][y] == k:
            return x, y, d
        
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                if arr[nx][ny] != -1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    que.append((nx, ny, d + 1))
                    
    return -1, -1, -1

total = 0
sx, sy = x, y

for i in range(1, 7):
    nx, ny, d = bfs(sx, sy, i)
    if nx == -1:
        print(-1)
        exit()
        
    total += d
    sx, sy = nx, ny

print(total)
