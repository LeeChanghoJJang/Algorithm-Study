import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())  # 레벨의 수
characters_per_level = list(map(int, input().split()))  # 각 레벨별 캐릭터의 수
power_per_level = list(map(int, input().split()))  # 각 레벨별 힘

# 최대 날짜 D 입력 받기
D = int(input())

# 초기 총 힘 계산
initial_power = sum([characters_per_level[i] * power_per_level[i] for i in range(N)])

# DP 배열 초기화
dp = [[0] * (D + 1) for _ in range(N)]

# 초기 상태 설정: 각 레벨에서 그대로 있을 때의 힘
for i in range(N):
    dp[i][0] = characters_per_level[i] * power_per_level[i]

# DP 배열 갱신
for d in range(1, D + 1):
    for i in range(N):
        for j in range(i + 1, N):
            if d >= j - i:  # 날짜가 충분할 때만
                characters_to_move = characters_per_level[i]
                power_gain = characters_to_move * (power_per_level[j] - power_per_level[i])
                dp[j][d] = max(dp[j][d], dp[i][d - (j - i)] + power_gain)

# 최대 힘 계산
max_power = initial_power
for d in range(D + 1):
    for i in range(N):
        max_power = max(max_power, dp[i][d])

# 최종 결과 출력
print(max_power)
