# 2482 색상환
N = int(input())
K = int(input())

# 색 분배 불가능한 경우
if K > N//2: exit(print(0))

# dp[i][j] : i개의 색 중에서 j개를 선택
DP = [[0] * (K+1) for _ in range(N+1)]

# n개의 색 중에서 1개를 선택하는 경우의 수는 n개
for i in range(N+1): DP[i][1] = i

# DP 실행
for i in range(2, N+1):
    for j in range(2, K+1):
        DP[i][j] += DP[i-1][j]
        DP[i][j] += DP[i-2][j-1] if i != N else DP[i-3][j-1]
        DP[i][j] %= 1000000003

print(DP[N][K])