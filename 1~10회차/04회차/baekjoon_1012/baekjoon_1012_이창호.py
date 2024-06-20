# 1012번 유기농 배추 (34088KB / 72ms)
from collections import deque
T =int(input())
# 인접하는 네방향의 단위벡터 정의 
dx = [0,0,1,-1] 
dy = [1,-1,0,0]

# 인근 배추들을 모두 방문하기 위해 BFS함수 정의
def bfs(a,b):
    que = deque()
    que.append([a,b])
    # 방문 한곳은 다시 방문하지 않기 위해 배추가 없는 것처럼 0처리 
    graph[a][b]=0
    # 주변에 배추가 없을 때까지 탐색
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 범위를 벗어나면 다음 차례로 이동 
            if nx < 0 or nx>= M or ny <0 or ny>=N:
                continue
            # 배추가 있으면 그 방향으로 탐색하기 위해 que에 좌표 추가
            if graph[nx][ny]:
                que.append([nx,ny])
                graph[nx][ny] =0
            
for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*N for _ in range(M)]
    # M * N 행렬 초기화    
    for i in range(K):
        a,b = map(int,input().split())
        graph[a][b]=1
    # 배추가 있는 곳은 1, 없는 곳은 0  
    total_cnt = 0
    for i in range(M):
        for j in range(N):
            # 배추가 있는 곳을 발견하면 BFS로 방문하고, 카운팅 
            if graph[i][j] == 1:
                bfs(i,j)
                total_cnt+=1
    print(total_cnt)
