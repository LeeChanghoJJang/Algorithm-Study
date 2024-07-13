import sys
input = sys.stdin.readline
from pprint import pprint as print

N = int(input())
l = [int(input()) for _ in range(N)]
r = [int(input()) for _ in range(N)]

link = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if abs(l[i] - r[j]) <= 4:
            link[i].append(j)
    
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if abs(l[i-1] - r[j-1]) <= 4:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][N])