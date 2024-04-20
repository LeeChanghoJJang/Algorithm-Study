import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def MST(start):
    pq = []
    heappush(pq, (0, start))

    mst = [0] * (V + 1)

    weight_sum = 0
    while pq:
        weight, now = heappop(pq)

        if mst[now]:
            continue

        mst[now] = 1

        weight_sum += weight

        for to in link[now]:
            next_w, nxt = to
            if mst[nxt]:
                continue
            else:
                heappush(pq, (next_w, nxt))
    print(weight_sum)


V, E = map(int, input().split())

link = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    A, B, C = map(int, input().split())
    link[A].append([C, B])
    link[B].append([C, A])

MST(1)