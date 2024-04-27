# 백준 1149번 RGB거리

# dp를 이용한 접근
N = int(input())

# m은 이전 줄까지의 최소 비용을 저장
# dp는 현재 줄까지의 최소 비용
m = [0] * 3
dp = [0] * 3

for _ in range(N):
    temp = list(map(int, input().split()))

    for i in range(3):

        # 직전의 집과 현재의 집은 색이 같으면 안되는 조건
        dp[i] = min(m[j] for j in range(3) if j != i) + temp[i]

    # 1차원 리스트이므로 슬라이싱 이용
    m = dp[:]

print(min(dp))