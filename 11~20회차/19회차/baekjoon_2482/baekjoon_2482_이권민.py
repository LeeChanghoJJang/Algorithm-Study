N = int(input())
K = int(input())

#1~i번째 색 중에서 j개의 색을 선택하는 경우의 수
dp = [[0]*(K+1) for _ in range(N+1)]

# nCr = n-1Cr + n-1Cr-1

# 반드시 N>=4, K>=1
for i in range(N+1):
    for j in range(K+1):
        if j == 0:
            dp[i][j] = 1
            continue
        if j == 1:
            dp[i][j] = i
            continue
        dp[i][j] += dp[i-1][j]
        # i번째 색을 선택하지 않는 경우
        dp[i][j] += dp[i-2][j-1] if i != N else dp[i-3][j-1] # n번째 색을 반드시 고른 경우면, 1번째와 n-1번째 색은 못 고르니까.
        # i번째 색을 선택하는 경우. 
        dp[i][j] %= 1_000_000_003
print(dp)
print(dp[N][K])
'''
조합의 합공식 이용
1-i 개 중 k개 선택하는 경우의 수

'''