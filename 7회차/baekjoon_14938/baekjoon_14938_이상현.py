import sys
input = sys.stdin.readline

import heapq

def dijkstra(start, graph):
    q = []
    cost_list[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        current_cost, current_vertex = heapq.heappop(q)

        if current_cost > cost_list[current_vertex]:
            continue

        for cost, vertex in graph[current_vertex]:
            temp = current_cost + cost

            if temp < cost_list[vertex]:
                cost_list[vertex] = temp
                heapq.heappush(q, (temp, vertex))

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
item = [0] + list(map(int, input().split()))
temp = 0

for _ in range(r):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((cost, v2))
    graph[v2].append((cost, v1))

for i in range(1, n + 1):
    cost_list = [float('inf')] * (n + 1)
    dijkstra(i, graph)
    temp = max(sum(item[j] for j in range(1, n + 1) if cost_list[j] <= m), temp)

print(temp)