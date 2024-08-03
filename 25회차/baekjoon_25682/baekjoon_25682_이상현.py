def check(color):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(M):
            if (i + j) % 2:
                temp = list_[i][j] == color
            else:
                temp = list_[i][j] != color

            dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + temp

    cnt = N * M + 1
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            cnt = min(cnt, dp[i + K - 1][j + K - 1] - dp[i + K - 1][j - 1] - dp[i - 1][j + K - 1] + dp[i - 1][j - 1])

    return cnt

N, M, K = map(int, input().split())
list_ = [list(input()) for _ in range(N)]
print(min(check("B"), check("W")))