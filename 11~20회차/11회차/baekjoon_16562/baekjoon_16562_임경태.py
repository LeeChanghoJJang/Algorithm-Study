# 16562 친구비

N, M, k = map(int, input().split())
cost = list(map(int, input().split()))

# 그래프 제작
graph = [[] for _ in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

# DFS를 통한 체크
sum_cost = 0
visit = [False] * (N+1)
for i in range(1, N+1):
    if visit[i]: continue
    visit[i] = True
    min_cost = 10000

    stack = [i]
    while stack:
        now = stack.pop()
        # 비용 비교 후 최솟값 결정
        min_cost = min(min_cost, cost[now-1])

        for next in graph[now]:
            if visit[next]: continue
            visit[next] = True
            stack.append(next)

    sum_cost += min_cost

print(sum_cost if sum_cost <= k else 'Oh no')