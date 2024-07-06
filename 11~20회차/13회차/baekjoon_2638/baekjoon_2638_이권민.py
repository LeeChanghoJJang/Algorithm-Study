from collections import deque
import sys
input=sys.stdin.readline
def BFS(r,c):
    
    visited[r][c] = 1
    deq = deque([[r,c]])
    while deq:
        row,col = deq.popleft()
        for i in range(4):
            lr = dr[i]+row
            lc = dc[i]+col
            if 0 <= lr < N and 0 <= lc < M:
                if visited[lr][lc] == 0 and matrix[lr][lc] == 0:
                    deq.append([lr,lc])
                    visited[lr][lc] = 1
                elif matrix[lr][lc] == 1:
                    visited[lr][lc] = visited[lr][lc] +1
                    
                    
                    
            
# 공기를 돌면서 주변에 치즈있으면 visited+=1. 그후 다시한번 돌면서 
N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
dr = [1,0,-1,0]
dc = [0,1,0,-1]
time = 0
while True:
    visited = [[0]*M for _ in range(N)]
    BFS(0,0)
    time += 1
    
    for i in range(N):
        for j in range(M):
            if visited[i][j]>=2:
                matrix[i][j]= 0
    block_cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                block_cnt += 1
    if block_cnt == N*M:
        break
    
print(time)
    
# import sys
# input=sys.stdin.readline
# from collections import deque

# #공기 탐색
# def air_bfs(i,j):
#     q=deque()
#     q.append([i,j])
#     visited[i][j]=1

#     while q:
#         x,y=q.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if 0<=nx<n and 0<=ny<m:
#             	#다음 진행이 공기면(큐 추가, 방문처리)
#                 if visited[nx][ny]==0 and real_graph[nx][ny]==0:
#                     q.append([nx,ny])
#                     visited[nx][ny]=1
#                 #다음 진행이 치즈면(방문정보 업데이트)
#                 elif real_graph[nx][ny]==1:
#                     visited[nx][ny]=visited[nx][ny]+1

# n, m=map(int, input().split())
# real_graph=[]
# for i in range(n):
#     real_graph.append(list(map(int, input().split())))

# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# time=0

# while 1:
#     visited=[[0 for _ in range(m)] for _ in range(n)]

#     air_bfs(0,0)
#     #탐색 한바퀴 끝나면 시간+1
#     time+=1
	
#     #두면이상 공기랑 닿으면, 빈칸 처리
#     for i in range(n):
#         for j in range(m):
#             if visited[i][j]>=2:
#                 real_graph[i][j]=0

#     # 공기 카운트
#     block_cnt=0
#     for i in range(n):
#         for j in range(m):
#             if real_graph[i][j]==0:
#                 block_cnt+=1
#     #탐색 한번 하고 난 그래프의 공기수가 배열의 크기랑 같으면 break
#     if block_cnt==(n*m):
#         break
    

# print(time)