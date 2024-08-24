import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start):
    dist = [sys.maxsize] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, now = heappop(pq)
        if d > dist[now]:
            continue
        for cost, next in edge[now]:
            if dist[next] > d + cost:
                dist[next] = d + cost
                heappush(pq, (dist[next], next))

    return dist

t = int(input())

for _ in range(t):
    n, m, t = map(int, input().split())
    edge = {i: [] for i in range(n + 1)}
    s, g, h = map(int, input().split())
    for _ in range(m):
        a, b, d = map(int, input().split())
        edge[a].append((d, b))
        edge[b].append((d, a))
    
    pos = [int(input()) for _ in range(t)]
    
    dist_from_s = dijkstra(s)
    dist_from_g = dijkstra(g)
    dist_from_h = dijkstra(h)
    
    res = []
    for p in pos:
        path_1 = dist_from_s[g] + dist_from_g[h] + dist_from_h[p]
        path_2 = dist_from_s[h] + dist_from_h[g] + dist_from_g[p]
        
        if dist_from_s[p] == path_1 or dist_from_s[p] == path_2:
            res.append(p)
    
    res.sort()
    print(*res)
