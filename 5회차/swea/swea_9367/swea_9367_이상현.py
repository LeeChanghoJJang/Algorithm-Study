T = int(input())

for tc in range(T):
    N = int(input())
    list_ = list(map(int, input().split()))
    dp = [1] * N
 
    for i in range(N - 1):
        if list_[i + 1] > list_[i]:
            dp[i + 1] = dp[i] + 1
 
    print(f'#{tc + 1} {max(dp)}')