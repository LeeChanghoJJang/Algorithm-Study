import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(sys.stdin.readline())

    pages = list(map(int,input().split()))

    dp = [[0 for _ in range(n)] for _ in range(n)]  # 2차원 DP

    for x in range(1,n):
        for i in range(n-x):

            j = i+x                                 # i, j 를 뽑고
            dp[i][j] = float('inf')                 # dp 에 최대값으로 덮기
            tmp = sum(pages[i:j+1])                 
            
            for k in range(i,j):
                dp[i][j] = min(dp[i][j],(dp[i][k]+dp[k+1][j]+tmp))  # ????

    print(dp[0][n-1])

## ㅈㅈ 치고 긁어와서 구경함