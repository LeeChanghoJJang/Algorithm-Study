from heapq import *

def prim(start):
    connected = {start}
    unconnected = [(w, e) for e, w in graph[start]]
    heapify(unconnected)
    sum_ = 0

    while unconnected:
        weight, vertex = heappop(unconnected)

        if vertex in connected:
            continue

        connected.add(vertex)
        sum_ += weight

        for v, w in graph[vertex]:
            if v in connected:
                continue
            heappush(unconnected, (w, v))

    return sum_

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

print(prim(1))