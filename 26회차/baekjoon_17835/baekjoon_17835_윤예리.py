import sys
input = sys.stdin.readline
from heapq import *
INF = int(10e10)

def solution():
    hq = []

    for t in targets:
        heappush(hq, (0, t))
        result[t] = 0

    while hq:
        cost, city = heappop(hq)
        if result[city] < cost: continue
        for next_cost, next_city in graph[city]:
            if cost + next_cost < result[next_city]:
                result[next_city] = cost + next_cost
                heappush(hq, (cost+next_cost, next_city))

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[v].append((c, u))

targets = list(map(int, input().split()))
max_start, max_cost = 0, 0
result = [INF for _ in range(n+1)]
solution()
for i, r in enumerate(result):
    if r > max_cost and r != INF:
        max_start, max_cost = i, r

print(max_start)
print(max_cost)