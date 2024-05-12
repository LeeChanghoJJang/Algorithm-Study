import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
memory = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [[0 for _ in range(sum(costs)+1)] for _ in range(N+1)] # dp[i][j] => 1~i번째 앱까지, j의 cost로 확보 가능한 메모리의 최대
# 행은 앱의 갯수만큼
for i in range(1, N+1):
    # 열은 총비용만큼 만들어줌(열만큼 cost를 사용함으로써 확보가능한 최대 메모리값)
    for j in range(0, sum(costs)+1):
        # 총비용보다 작으면 갱신해줘야지 메모리 최댓값 더 큰 것으로
        if j >= costs[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i-1]]+memory[i-1])
        # 만약 크다?..면 더이상 더해줄 필요 없지
        else:
            dp[i][j] = dp[i-1][j]
for i, mem in enumerate(dp[N]):
    if mem >= M:
        print(i)
        break
