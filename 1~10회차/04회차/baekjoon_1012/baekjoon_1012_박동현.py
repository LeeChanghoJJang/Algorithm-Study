from collections import deque
import sys

dx = [0,1,0,-1]
dy = [1,0,-1,0]

t = int(input())

for _ in range(t):
    M,N,K = map(int, sys.stdin.readline().strip().split()) # M : 가로 길이, N : 세로 길이, K : 배추 개수
    farm = [[0 for _ in range(M)] for _ in range(N)] # 배추 농장
    baechu_lst = []
    for _ in range(K):
        baechu = list(map(int, sys.stdin.readline().strip().split()))
        n,m = baechu
        # n,m = map(int, sys.stdin.readline().strip().split())
        farm[m][n] = 1
        baechu_lst.append(baechu)
    
    result = 0                          
    # for i in range(N):                  # 2차원 리스트에 대한 전역 bfs 탐색       34088kb / 88ms
    #     for j in range(M):
        # start = [i,j]
    for j,i in baechu_lst:                # 입력 받은 배추 위치를 기반으로 한 bfs 탐색     34072kb / 80ms
        if farm[i][j] == 1:         # 해당 if 조건이 참일 시 bfs가 작동하므로 맨 아래줄에 result 값 + 1
            q = deque()
            q.append((i,j))


            while q :
                ti, tj = q.popleft()     # 배추 위치를 기반으로 하며, DFS 형식으로 pop() 시행시 34072kb / 96ms

                for dlt in range(4) :
                    di = ti + dx[dlt]
                    dj = tj + dy[dlt]
                    if 0<= di < N and 0<= dj < M and farm[di][dj] == 1:
                            farm[di][dj] = 0            # visit 확인이 필요없으므로 배추 확인시 바로 0 
                            q.append([di,dj])
          
            result += 1

    print(result)                       # 최종적인 result 호출