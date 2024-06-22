dp = [float('inf')] * 101
dp[2] = '1'
dp[3] = '7'
dp[4] = '4'
dp[5] = '2'
dp[6] = '6'
dp[7] = '8'
dp[8] = '10'

for i in range(9, 101):
    for j in range(2, i - 1):
        dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i - j])))

        if j == 6:
            dp[i] = min(dp[i], int(str(dp[i - j]) + '0'))

dp_max = [''] * 101

for i in range(2, 101):
    if i // 2 == 1:
        dp_max[i] = '7' + '1' * ((i - 3)// 2)
    else:
        dp_max[i] = '1' * (i // 2)

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n], dp_max[n])