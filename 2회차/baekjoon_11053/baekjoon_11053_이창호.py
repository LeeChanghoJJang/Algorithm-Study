# 백준 11053 가장 긴 증가하는 부분수열
# 약간만 이해한 참이라 다시 한번 보고 진행 필요
N = int(input())
sequence = map(int,input().split())
dp = [1]*N
for i in range(N):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))


'''
10 1
10 20 2
10 20 10 2
10 20 10 30 3
10 20 10 30 20 3
10 20 10 30 20 50 4

'''
