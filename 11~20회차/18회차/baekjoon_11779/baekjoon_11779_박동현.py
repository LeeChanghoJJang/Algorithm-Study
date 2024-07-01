import sys
from heapq import *

input = sys.stdin.readline
# 입력
N,M = int(input()), int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
start, end = map(int,input().split())

# 최단 거리 경로를 저장할 리스트
route  = [0] * (N+1)
route[start] = start

# 거리 정보를 저장할 리스트
distance = [float("inf")] * (N+1)
distance[start] = 0 

# q에 heappush 하면서 다익스트라 시행
q = [(0,start)] 
while q :
    dist_now, now = heappop(q)

    if distance[now] >= dist_now :
        
        for next, dist_next in graph[now]:
            cost = dist_now + dist_next
            if distance[next] > cost :
                distance[next] = cost
                route[next] = now
                heappush(q,(cost,next))


print(distance[end])

# result 경로를 모두 저장
result = [end]
while end != route[end] :
    result.append(route[end])
    end = route[end]

print(len(result))
print(*reversed(result))