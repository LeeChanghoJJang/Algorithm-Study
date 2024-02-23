# 10026 : 적록색약
import sys
from collections import deque 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# BFS를 통해 델타탐색. 
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
            # 조건 : 1. 방문하지 않았으며, 2.색깔이 같은 곳만 한번에 탐색한다. 
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and district[nx][ny]==color:
                visited[nx][ny]=1
                queue.append([nx,ny])
# N은 행과 열 숫자. district는 RGB로 색칠한 그림, cnt는 구역 구분할 수 있는 숫자 
N = int(sys.stdin.readline())
district = [sys.stdin.readline().strip() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
# 두가지 경우로 나누어 진행 (색약이 없는 경우와 색약이 있는 경우)
# 방문하지 않은 곳은 BFS로 탐색하여 같은 곳은 전부 방문처리한 후, 카운팅
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
print(cnt,end=' ')
# 색약 있는 경우 재탐색을 위해 visited와 cnt 초기화 
visited = [[0] * N for _ in range(N)]
cnt = 0
# 색약이 있는 경우 R과 G의 구분이 안되므로, R과 G를 통일
for i in range(N):
    district[i] = district[i].replace('R','G')
# 앞의 절차와 똑같이 탐색 
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
print(cnt)
