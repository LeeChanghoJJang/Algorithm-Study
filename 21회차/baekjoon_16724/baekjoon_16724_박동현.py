from sys import stdin
input = stdin.readline

dr = {
    "D" : (1,0),
    "U" : (-1,0),
    "L" : (0,-1),
    "R" : (0,1)
}

def dfs(x, y, cycle=[]):
    global cnt

    visit[x][y] = 1
    
    dx,dy = dr[arr[x][y]]
    di,dj = x+dx, y+dy

    if visit[di][dj]:                   # 이동한 곳를 이미 방문한 경우
        if (di, dj) in cycle:           # 사이클에 이 곳이 포함되어 있다면
            cnt += 1                    # 사이클이 생겼으므로 세이프 존을 설치해야한다.
                                        # 방문한 곳인데 사이클에 이 위치가 포함되어 있지 않다면
                                        # 다른 사이클에 이미 포함됐던 위치이므로 처리할 필요 없음
    else: dfs(di, dj, cycle+[(x,y)])    # 방문안했으면 다음 위치로


N,M = map(int,input().split())
arr = [ list(input()) for _ in range(N) ]

cnt = 0
visit = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if visit[i][j]: continue
        dfs(i,j)
        
print(cnt)