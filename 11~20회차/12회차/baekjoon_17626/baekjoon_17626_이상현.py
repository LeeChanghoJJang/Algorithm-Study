n = int(input())
dp = [4] * 50001

for num in range(1, 224):
    dp[num ** 2] = 1

for num in range(1, 50001):
    if dp[num] == 1:
        continue

    for i in range(1, 224):
        temp = i ** 2

        if temp > num:
            continue

        dp[num] = min(dp[num], 1 + dp[num - temp])

print(dp[n])