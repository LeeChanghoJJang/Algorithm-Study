import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
m = int(input())

link = {i:[] for i in range(n+1)}
for _ in range(m):
    s, e, w = map(int, input().split())
    link[s].append((w, e))

start, end = map(int, input().split())

heap = []
heappush(heap, (0, start))

inf = float('INF')
visited = [inf for _ in range(n+1)]
visited[start] = 0
prev = [0] * (n+1)
while heap:
    now_w, now = heappop(heap)

    if visited[end] <= now_w:
        continue

    for nxt_w, nxt in link[now]:
        new_w = now_w + nxt_w
        if visited[nxt] <= new_w:
            continue

        visited[nxt] = new_w
        prev[nxt] = now
        if nxt != end:
            heappush(heap, (new_w, nxt))

result = [end]
cur = end
while cur != start:
    result.append(prev[cur])
    cur = prev[cur]
print(visited[end])
print(len(result))
print(*result[::-1])


