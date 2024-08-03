import sys
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def backtrack(idx=0) :
    global ans
    if idx == 3 :
        ans = max(ans,bfs())
        return 
    
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                backtrack(idx+1)
                lab[i][j] = 0


def bfs () :
    labs = [row[:] for row in lab]
    visit = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and labs[i][j] == 2:
                q = deque(two)
                while q :
                    i,j = q.popleft()

                    for dt in range(4):
                        di = i + dx[dt]
                        dj = j + dy[dt]
                        if 0 <= di < N and 0 <= dj < M:
                            if not visit[di][dj] and labs[di][dj] == 0:
                                visit[di][dj] = 1
                                labs[di][dj] = 2
                                q.append((di,dj))
    return sum([x.count(0) for x in labs])




N,M = map(int,input().split()) # N 세로 M 가로
two = []

lab = []
for x in range(N):
    tmp = list(map(int,input().split()))

    for y,value in enumerate(tmp):
        if value == 2:
            two.append((x,y))
    lab.append(tmp)

ans = 0

backtrack()

print(ans)