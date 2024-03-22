from heapq import *

def prim(start):
    connected = {start}
    unconnected = [(c, e) for e, c in graph[start]]
    heapify(unconnected)
    edges = []

    while unconnected:
        cost, current = heappop(unconnected)

        if current in connected:
            continue

        edges.append(cost)
        connected.add(current)

        for next, next_cost in graph[current]:
            if next in connected:
                continue
            heappush(unconnected, (next_cost, next))

    return edges

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

result = prim(1)
print(sum(result) - max(result))