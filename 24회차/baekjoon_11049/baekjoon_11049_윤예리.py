import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if i + j == n: break
        dp[i][i+j] = float('inf')
        for k in range(i, i+j):
            dp[i][i+j] = min(dp[i][i+j], dp[i][k] + dp[k+1][i+1] + arr[i][0] * arr[k][1] * arr[i+j][1])

print(dp[0][n-1])
