def death_note(idx):
    if dp[idx] < n * m ** 2:
        return dp[idx]

    r = m - list_[idx]

    for i in range(idx + 1, n + 1):
        if r >= 0:
            if i == n:
                dp[idx] = 0
                break

            dp[idx] = min(dp[idx], r ** 2 + death_note(i))
            r -= list_[i] + 1
    return dp[idx]

n, m = map(int, input().split())
list_ = [int(input()) for _ in range(n)]
dp = [n * m ** 2] * (n + 1)
dp[n] = 0

print(death_note(0))