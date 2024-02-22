import sys
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def BFS(x,y):
    global cnt
    queue = deque([[x,y]])
    color = district[x][y]
    cnt+=1
    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and district[nx][ny]==color:
                visited[nx][ny]=1
                queue.append([nx,ny])

N = int(sys.stdin.readline())
district = [sys.stdin.readline().strip() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
print(cnt,end=' ')
visited = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    district[i] = district[i].replace('R','G')
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
print(cnt)