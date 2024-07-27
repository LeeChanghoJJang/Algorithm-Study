import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n,k = map(int,input().split())

things = [(0,0)] + [tuple(map(int,input().split())) for i in range(n)]

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w = things[i][0]
    v = things[i][1]
    for j in range(1,k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[n][k])
