from collections import deque
dr = (1,0),(0,1),(-1,0),(0,-1)

N = int(input())
arr = [ [*map(int,input().split())] for _ in range(N) ]
k = 1

# 색칠하고 lands에 담기
lands = dict()
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1: 
            k+=1 
            arr[i][j] = k
            q = deque([(i,j)])
            lands[k] = [(i,j)]
            while q :
                x,y = q.popleft()
                for dx,dy in dr :
                    di,dj = x+dx, y+dy
                    if 0 <= di < N and 0 <= dj < N:
                        if arr[di][dj] == 1:
                            arr[di][dj] = k
                            q.append((di,dj))
                            lands[k].append((di,dj))

# 거리 계산하기
ans = float('inf') 
for k in lands :
    q = deque(lands[k])
    visit = [ [-1]*N for _ in range(N) ]
    for x,y in lands[k]:
        visit[x][y] = 0
    while q :
        x,y = q.popleft()
        for dx,dy in dr:
            di,dj = x+dx, y+dy
            if 0 <= di < N and 0 <= dj < N:
                if visit[di][dj]==-1 :
                    if arr[di][dj] != 0 and arr[x][x] != k:
                        ans = min(ans,visit[x][y])
                        break
                    visit[di][dj] = visit[x][y] + 1
                    q.append((di,dj))

# 최단거리 출력            
print(ans)