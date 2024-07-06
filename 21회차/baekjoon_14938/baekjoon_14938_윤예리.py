import sys
input = sys.stdin.readline
from heapq import *

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

result = 0
for i in range(1, n+1):
    distance = [float('inf')] * (n+1)
    hq = []

    heappush(hq, (0, i))
    distance[i] = 0

    while hq:
        cur_dist, cur_node = heappop(hq)

        if cur_dist > distance[cur_node]:
            continue

        for next_ in graph[cur_node]:
            new_dist = cur_dist + next_[1]

            if new_dist < distance[next_[0]]:
                distance[next_[0]] = new_dist
                heappush(hq, (new_dist, next_[0]))

    tmp = 0
    for i, d in enumerate(distance):
        if d <= m:
            tmp += items[i-1]
    result = max(tmp, result)

print(result)