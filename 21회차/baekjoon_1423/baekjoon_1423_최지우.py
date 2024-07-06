import sys

sys.setrecursionlimit(10000)

def solve(level, upgrade, remain):
    if remain < 0 or level >= n:
        return -1

    if dp[level][upgrade][remain] != -1:
        return dp[level][upgrade][remain]

    if level == n - 1:
        dp[level][upgrade][remain] = (characters[level] + upgrade) * powers[level]
        return dp[level][upgrade][remain]

    cnt = min(characters[level] + upgrade, remain)
    res = 0
    for count in range(cnt + 1):
        nxt = solve(level + 1, count, remain - count)
        if nxt == -1:
            continue

        cur = powers[level] * (characters[level] + upgrade - count)
        result = nxt + cur
        res = max(res, result)

    dp[level][upgrade][remain] = res
    return res

n = int(input())
characters = list(map(int, input().split()))
powers = list(map(int, input().split()))
d = int(input())

dp = [[[-1 for _ in range(d + 1)] for _ in range(d + 1)] for _ in range(n)]

print(solve(0, 0, d))