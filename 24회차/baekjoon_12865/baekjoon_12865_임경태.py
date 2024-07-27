# 12865 평범한 배낭
N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (K + 1) for _ in range(N + 1)]

# DP 테이블 채우기
for i in range(1, N + 1):
    for j in range(1, K + 1):
        # 현재 물건의 무게가 현재 최대 무게 j보다 작거나 같은 경우
        if j >= bag[i - 1][0]:
            # 현재 물건을 담는 경우와 담지 않는 경우 중 최대 가치를 선택
            DP[i][j] = max(bag[i - 1][1] + DP[i - 1][j - bag[i - 1][0]], DP[i - 1][j])
        else:
            # 현재 물건을 담을 수 없는 경우, 이전 물건까지 고려한 최대 가치를 그대로 사용
            DP[i][j] = DP[i - 1][j]

# 최종 결과 출력, DP[N][K]는 N개의 물건을 고려했을 때 배낭의 최대 무게 K에서의 최대 가치
print(DP[N][K])
