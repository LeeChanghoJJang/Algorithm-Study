rings = input().strip()
bridge = [list(input().strip()) for _ in range(2)]

strlen = len(rings)
bdglen = len(bridge[0])
dp = [[[0] * (strlen+1) for _ in range(bdglen+1)] for _ in range(2)]
for i in range(bdglen):
    if bridge[0][i] == rings[0]:
        dp[0][i][1] = 1
    if bridge[1][i] == rings[0]:
        dp[1][i][1] = 1

for i in range(1, strlen):
    for j in range(bdglen):
        if bridge[0][j] == rings[i]:
            for k in range(j):
                dp[0][j][i+1] += dp[1][k][i]
        if bridge[1][j] == rings[i]:
            for k in range(j):
                dp[1][j][i+1] += dp[0][k][i]
            
result = 0
for i in range(bdglen + 1):
    result += dp[0][i][strlen]
    result += dp[1][i][strlen]

print(result)