# 백준 11053 가장 긴 증가하는 부분수열
import sys
sys.stdin = open('input.txt')

N = int(input())
sequence = list(map(int,input().split()))
dp = [1]*N
for i in range(1,N):
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(dp)


'''
10 1 DP[1] = 1
10 20 2 DP[2] = max(DP[1], DP[2]) if DP[i] > DP[i-1]: DP[i] +=1
10 20 10 2
10 20 10 30 3
10 20 10 30 20 3
10 20 10 30 20 50 4

'''
