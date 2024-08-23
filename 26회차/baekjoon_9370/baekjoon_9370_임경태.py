# 9370 미확인 도착지

import heapq, sys
input = sys.stdin.readline
INF = 987654321

# 다익스트라 알고리즘
def dijkstra(x, graph):
    visited = [INF] * (n+1)
    queue = [(0, x)]
    visited[x] = 0

    while queue:
        cost, now = heapq.heappop(queue)

        if cost > visited[now]:
            continue

        for i in graph[now]:
            newcost = cost + i[1]

            if visited[i[0]] > newcost:
                visited[i[0]] = newcost
                heapq.heappush(queue, (newcost, i[0]))

    return visited


for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    arrive = []
    res = []
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(t):
        arrive.append(int(input()))

    Ds = dijkstra(s, graph)
    Dg = dijkstra(g, graph)
    Dh = dijkstra(h, graph)

    for x in arrive:
        if Ds[g] + Dg[h] + Dh[x] == Ds[x] or Ds[h] + Dh[g] + Dg[x] == Ds[x]:
            res.append(x)
    res.sort()
    print(*res)
