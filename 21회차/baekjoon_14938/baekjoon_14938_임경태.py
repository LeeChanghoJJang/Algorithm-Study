# 14938 서강그라운드
from heapq import heappop, heappush

N, M, R = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
ans = 0

for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

for i in range(1, N+1):
    item = 0
    dist = [float("inf")] * (N+1)
    dist[i] = 0
    Q = [(0, i)]

    while Q:
        now_cost, now = heappop(Q)

        if dist[now] < now_cost: continue

        item += items[now]

        for next_cost, next in graph[now]:
            cost = now_cost + next_cost

            if cost <= M and dist[next] > cost:
                heappush(Q, (cost, next))
                dist[next] = cost

    ans = max(ans, item)

print(ans)
