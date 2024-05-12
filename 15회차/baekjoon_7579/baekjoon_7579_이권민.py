# 메모리, 비용. 특정 메모리가 필요할 경우
# 그 메모리 이상 비활성화, 그 중 비용이 최소인 값.
# N,M  = map(int,input().split())
# memory_st = list(map(int,input().split()))
# cost_st = list(map(int,input().split()))
# 최대에서 내려가야 될거같은데. 내려가면서 그 때의 비용이 더 작으면 갱신. 아니면 그대로
# 메모리를 전부 다썼을 때. 거기서 넣거나 빼거나. 더 작은 거를 비용으로. 
# 아니지. 비용을 기준으로 오름차순. 제일 적은 비용에 메모리. 그거보다 낮은 애들은 그걸로 고정.
# 근데 낮은 비용 두개 더하고 메모리 더한거 보다 그 다음 비용이 더 작고 메모리도 클 수 있잖아.

# lst = []
# sum_c = 0
# sum_m = 0
# for i in range(N):
#     lst.append([cost_st[i],memory_st[i]])
#     sum_m += memory_st[i]
#     sum_c += cost_st[i]
# lst.sort(reverse=True)
# result = [sum_c,sum_m]


# 비용이 같을수도 있으니까. 이건 람다로 나중에. 특정 코스트에 가능한 바이트의 값.


N,M = map(int,input().split())
memories = [0]+list(map(int,input().split()))
costs = [0] + list(map(int,input().split()))
length = sum(costs)+1
dp = [[0]*(length) for _ in range(N+1)]
result = 10e10
for i in range(1,N+1):
    cost = costs[i]
    memory = memories[i]
    for j in range(length):
        dp[i][j] = dp[i-1][j]
    for j in range(cost,length):
        dp[i][j] = max(dp[i-1][j-cost]+memory,dp[i][j])
        if dp[i][j] >= M:
            result = min(result,j)
print(result)