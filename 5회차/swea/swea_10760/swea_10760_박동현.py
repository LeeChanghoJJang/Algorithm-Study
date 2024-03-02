t = int(input())

dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]

for idx in range(t):
    N,M = map(int,input().split())
    space = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            cnt = 0 
            for dt in range(8):
                di = i + dx[dt]
                dj = j + dy[dt]
                if 0 <= di < N and 0 <= dj < M:
                    if space[i][j] > space[di][dj]:
                        cnt +=1
            if cnt >=4 :
                ans += 1
    print(f"#{idx+1} {ans}")