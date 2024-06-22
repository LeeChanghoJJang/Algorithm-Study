n = int(input())
k = int(input())

dp = [[-1] * (k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i

def solution(n, k):
    if k > n/2:
        dp[n][k] = 0
        return 0

    if dp[n][k] != -1:
        return dp[n][k]
    else:
        dp[n][k] = solution(n-1, k) % 1000000003 + solution(n-2, k-1) % 1000000003
        return dp[n][k] % 1000000003

print(solution(n, k))