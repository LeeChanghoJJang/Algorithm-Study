import sys
sys.stdin = open('input.txt')
import heapq
# 다익스트라 구현해서 DP 반환(최단거리)
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

n, m, r =map(int,input().split())
# 인덱스를 키값으로하여 아이템 갯수들 저장 
t = dict(enumerate(map(int,input().split()),start=1))
heap = []
graph = [[] for _ in range(n+1)]
for i in range(r):
    a,b,l = map(int,input().split())
    graph[a].append([b,l])
    graph[b].append([a,l])

max_val = 0
for i in range(1,n+1):
    # 각 점으로부터 최단거리 호출
    distances = Dijkstra(i)
    ans = 0
    # 가용거리 내 있으면 그 거리에 있는 아이템 갯수 저장 
    for j in range(1,n+1):
        if distances[j] <= m:
            ans += t[j]
    if max_val < ans:
        max_val = ans
print(max_val)

