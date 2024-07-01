# 1854 K번째 최단경로 찾기

from heapq import heappush, heappop

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [[] for _ in range(N+1)]
Q = []

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

heappush(dist[1], 0)  # 비용
heappush(Q, (0, 1))   # 비용, 도시

while Q:
    now_w, now = heappop(Q)

    for next_w, next in graph[now]:
        cost = now_w + next_w
        # 거리가 K보다 작을 때
        if len(dist[next]) < K:
            heappush(dist[next], -cost)
            heappush(Q, (cost, next))
        # heapq의 -가장 작은 값보다 cost가 작을 때
        elif cost < -dist[next][0]:
            heappop(dist[next])
            heappush(dist[next], -cost)
            heappush(Q, (cost, next))

for i in range(1, N+1):
    print(-dist[i][0] if len(dist[i]) == K else -1)