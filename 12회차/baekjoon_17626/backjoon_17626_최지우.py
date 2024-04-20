n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    mini = 1e9
    j = 1

    while (j ** 2) <= i:
        mini = min(mini, dp[i - (j ** 2)])
        j += 1

    dp.append(mini + 1)
# print(dp)
print(dp[n])
