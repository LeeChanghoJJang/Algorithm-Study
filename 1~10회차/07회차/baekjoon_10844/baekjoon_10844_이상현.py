N = int(input())
dp = [[0] * N for _ in range(10)]

for i in range(10):
    dp[i][0] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[j][i] += dp[j + 1][i - 1]

        elif j == 9:
            dp[j][i] += dp[j - 1][i - 1]

        else:
            dp[j][i] += dp[j - 1][i - 1] + dp[j + 1][i - 1]

print(sum(dp[i][N - 1] for i in range(1, 10)) % 1000000000)