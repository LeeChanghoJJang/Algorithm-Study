from collections import deque


dr = ((1,0),(0,1),(-1,0),(0,-1))
N,M = map(int,input().split()) # N 가로 M 세로

tomatoes = [list(map(int,input().split())) for _ in range(M)]
# 토마토 위치 구하기
q = deque([])
for i in range(M):
    for j in range(N):
        if tomatoes[i][j] == 1 :
            q.append((i,j,0))
# BFS
while q :
    i,j,cnt = q.popleft()

    for dx,dy in dr :
        di, dj = i+dx, j+dy

        if 0 <= di < M and 0 <= dj < N :
            if tomatoes[di][dj] == 0 :
                tomatoes[di][dj] = 1
                q.append((di,dj,cnt+1))
# 0 발견 시 -1 출력 후 종료
for i in range(M):
    for j in range(N):
        if tomatoes[i][j]==0:
            exit(print(-1))

# 그 외에는 마지막에 pop된 cnt가 정답
print(cnt)