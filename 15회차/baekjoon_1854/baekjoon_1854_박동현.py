# BFS에서 cnt나 다른 변수를 두는 것처럼 다익스트라에서도 변형이 가능.
import sys
input = sys.stdin.readline
from heapq import heappush, heappop


N,M,K = map(int,input().split())

graph = [ [] for _ in range(N+1) ]
for _ in range(M): 
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))

# K번째 최단거리를 찾기 위해 각 인덱스마다 K만큼의 공간을 줌 
distance = [ [float('inf')] * (K) for _ in range(N+1) ]
# 초기값 설정은 동일
distance[1][0] = 0

hq = [(0,1)]

# 다익스트라 (변형)
while hq :
    dist_now, now = heappop(hq)

    # K 번째 최단거리를 찾기 위해서기 때문에 최단 거리인지 비교하는 구문 변경 
    # if dist_now > distance[now] :
    #     continue
    
    if dist_now > distance[now][-1]:
        continue
    
    # 순회하면서
    for next, dist_next in graph[now]:
        cost = dist_next + dist_now
        
        # if distance[next] > cost :
        #     distance[next] = cost

        # sort하면서 진행할 것이기 때문에 마지막 값(현재 저장된 최대치)과 cost를 비교
        if distance[next][K-1] > cost:
            distance[next][K-1] = cost
            distance[next].sort()
        
            # 순회
            heappush(hq, (cost,next))


for i in range(1,N+1):
    print(distance[i][-1] if distance[i][-1] != float('inf') else -1)