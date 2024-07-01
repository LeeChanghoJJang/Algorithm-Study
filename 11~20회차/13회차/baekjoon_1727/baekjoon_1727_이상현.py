# 입력으로 남자들의 수 n과 여자들의 수 m을 받습니다.
n, m = map(int, input().split())

# 남자들의 성격을 나타내는 리스트를 입력 받고 정렬합니다.
m_list = sorted(map(int, input().split()))

# 여자들의 성격을 나타내는 리스트를 입력 받고 정렬합니다.
w_list = sorted(map(int, input().split()))

# DP(Dynamic Programming) 테이블을 생성합니다.
# dp[i][j]는 m_list의 i번째 요소와 w_list의 j번째 요소까지 고려했을 때 성격 차의 합을 나타냅니다.
dp = [[0] * (m + 1) for _ in range(n + 1)]

# DP 테이블을 채우는 반복문입니다.
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # m_list의 i번째 요소와 w_list의 j번째 요소를 짝지어 만들었을 때의 성격 차를 더한 값입니다.
        dp[i][j] = dp[i - 1][j - 1] + abs(m_list[i - 1] - w_list[j - 1])

        # i가 j보다 큰 경우, 남은 요소 중 하나를 선택하지 않는 경우를 고려하여 갱신합니다.
        if i > j:
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
        # i가 j보다 작은 경우, w_list의 요소 중 하나를 선택하지 않는 경우를 고려하여 갱신합니다.
        elif i < j:
            dp[i][j] = min(dp[i][j], dp[i][j - 1])

# DP 테이블의 마지막 값을 출력합니다.
# 이 값은 m_list와 w_list를 짝지어서 만들 수 있는 성격 차의 합을 최소화한 값입니다.
print(dp[n][m])
