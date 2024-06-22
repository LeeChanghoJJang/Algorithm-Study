N,K = int(input()), int(input())

DP = [ [0]*(K+1) for _ in range(N+1) ]

for i in range(N+1):
    for j in range(K+1):
        if j==0:
            DP[i][j] = 1
        if j==1:
            DP[i][j] = i
    DP[i][j] += DP[i-1][j]
    DP[i][j] += DP[i-2][j-1] if i!= N else DP[i-3][j-1]

    DP[i][j] %= 1000000003

print(DP[N][K])