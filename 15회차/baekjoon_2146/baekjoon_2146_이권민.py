# from collections import deque
# def bfs(row,col,search,cnt):
#     global min_n
#     deq = deque([[row,col,search,cnt]])
#     while deq:
#         r,c,travel,counting = deq.popleft()
#         if counting >= min_n:
#             continue
#         if travel and matrix[r][c]:
#             min_n = min(min_n,counting)
#         for i in range(4):
#             lr = dr[i]+r
#             lc = dc[i]+c
#             if 0 <= lr < N and 0 <= lc < N:
                
            
        
    
    
    

# N = int(input())
# matrix = [list(map(int,input().split())) for _ in range(N)]
# visited = [[0]*N for _ in range(N)]
# min_n = 10e10
# dr = [1,0,-1,0]
# dc = [0,1,0,-1]
# for i in range(N):
#     for j in range(N):
#         if matrix[i][j] and not visited[i][j]:
#             visited[i][j] = 1
#             bfs(i,j,False,0)

from collections import deque

# 입력값
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
num = 1
res = int(1e9)

# 1번째 bfs (섬 구분)
def bfs(i,j):
  que = deque()
  que.append([i,j])
  while que:
    x, y = que.popleft()
    for (h, w) in [[1,0],[0,1],[-1,0],[0,-1]]:
      dx, dy = x+h, y+w
      if 0<=dx<n and 0<=dy<n and not visited[dx][dy] and graph[dx][dy]:
        visited[dx][dy] = 1
        graph[dx][dy] = num
        que.append([dx,dy])

        
# 2번째 bfs (최단거리 구하기)
def bfs2(v):
  queue = deque()
  dist = [[-1]*n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if graph[i][j]==v:
        dist[i][j] = 0
        queue.append([i,j])

  while queue:
    x, y = queue.popleft()
    for (w, h) in [[1,0],[0,1],[-1,0],[0,-1]]:
      dx, dy = x+w, y+h
      if 0<=dx<n and 0<=dy<n:
        # 다른 섬 만났다! 연결됨!
        if graph[dx][dy] and graph[dx][dy]!=v:
          return dist[x][y]
        # 물이고 아직 다리 없는 곳
        elif (not graph[dx][dy]) and dist[dx][dy]==-1:
          dist[dx][dy] = dist[x][y]+1
          queue.append([dx,dy])

  return int(1e9)



# 섬 구분
for i in range(n):
  for j in range(n):
    if graph[i][j] and not visited[i][j]:
      visited[i][j] = 1
      graph[i][j] = num
      bfs(i,j)
      num += 1


# 최단거리 구하기
for v in range(1,num):
  res = min(res, bfs2(v))
print(res)