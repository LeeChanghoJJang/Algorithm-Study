# 18352 특정 거리의 도시 찾기 (실버2)

import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]; INF = float('inf')
dist = [INF] * (N+1); dist[X] = 0

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

Q, ans = [], []
heappush(Q, [0, X])

while Q:
    w, now = heappop(Q)

    if dist[now] < w: continue

    if w == K: ans.append(now); continue

    for next in graph[now]:
        cost = w + 1
        if dist[next] > cost:
            dist[next] = cost
            heappush(Q, [cost, next])

if ans:
    for i in ans: print(i)
else: print(-1)