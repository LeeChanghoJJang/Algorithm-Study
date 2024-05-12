import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra():
    heap = []
    heappush(heap, (0, 1))
    dist[1][0] = 0

    while heap:
        now_w, now_node = heappop(heap)
        for nxt_w, nxt_node in link[now_node]:
            new_w = now_w + nxt_w
            if dist[nxt_node][k - 1] <= new_w:
                continue

            dist[nxt_node][k - 1] = new_w
            dist[nxt_node].sort()
            heappush(heap, (new_w, nxt_node))


n, m, k = map(int, input().split())

link = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    link[a].append((c, b))

dist = [[1e9] * k for _ in range(n+1)]
dijkstra()

for i in range(1, n+1):
    if dist[i][k-1] == 1e9:
        print(-1)
    else:
        print(dist[i][k-1])
