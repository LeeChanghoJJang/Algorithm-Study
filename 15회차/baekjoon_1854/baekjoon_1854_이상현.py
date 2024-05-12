from heapq import *

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist_list = [[] for _ in range(n + 1)]
q = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

heappush(dist_list[1], 0)
heappush(q, (0, 1))

while q:
    dist_, cur = heappop(q)

    for cost, next_ in graph[cur]:
        ndist = dist_ + cost

        if len(dist_list[next_]) < k:
            heappush(dist_list[next_], -ndist)
            heappush(q, (ndist, next_))
        elif ndist < -dist_list[next_][0]:
            heappop(dist_list[next_])
            heappush(dist_list[next_], -ndist)
            heappush(q, (ndist, next_))

for i in range(1, n + 1):
    if len(dist_list[i]) == k:
        print(-dist_list[i][0])
    else:
        print(-1)