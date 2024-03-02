dx = [0,1,0,-1]
dy = [1,0,-1,0]

T = int(input())
for tc in range(1,T+1):
    M, N = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(M)]
    result = 0
    for x in range(M):
        for y in range(N):
            temp = arr[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<M and 0<=ny<N:
                    temp += arr[nx][ny]
            if result < temp:
                result = temp

    print(f'#{tc} {result}')