# 7579 앱

N, M = map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))
DP = [0] * (sum(cost)+1)  # 비용당 비활성화 가능한 메모리

for i in range(N):  # 각 앱에 대하여
    for j in range(sum(cost), cost[i]-1, -1):  # 각 비용에 대하여
        # 앱의 비용이 j보다 작다면
        if j >= cost[i]:
            # 비활성화하지 않았을 때의 바이트 수, 비활성화하였을 때의 바이트 수를 더한 값 비교
            DP[j] = max(DP[j], DP[j - cost[i]] + byte[i])

# 필요한 바이트 수 M 이상을 처음으로 달성하는 최소 비용 찾기
for i, mem in enumerate(DP):
    if mem >= M: exit(print(i))