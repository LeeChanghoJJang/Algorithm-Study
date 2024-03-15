from heapq import *

def bfs(start):
    q = []
    heappush(q, (0, start))
    visited[start] = True

    while q:
        dist, vertex = heappop(q)

        for v in graph[vertex]:
            if not visited[v]:
                visited[v] = True
                dist_list[v] = min(dist_list[v], dist + 1)
                heappush(q, (dist + 1, v))

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
dist_list = [float('inf') for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

bfs(X)
flag = 0

for i in range(1, N + 1):
    if dist_list[i] == K:
        flag = 1
        print(i)

if not flag:
    print(-1)