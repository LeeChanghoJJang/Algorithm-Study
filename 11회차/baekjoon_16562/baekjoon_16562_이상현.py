from heapq import *

def prim(start):
    connected = {start}
    unconnected = [(w, v) for w, v in graph[start]]
    heapify(unconnected)
    cost = 0

    while unconnected:
        weight, vertex = heappop(unconnected)

        if vertex in connected:
            continue

        connected.add(vertex)
        cost += weight

        for w, v in graph[vertex]:
            if v in connected:
                continue
            heappush(unconnected, (w, v))

    return cost

N, M, k = map(int, input().split())
list_ = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[0].append((list_[i], i))
    graph[i].append((list_[i], 0))

for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append((0, w))
    graph[w].append((0, v))

result = prim(0)

if result > k:
    print('Oh no')
else:
    print(result)