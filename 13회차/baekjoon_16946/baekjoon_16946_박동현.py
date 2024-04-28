import sys
from collections import deque 

input = sys.stdin.readline


dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
maze = [ list(map(int,list(input().strip()))) for _ in range(N)]

ans = [ [0] * M for _ in range(N) ]

tmp = {1:0}
idx = 2
visit = [ [0]*M for _ in range(N) ]
for i in range(N):
    for j in range(M):
        if maze[i][j] == 0 and not visit[i][j] :
            visit[i][j] = 1
            q = deque([(i,j)])
            maze[i][j] = idx
            cnt = 1
            while q :
                x,y = q.popleft()

                for dx,dy in dr :
                    di, dj = x+dx, y+dy
                    if 0 <= di < N and 0 <= dj < M :
                        if maze[di][dj] == 0 :
                            maze[di][dj] = idx
                            q.append((di,dj))
                            visit[di][dj] = 1
                            cnt += 1
            tmp[idx] = cnt
            idx += 1


for i in range(N):
    for j in range(M):
        if maze[i][j] == 1:
            ans[i][j] = 1

            temp = set()

            for dx,dy in dr :
                di, dj = i+dx, j+dy

                if 0 <= di < N and 0 <= dj < M :
                    temp.add(maze[di][dj])
            
            for x in temp :
                ans[i][j] += tmp[x]

            ans[i][j] %= 10
for answer in ans:
    print(*answer, sep="")