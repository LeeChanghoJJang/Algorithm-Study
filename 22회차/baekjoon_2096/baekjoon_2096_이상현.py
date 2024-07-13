dp = [0] * 6
memo = [0] * 6

for _ in range(int(input())):
    temp = list(map(int, input().split()))

    dp[0] = max(memo[0], memo[1]) + temp[0]
    dp[1] = max(memo[:3]) + temp[1]
    dp[2] = max(memo[1], memo[2]) + temp[2]

    dp[3] = min(memo[3], memo[4]) + temp[0]
    dp[4] = min(memo[3:]) + temp[1]
    dp[5] = min(memo[4], memo[5]) + temp[2]

    memo = dp[:]

print(max(dp[:3]), min(dp[3:]))