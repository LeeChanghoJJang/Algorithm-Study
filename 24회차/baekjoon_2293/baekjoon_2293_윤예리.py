import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])

dp = [1] + [0] * k  # dp[x] : x 라는 수를 만드는 데에 필요한 경우의 수

for i in coins: # 1로만 10을 만드는 경우의 수
    for j in range(i, k+1): # 1과 2로 10을 만드는 경우의 수
        dp[j] += dp[j-i]
print(dp[k])