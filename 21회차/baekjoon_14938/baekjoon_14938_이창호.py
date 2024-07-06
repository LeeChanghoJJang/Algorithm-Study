import sys
import heapq

def Dijkstra(start):
    dp = [100 for _ in range(n + 1)]
    INF = int(1e9)
    dp[start]=0
    heapq.heappush(heap,(start,0))
    while heap:
        now, wei  = heapq.heappop(heap)
        if dp[now] < wei:
            continue
        for next, cost in graph[now]:
            next_cost = cost + wei
            if next_cost < dp[next]:
                dp[next] = next_cost
                heapq.heappush(heap,(next,next_cost))
    return dp

n, m, r =map(int,sys.stdin.readline().split())
t = dict(enumerate(map(int,sys.stdin.readline().split()),start=1))
heap = []
graph = [[] for _ in range(n+1)]
for i in range(r):
    a,b,l = map(int,sys.stdin.readline().split())
    graph[a].append([b,l])
    graph[b].append([a,l])

max_val = 0
for i in range(1,n+1):
    distances = Dijkstra(i)
    ans = 0
    for j in range(1,n+1):
        if distances[j] <= m:
            ans += t[j]
    if max_val < ans:
        max_val = ans
print(max_val)

