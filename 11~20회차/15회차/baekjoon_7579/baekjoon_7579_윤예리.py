# 냅색 문제
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0] * (sum(cost)+1) for _ in range(n+1)]
result = float('inf')

for i in range(1, n+1):
    for j in range(sum(cost)+1):
        if j < cost[i]:   # cost 가 다 떨어지면 이전 dp
            dp[i][j] = dp[i-1][j]

        else:   # 앱 끈 거, 안 끈 거 비교
            dp[i][j] = max(dp[i-1][j-cost[i]] + memory[i], dp[i-1][j])

        if dp[i][j] >= m:
            result = min(result, j)

print(result if m else 0)