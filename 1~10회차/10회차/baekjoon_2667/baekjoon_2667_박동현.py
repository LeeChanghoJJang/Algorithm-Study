from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N = int(input())
town = [list(map(int,list(input()))) for _ in range(N)]

visit = [[0]*N for _ in range(N)]
ans =[]

# 리스트 전역 BFS 시행
for i in range(N):
    for j in range(N):
        
        cnt = 0
        
        if not visit[i][j] and town[i][j] == 1:

            q = deque([(i,j)])
            visit[i][j] = 1
            cnt += 1

            while q :
            
                x,y = q.popleft()
            
                for dt in range(4):
                    di = x + dx[dt]
                    dj = y + dy[dt]
            
                    if 0 <= di < N and 0 <= dj < N:
            
                        if not visit[di][dj] and town[di][dj] == 1:
                            q.append((di,dj))
                            visit[di][dj] = 1
                            cnt += 1
        if cnt:
            ans.append(cnt)

print(len(ans))
for i in sorted(ans):
    print(i)