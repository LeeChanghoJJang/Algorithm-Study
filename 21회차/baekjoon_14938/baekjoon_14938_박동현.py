from heapq import *

n,m,r = map(int,input().split())                # n : 지역 m : 수색 범위 r : 길 개수

items = [0] + list(map(int,input().split()))    # items : 각 지역에서 얻을 수 있는 아이템 개수

graph = [[] for _ in range(n+1)]                # graph : 인접 리스트            

for _ in range(r):                              # 인접 리스트 구성
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

ans = 0                                         # ans : 각 좌표 중 최대값

for i in range(1,n+1):
    distance = [float('inf')] * (n+1)           # distance : 거리 리스트 (각 인덱스에 도달할 수 있는 최소거리가 저장됨)
    distance[i] = 0                             # 탐색 값을 0 으로 지정
    q=[(0,i)]                                   # q 에 (현재 거리, 시작점) 담고 시작

    while q :
        dist_now, now = heappop(q)              # dist_now : 현재 누적 거리, now : 현재 위치

        if distance[now] >= dist_now :          # 리스트에 담겨있는 거리가 현재 거리보다 크거나 같다면 (지금 탐색이 최소 거리로 진행되고 있다는 뜻)

            for next, dist_next in graph[now]:  # 갈 수 있는 길을 탐색하면서, ( next : 다음 위치, dist_next : 다음 위치까지의 거리)
                cost = dist_now + dist_next     # cost : 현재 누적 거리와 다음 위치까지의 거리를 더한 값 

                if distance[next] > cost:       # 지금 계산한 거리가 더 짧은 경우
                    distance[next] = cost       # 갱신하고
                    heappush(q,(cost,next))     # q에 푸시

    tmp = 0
    for idx, value in enumerate(items):         # idx : 지역, value : 지역에서 얻을 수 있는 아이템
        if m >= distance[idx] :                 # 지역의 거리가 수색 범위 내라면
           tmp += value                         # 획득 가능
    ans = max(ans, tmp)                         # ans와 최대값 비교

print(ans)                                      # 최대값 출력