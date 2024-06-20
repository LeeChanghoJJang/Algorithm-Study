T = int(input())
for tc in range(1, T+1):
    k = int(input())
    arr = [0] + sorted(list(map(int, input().split())))

    ls = [0 for _ in range(k+1)]

    for i in range(1, k+1):
        ls[i] = ls[i-1] + arr[i]

    dp = [[0 for i in range(k + 1)] for j in range(k + 1)]

    for i in range(2, k+1):
        for j in range(1, k+2-i):
            dp[j][j+i-1] = min([dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)]) +(ls[j+i-1] - ls[j-1])

    print(dp[1][k])