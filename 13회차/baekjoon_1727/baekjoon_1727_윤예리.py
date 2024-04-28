import sys
input = sys.stdin.readline

n, m = map(int, input().split())
per_n = sorted(list(map(int, input().split())))
per_m = sorted(list(map(int, input().split())))

# 만약 n이 많으면 남녀를 바꿔준다.
# 여자가 많다고 가정하고 풀어줄 예정이라
if n > m:
    n, m = m, n
    per_n, per_m = per_m, per_n

dp = [[0] * m for _ in range(n)]    # 2차원 dp로 풀 예정
# dp[남자][여자] = 남자가 여자를 선택했을 때 셩격 차 합의 최소값
dp[0][0] = abs(per_n[0] - per_m[0])
for i in range(1, m-(n-1)):
    dp[0][i] = min(abs(per_n[0]-per_m[i]), dp[0][i-1])

for i in range(1, n):
    for j in range(i, m-(n-i-1)):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + abs(per_n[i]-per_m[j])
        else:
            dp[i][j] = min(dp[i-1][j-1] + abs(per_n[i]-per_m[j]), dp[i][j-1])
print(dp[n-1][m-1])
