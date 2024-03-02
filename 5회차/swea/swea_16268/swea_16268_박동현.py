dx = [1,0,-1,0]
dy = [0,1,0,-1]

T = int(input())

for idx in range(T):
    N,M = map(int,input().split())
    ballons = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            s = ballons[i][j]

            for weight in range(1,s+1):                 # 종이 꽃가루 개수만큼 추가로 터진다
                    for dt in range(4):                 # 델타탐색
                        di = i+dx[dt]*weight
                        dj = j+dy[dt]*weight
                        if 0<= di < N and 0<= dj < M:
                            s += ballons[di][dj]
                    if s > result:
                        result = s
    print(f"#{idx+1} {result}")