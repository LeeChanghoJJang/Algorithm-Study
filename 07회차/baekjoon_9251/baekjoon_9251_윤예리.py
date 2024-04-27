str1, str2 = input(), input()
m, n = len(str1), len(str2)

dp = [[0] * (n+1) for _ in range(m+1)]      # 2차원 배열 만들어서 최대값 저장

for i in range(1, m+1):
    for j in range(1, n+1):                 # str1의 한 글자씩 str2와 비교
        if str1[i-1] == str2[j-1]:          # 같으면 이전 최대값에 + 1
            dp[i][j] = dp[i-1][j-1] + 1
        else:                               # 다르면 이전까지의 최대값 그대로
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[m][n])     # 마지막 칸 프린트