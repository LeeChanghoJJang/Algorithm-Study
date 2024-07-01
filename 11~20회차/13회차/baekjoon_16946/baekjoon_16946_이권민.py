# import sys
# from collections import deque
# def BFS(row,col):
#     deq = deque([[row,col]])
#     id = str(row)+str(col)
#     cnt = 1
#     visited[row][col] = id
#     while deq:
#         r,c = deq.popleft()
        
#         for i in range(4):
#             lr = dr[i]+r
#             lc = dc[i]+c
#             if 0 <= lr < N and 0 <= lc < M and matrix[lr][lc] == '0' and visited[lr][lc] != id:
#                 visited[lr][lc] = id
#                 deq.append([lr,lc])
#                 cnt += 1
#     return cnt
                

# N,M = map(int,input().split())
# matrix = [sys.stdin.readline() for _ in range(N)]
# result = [[0]*M for _ in range(N)]
# visited = [[0]*M for _ in range(N)]

# dr = [1,0,-1,0]
# dc = [0,1,0,-1]
# for i in range(N):
#     for j in range(M):
#         if matrix[i][j] == '1':
#             result[i][j] = BFS(i,j)%10
#         print(result[i][j],end='')
#     print()

from collections import deque

def bfs(start, num):
    q = deque() 
    q.append(start)

    cnt = 1
    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy
            # 범위 내에 있고 빈 공간이며, 방문을 한 적 없다면
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0 and visited[nx][ny] == 0:
                visited[nx][ny] = num
                cnt+=1
                q.append((nx,ny))

    return cnt
                
                            

n,m = map(int,input().split())
grid = [list(map(int,input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dxs, dys = [1,-1,0,0], [0,0,1,-1]

area = {}
area[0] = 0

# 각 구역의 빈 칸 정보 저장
num = 1
for x in range(n):
    for y in range(m):
        if grid[x][y] == 0 and visited[x][y] == 0:
            visited[x][y] = num
            cnt = bfs((x, y), num)
            area[num] = cnt

            num+=1
            

for x in range(n):
    for y in range(m):
        if grid[x][y] == 1:
            
            # 중복되는 구역의 빈칸을 더하는 것 방지.
            ss = set()

            # 벽인 부분의 상하좌우 확인
            for dx,dy in zip(dxs,dys):
                nx,ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and grid[nx][ny] == 0:
                    ss.add(visited[nx][ny])
            
            # 각 구역의 빈 칸을 더하기
            for s in ss:
                grid[x][y] += area[s]

            grid[x][y] %= 10


for i in grid:
    print("".join(map(str, i)))