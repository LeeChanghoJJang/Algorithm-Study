import sys
input = sys.stdin.readline


def solve(n, k, coins):
    dp = [0] * (k+1)
    dp[0] = 1

    for val in coins:
        for cnt in range(val, k+1):
            dp[cnt] += dp[cnt-val]
    
    return dp[k]


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

result = solve(n, k, coins)
print(result)