N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
min_ = float('inf')

for start in range(3):
    temp = [row[:] for row in list_]

    for i in range(3):
        if i != start:
            temp[0][i] = float('inf')

    dp[0] = temp[0][:]
    temp[N - 1][start] = float('inf')

    for i in range(1, N):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][k] for k in range(3) if j != k) + temp[i][j]

    min_ = min(min_, min(dp[N - 1]))

print(min_)