import sys
input = sys.stdin.readline

N = int(input())

left_list = [0] + [int(input()) for _ in range(N)]
right_list = [0] + [int(input()) for _ in range(N)]
dp = [[0] * 1001 for _ in range(1001)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        if abs(left_list[i] - right_list[j]) <= 4:
            dp[i][j] = dp[i - 1][j - 1] + 1

print(dp[N][N])