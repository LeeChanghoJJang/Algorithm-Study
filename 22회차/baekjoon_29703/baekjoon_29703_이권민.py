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
    matrix.append(list(input().strip()))  # Strip the newline character from each line
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

min_time = float('inf')

# Calculate the minimum time from each feed to home
for f in feed:
    feed_time = bfs(start, f)
    if feed_time == float('inf'):
        continue  # If there's no valid path from start to this feed, skip it
    
    home_time = bfs(f, home)
    if home_time == float('inf'):
        continue  # If there's no valid path from this feed to home, skip it
    
    min_time = min(min_time, feed_time + home_time)

if min_time == float('inf'):
    print(-1)
else:
    print(min_time)
