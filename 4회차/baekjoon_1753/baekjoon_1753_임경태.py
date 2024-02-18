# 1753 / 최단경로 / 골드4

import math
import heapq

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
INF = math.inf
dist = [INF] * (V+1); dist[K] = 0

# 방향 그래프 제작 (가중치, 다음 노드)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

# Dijkstra
Q = []
heapq.heappush(Q, (0, K))

while Q:
    w, now = heapq.heappop(Q)

    # 현재 가중치보다 큰 가중치면 무시
    if dist[now] < w:
        continue

    for next_w, next in graph[now]:
        cost = w + next_w
        # 현재 노드를 거쳐, 다음 노드로 이동하는 비용이 더 적은 경우
        if dist[next] > cost:
            dist[next] = cost
            heapq.heappush(Q, (dist[next], next))

for i in dist[1:]:
    print(i if i != INF else 'INF')

'''
70504KB / 676ms
'''