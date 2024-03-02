T = int(input())
drow, dcol = [1, 1, 0, -1, -1, -1, 0, 1], [0, -1, -1, -1, 0, 1, 1, 1]
 
for tc in range(T):
    N, M = map(int, input().split())
    list_ = [list(map(int, input().split())) for _ in range(N)]
    result = 0
 
    for row in range(N):
        for col in range(M):
            land = list_[row][col]
            cnt = 0
 
            for i in range(8):
                nrow, ncol = row + drow[i], col + dcol[i]
 
                if not (0 <= nrow < N and 0 <= ncol < M) or list_[nrow][ncol] >= list_[row][col]:
                    continue
 
                cnt += 1
 
            if cnt >= 4:
                result += 1
 
    print(f'#{tc + 1} {result}')