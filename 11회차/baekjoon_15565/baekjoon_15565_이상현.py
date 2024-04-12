N, K = map(int, input().split())
list_ = list(map(int, input().split()))
min_length = float('inf')

dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + (list_[i - 1] == 1)

min_length = float('inf')

left = right = 0

while right <= N:
    count = dp[right] - dp[left]

    if count >= K:
        min_length = min(min_length, right - left)
        left += 1
    else:
        right += 1

if min_length != float('inf'):
    print(min_length)
else:
    print(-1)
