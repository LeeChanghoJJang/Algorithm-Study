import sys
input = sys.stdin.readline

N = int(input().strip())
lefts = [int(input().strip()) for _ in range(N)]
rights = [int(input().strip()) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        if abs(lefts[i] - rights[j]) <= 4:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
# 그 전꺼에서 넘어온것들 비교
print(dp[N][N])
