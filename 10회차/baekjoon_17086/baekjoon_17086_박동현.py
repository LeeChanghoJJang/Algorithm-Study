from collections import deque
# 델타 설정
dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]

# bfs
def bfs (i,j) :
    q = deque([(i,j)])
    visit = [[0] * M for _ in range(N)]

    while q :
        i,j = q.popleft()

        if ocean[i][j] == 1:
            ans.append(visit[i][j])
            break
        for dt in range(8):
            di = i + dx[dt]
            dj = j + dy[dt]
            if 0 <= di < N and 0 <= dj < M :
                if not visit[di][dj] :
                    visit[di][dj] = visit[i][j] + 1
                    q.append((di,dj))
            
# 백트래킹 
def backtrack() :
    for i in range(N):
        for j in range(M):
            if not ocean[i][j] :
                ocean[i][j] = 2
                bfs(i,j)
                ocean[i][j] = 0


N,M = map(int,input().split())

ocean = [list(map(int,input().split())) for _ in range(N)]

ans = []
# bfs를 백트래킹 하면서 최대값을 구함
backtrack()
print(max(ans))