# 앱
N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

if not M:
    exit(print(0))

max_sum = sum(costs)
start = set()
start_sum = 0
for i in range(N):
    if not costs[i]:
        start.add(i)
        start_sum += memories[i]

if M <= start_sum:
    exit(print(0))

dp = [[start_sum] * (max_sum+2) for _ in range(N+1)]

result = max_sum

for i in range(1, N+1):
    memory = memories[i-1]
    cost = costs[i-1]

    for j in range(1, max_sum+1):
        if i-1 in start:
            dp[i][j] = dp[i-1][j]
        else:
            if j < cost:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(memory + dp[i-1][j-cost], dp[i-1][j])

        if dp[i][j] >= M:
            result = min(result, j)

print(result)
