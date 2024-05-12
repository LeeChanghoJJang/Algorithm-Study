N, M = map(int, input().split())

if M == 0:
    exit(0)

memory_list = [0] + list(map(int, input().split()))
cost_list = [0] + list(map(int, input().split()))
sum_ = sum(cost_list)

dp = [[0] * (sum_ + 1) for _ in range(N + 1)]
min_ = float('inf')

for app in range(1, N + 1):
    for j in range(sum_ + 1):
        if j < cost_list[app]:
            dp[app][j] = dp[app - 1][j]

        else:
            dp[app][j] = max(dp[app - 1][j - cost_list[app]] + memory_list[app], dp[app - 1][j])

        if dp[app][j] >= M:
            min_ = min(min_, j)

print(min_)