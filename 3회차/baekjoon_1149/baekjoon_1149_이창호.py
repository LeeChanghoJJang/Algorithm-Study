# 1149 RGB 거리
import sys
sys.stdin = open('input.txt')
N = int(input())
DP = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,N):
    DP[i][0] = min(DP[i - 1][1],DP[i - 1][2]) + DP[i][0]
    DP[i][1] = min(DP[i - 1][0],DP[i - 1][2]) + DP[i][1]
    DP[i][2] = min(DP[i - 1][0],DP[i - 1][1]) + DP[i][2]
print(min(DP[N-1]))
