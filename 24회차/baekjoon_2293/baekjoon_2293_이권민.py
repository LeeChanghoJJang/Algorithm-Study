n,k = map(int, input().split())
# 보통이면 dp = [(0)*N for _ in range(N)] 같은 식으로 해서 지금 애가 들어갔을때랑 안들어갔을때.
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()

DP = [0] * (k + 1)
DP[0] = 1
for c in coins:
    for i in range(c, k + 1):
        DP[i] += DP[i - c]
print(DP[k])