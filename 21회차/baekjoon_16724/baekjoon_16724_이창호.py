import sys
input =sys.stdin.readline
def dfs(i,j,c):
    global r
    if visit[i][j] != -1:
        if visit[i][j] == c: r+=1
        return
    visit[i][j] = c
    dir = direction.index(Map[i][j])
    dfs(i+dx[dir],j+dy[dir],c)

n,m = map(int,input().split())
Map = [list(input()) for _ in range(n)]
visit = [[-1] * m for _ in range(n)]
direction = ['L','R','U','D'] # (0,-1), (0,1), (-1,0), (1,0)
dx,dy = [0,0,-1,1],[-1,1,0,0]

r,c = 0,0
for i in range(n):
    for j in range(m):
        dfs(i,j,c)
        c+=1
print(r)