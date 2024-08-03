N,M = map(int,input().split())
arr = [[*map(int,list(input()))] for _ in range(N)]

DP = [[0]*M for _ in range(N)]
ans=0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            DP[i][j] += min(DP[i][j-1], DP[i-1][j], DP[i-1][j-1])+1
            ans = max(ans, DP[i][j])
        else:
            DP[i][j]=0
print(ans**2)