from heapq import *

def prim(start):
    connected = {start}
    unconnected = [(0, v) if (start, v) in pre_connected else (d, v) for d, v in graph[start]]
    heapify(unconnected)
    sum_ = 0

    while unconnected:
        d, v = heappop(unconnected)

        if v in connected:
            continue

        connected.add(v)
        sum_ += d

        for dist_, vertex in graph[v]:
            if vertex in connected:
                continue
            if (v, vertex) in pre_connected:
                heappush(unconnected, (0, vertex))
            else:
                heappush(unconnected, (dist_, vertex))
    return sum_

N, M = list(map( int, input().split()))
graph = [[] for _ in range(N + 1)]
pre_connected = set()
c_list = [0] + [tuple(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i + 1, N + 1):
        dist_ = ((c_list[i][0] - c_list[j][0]) ** 2 +
                (c_list[i][1] - c_list[j][1]) ** 2) ** 0.5
        graph[i].append((dist_, j))
        graph[j].append((dist_, i))

for _ in range(M):
    x, y = list(map(int, input().split()))
    pre_connected.add((x, y))
    pre_connected.add((y, x))

print(f'{round(prim(1), 2):.2f}')