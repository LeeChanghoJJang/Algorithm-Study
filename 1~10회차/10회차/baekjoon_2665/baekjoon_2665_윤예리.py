from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    
    while q:
        x, y = q.popleft()
        
        # 도착!
        if x == n-1 and y == n-1:
            return visited[x][y]
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                # 하얀 방
                if arr[nx][ny]:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                # 까만 방이면 벽 뚫음
                # visited에 벽 뚫은 횟수 저장
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().strip())))
print(bfs())