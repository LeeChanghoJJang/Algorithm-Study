import sys
from heapq import heappop, heappush

N, M, K = map(int, input().split())
link = {i:[] for i in range(1, N+1)}

for _ in range(M):
    u, v, c = map(int, input().split())
    link[v].append((c, u))
    
pos = list(map(int, input().split()))


def dijkstra(start):
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        now_d, now = heappop(pq)
        if now_d > dist[now]:
            continue
        for next_d, next in link[now]:
            new_d = now_d + next_d
            if new_d < dist[next]:
                dist[next] = new_d
                heappush(pq, (new_d, next))

dist = [sys.maxsize] * (N+1)
dist[0] = 0
for start in pos:
    dijkstra(start)

result = [1, 0]
for i in range(1, N+1):
    if dist[i] > result[1]:
        result = [i, dist[i]]

for i in result:
    print(i)

