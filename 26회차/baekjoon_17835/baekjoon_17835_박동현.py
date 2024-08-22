import sys; input = sys.stdin.readline
from heapq import heappop, heappush

# 로직: 다익스트라를 갈기는데 노드를 역순으로 넣고 모든 좌표를 넣어서 갈겨버림
def djikstra():
    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]: continue

        for nxt, cost in graph[now]:
            dist_nxt = dist_now + cost

            if distance[nxt] > dist_nxt:
                distance[nxt] = dist_nxt
                heappush(hq, (dist_nxt, nxt))


N, M, K = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int,input().split())
    graph[b].append((a, cost))

distance = [float('inf')]*(N+1)
hq = []
for i in map(int,input().split()):
    distance[i] = 0
    heappush(hq, (0, i))

djikstra()

ans, ans_dist = 0, 0
for i,v in enumerate(distance[1:], start=1):
    if v > ans_dist:
        ans_dist = v
        ans = i
print(ans)
print(ans_dist)
