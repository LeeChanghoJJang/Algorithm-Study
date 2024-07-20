import sys
input = sys.stdin.readline


n, m = map(int, input().split())
lens = [int(input()) for _ in range(n)]

dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(m + 1):
        if dp[i][j] != float('inf'):
            dp[i + 1][lens[i]] = min(dp[i + 1][lens[i]], dp[i][j] + (m - j) ** 2)
            if j + lens[i] + (1 if j > 0 else 0) <= m:
                dp[i + 1][j + lens[i] + (1 if j > 0 else 0)] = min(dp[i + 1][j + lens[i] + (1 if j > 0 else 0)], dp[i][j])

result = min(dp[n])
for i in dp:
    print(i)
print(result)