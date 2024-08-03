magic = input()
devil = input()
angel = input()

dp = [[[0] * 2 for _ in range(len(magic))] for _ in range(len(devil))]

for i in range(len(devil)):
    if devil[i] == magic[0]:
        dp[i][0][0] = 1
    if angel[i] == magic[0]:
        dp[i][0][1] = 1

for i in range(len(devil)):
    for j in range(1, len(magic)):
        if devil[i] == magic[j]:
            for k in range(i):
                dp[i][j][0] += dp[k][j-1][1]

        if angel[i] == magic[j]:
            for k in range(i):
                dp[i][j][1] += dp[k][j-1][0]

answer = 0
for i in range(len(devil)):
    answer += (dp[i][len(magic) - 1][0] + dp[i][len(magic)-1][1])

print(answer)