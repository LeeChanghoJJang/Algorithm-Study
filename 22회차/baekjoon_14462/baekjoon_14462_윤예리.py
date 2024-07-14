import sys
input = sys.stdin.readline

n = int(input())
cows = [0] + list(int(input()) for _ in range(n))
right = [0] + list(int(input()) for _ in range(n))

dp = [[0] * 1001 for _ in range(1001)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        if (abs(cows[i] - right[j]) <= 4):
            dp[i][j] = dp[i-1][j-1] + 1

print(dp[n][n])