import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())  # 레벨의 수
characters_per_level = list(map(int, input().split()))  # 각 레벨별 캐릭터의 수
power_per_level = list(map(int, input().split()))  # 각 레벨별 힘
sum_power = sum([characters_per_level[i] * power_per_level[i] for i in range(N)])  # 초기 총 힘

D = int(input())  # 최대 레벨 차이

# dp 배열 초기화
dp = [[0] * N for _ in range(N)]
# dp[i][j]: i에서 j로 레벨업할 때 힘의 증가량

# dp 배열 채우기
for i in range(N):
    for j in range(N):
        if i < j:
            dp[i][j] = power_per_level[j] - power_per_level[i]

# 예제 입력에 대한 처리를 진행합니다. 이 부분에서는 특정 규칙에 따라 총 힘을 계산하거나 갱신합니다.
# 예를 들어, dp 테이블을 사용하여 가능한 모든 레벨업 조합을 고려해 최적의 결과를 도출할 수 있습니다.

# 레벨업 후의 총 힘을 계산하는 로직
max_sum_power = sum_power  # 레벨업 후의 최대 총 힘을 저장하는 변수

# 가능한 모든 레벨업 조합을 고려하여 총 힘을 계산합니다.
for i in range(N):
    for j in range(i + 1, min(i + D + 1, N)):
        if dp[i][j] > 0:  # i에서 j로 레벨업할 때 힘이 증가하는 경우만 고려
            new_sum_power = sum_power + characters_per_level[i] * dp[i][j]
            max_sum_power = max(max_sum_power, new_sum_power)

# 최종 결과 출력
print(max_sum_power)
