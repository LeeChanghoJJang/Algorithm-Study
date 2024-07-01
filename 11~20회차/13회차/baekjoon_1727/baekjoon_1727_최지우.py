n, m = map(int, input().split())

N = list(map(int, input().split()))
M = list(map(int, input().split()))

N.sort()
M.sort()

result = 0
if n == m:
    for i in range(n):
        result += abs(N[i] - M[i])
    exit(print(result))

if n < m:
    N, M = M, N
    n, m = m, n

dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(i, n+1):
        dp[i][j] = dp[i-1][j-1] + abs(M[i-1]-N[j-1])
        if i == j:
            continue

        dp[i][j] = min(dp[i][j], dp[i][j-1])
print(dp[m][n])