str1 = input()
str2 = input()
len1 = len(str1)
len2 = len(str2)
dp = [[''] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(len1):
    for j in range(len2):
        if str1[i] == str2[j]:
            dp[i + 1][j + 1] = dp[i][j] + str1[i]
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], key=lambda x: len(x))

result = dp[-1][-1]

if result:
    print(len(result), result, sep='\n')
else:
    print(0)