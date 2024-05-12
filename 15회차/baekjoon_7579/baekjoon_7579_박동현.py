N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
size = sum(C)
DP = [ [0] * (size+1) for _ in range(N) ]

ans = float('inf')

for i in range(N):
    byte,cost = A[i], C[i]
    
    for j in range(size+1):
        if j < cost :
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(byte + DP[i-1][j-cost], DP[i-1][j])

        if DP[i][j] >= M :
            ans = min(ans, j)

print(ans)