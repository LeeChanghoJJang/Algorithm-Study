n, m = map(int, input().split())
list_ = [list(map(int, list(input()))) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if list_[i - 1][j - 1]:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

max_ = max(max(row) for row in dp)
print(max_ ** 2)