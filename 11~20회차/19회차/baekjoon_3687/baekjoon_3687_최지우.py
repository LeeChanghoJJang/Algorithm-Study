import sys
input = sys.stdin.readline

t = int(input())

dp = [sys.maxsize for _ in range(101)]
d = [1, 7, 4, 2, 6, 8, 10]
for i in range(2, 9):
    dp[i] = d[i-2]

for i in range(9, 101):
    for j in range(2, 8):
        if j != 6:
            dp[i] = min(dp[i], dp[i-j]*10 + dp[j])
        else:
            dp[i] = min(dp[i], dp[i-j]*10)

for _ in range(t):
    n = int(input())
    max_ = '7' if n%2 else '1'
    max_ += '1' * (n//2 - 1)
    print(dp[n], max_)


