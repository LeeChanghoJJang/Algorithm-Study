from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
start = None
feed = []
home = None

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(N):
    matrix.append(list(input())[:M])
    if 'S' in matrix[i]:
        start = (i, matrix[i].index('S'))
    if 'F' in matrix[i]:
        feed.append((i, matrix[i].index('F')))
    if 'H' in matrix[i]:
        home = (i, matrix[i].index('H'))

def bfs(start, target):
    queue = deque([(start[0], start[1], 0)])
    visited = [[False]*M for _ in range(N)]
    visited[start[0]][start[1]] = True
    
    while queue:
        r, c, time = queue.popleft()
        if (r, c) == target:
            return time
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and matrix[nr][nc] != 'D':
                visited[nr][nc] = True
                queue.append((nr, nc, time + 1))
    
    return float('inf')
next = None
feed_time = float('inf')
for f in feed:
    n = bfs(start, f)
    if feed_time > n:
        feed_time = n
        next = f
if next == None:
    print(-1)
    sys.exit(0)
home_time = bfs(next, home)
min_time = feed_time + home_time if feed_time != float('inf') and home_time != float('inf') else -1

print(min_time)
