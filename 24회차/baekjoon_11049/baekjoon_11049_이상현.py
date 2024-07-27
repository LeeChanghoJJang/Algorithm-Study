import sys
input = sys.stdin.readline

N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(N - 1):
    for j in range(N - i - 1):
        k = i + j + 1
        dp[j][k] = float('inf')

        for l in range(j, k):
            dp[j][k] = min(dp[j][k], dp[j][l] + dp[l + 1][k] + list_[j][0] * list_[l][1] * list_[k][1])

print(dp[0][-1])