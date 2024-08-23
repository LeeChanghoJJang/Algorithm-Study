import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    end = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for i in range(t):
        end.append(int(input()))

    Ds = dijkstra(s)
    Dg = dijkstra(g)
    Dh = dijkstra(h)

    result = []
    for e in end:
        if Ds[g] + Dg[h] + Dh[e] == Ds[e] or Ds[h] + Dh[g] + Dg[e] == Ds[e]:
            result.append(e)

    result.sort()
    for r in result:
        print(r, end=' ')