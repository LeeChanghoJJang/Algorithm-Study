# 1012번 유기농 배추
from collections import deque
T =int(input())
# 인접하는 네방향의 단위벡터 정의 
dx = [0,0,1,-1] 
dy = [1,-1,0,0]

# 인근 배추들을 모두 방문하기 위해 BFS함수 정의
def bfs(a,b):
    que = deque()
    que.append([a,b])
    graph[a][b]=0
    
    while que:
        x,y = que.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or nx>= M or ny <0 or ny>=N:
                continue
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
            # 배추가 있는 곳을 기준으로, 너비 우선 탐색 실시
            if graph[i][j] == 1:
                bfs(i,j)
                total_cnt+=1
    print(total_cnt)
'''코드리뷰
bfs 코드 구현을 위해 사이트를 참조하여 풀었음.
완벽히 bfs 코드 구현 후, 재도전 필요
'''