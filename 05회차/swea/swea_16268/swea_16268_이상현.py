T = int(input())
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
 
for tc in range(T):
    N, M = map(int, input().split())
    list_ = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0
 
    for row in range(N):
        for col in range(M):
            temp = list_[row][col]
 
            for i in range(4):
                nrow, ncol = row + drow[i], col + dcol[i]
 
                if not (0 <= nrow < N and 0 <= ncol < M):
                    continue
 
                temp += list_[nrow][ncol]
                max_ = max(max_, temp)
 
    print(f'#{tc + 1} {max_}')