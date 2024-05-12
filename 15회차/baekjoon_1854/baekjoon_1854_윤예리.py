import sys
input = sys.stdin.readline
from heapq import *

n, m, k = map(int, input().split())
q = []
distance = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

heappush(distance[1], 0)
heappush(q, (0, 1))

while q:
    dist, now = heappop(q)
    for i in graph[now]:
        cost = dist + i[0]
        if len(distance[i[1]]) < k:
            heappush(distance[i[1]], -cost)
            heappush(q, (cost, i[1]))
        elif cost < -distance[i[1]][0]:
            heappop(distance[i[1]])
            heappush(distance[i[1]], -cost)
            heappush(q, (cost, i[1]))

for i in range(1, n+1):
    if len(distance[i]) == k:
        print(-distance[i][0])
    else:
        print(-1)