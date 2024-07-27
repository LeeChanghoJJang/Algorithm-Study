import sys
input = sys.stdin.readline


def knapsack(N, K, items):
    dp = [0] * (K + 1)

    for weight, val in items:
        for w in range(K, weight-1, -1):
            dp[w] = max(dp[w], dp[w-weight] + val)
    
    return dp[K]


N, K = map(int, input().split())
items = [(map(int, input().split())) for _ in range(N)]

print(knapsack(N, K, items))