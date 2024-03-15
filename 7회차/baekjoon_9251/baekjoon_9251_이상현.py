str1 = input()
str2 = input()

len_str1 = len(str1)
len_str2 = len(str2)

dp = [[0] * (len_str1 + 1) for _ in range(len_str2 + 1)]

for i in range(1, len_str2 + 1):
    for j in range(1, len_str1 + 1):
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max([max(row) for row in dp]))