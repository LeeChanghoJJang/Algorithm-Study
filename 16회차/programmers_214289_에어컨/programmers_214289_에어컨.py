def solution(temperature, t1, t2, a, b, onboard):
    # 인덱스를 맞추기 위해 온도를 10씩 더해준다
    temperature, t1, t2 = temperature + 10, t1 + 10, t2 + 10
    # 시간을 행으로, 온도를 열로, 값은 누적된 소비전력을 넣는다.
    dp = [[float("inf")] * 53 for _ in range(len(onboard))]
    # 시간이 0일 때는 온도가 어떻든 소비전력이 0으로 시작
    dp[0][temperature] = 0
    # 신경써야할 온도의 최소값과 최대값을 설정합니다.
    min_t, max_t = min(temperature, t1), max(temperature, t2)
    for i in range(1, len(onboard)):
        # 손님이 있으면 지정된 최소온도와 최대온도를 신경쓰고,
        # 없을 때에는 실외온도와 비교해서 작거나 큰걸로 결정해도 무관함
        start, end = [t1, t2] if onboard[i] else [min_t, max_t]

        for j in range(start, end + 1):
            # 이전 시간 간격에서 현재 온도로 변하는 비용을 계산
            # 실외온도와 실내온도가 같으면 b, 다르면 a만큼 소비전력 소모
            l = dp[i - 1][j - 1] if j-1 < temperature else dp[i - 1][j - 1] + a
            m = dp[i - 1][j] if j == temperature else dp[i - 1][j] + b
            h = dp[i - 1][j + 1] if j+1 > temperature else dp[i - 1][j + 1] + a
            # 위 3개 중에 가장 누적소비전력이 작은것을 dp배열에 저장
            dp[i][j] = min(l, m, h)
    return min(dp[-1])

print(solution(28,18,26,10,8,[0, 0, 1, 1, 1, 1, 1]))