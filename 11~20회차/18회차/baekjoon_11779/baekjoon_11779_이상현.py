from heapq import *

def dijkstra(start):
    q = []
    q.append((0, start, [start]))
    cost_list[start] = 0

    while q:
        cost, vertex, path = heappop(q)

        if cost_list[vertex] < cost:
            continue

        for temp in graph[vertex]:
            v, cost_v = temp[0], temp[1]

            if cost_list[v] > cost + cost_v:
                cost_list[v] = cost + cost_v

                if v == end:
                    heappush(result, (cost_list[v], path + [v]))

                q.append((cost + cost_v, v, path + [v]))

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
cost_list = [float('inf')] * (n + 1)
result = []

for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))

start, end = map(int, input().split())
dijkstra(start)

if start == end:
    print(0)
    print(1, 1, sep = '\n')
else:
    temp = heappop(result)
    print(temp[0])
    print(len(temp[1]))
    print(*temp[1])