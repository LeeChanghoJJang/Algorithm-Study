import sys; input = sys.stdin.readline
from heapq import heappop, heappush

#로직: 다익스트라를 하면서, 특정 노드를 지나가는 경우 check를 True로 표시

def dijkstra():
    while hq:
        dist_now, now, is_checked = heappop(hq)

        if dist_now > distance[now][0]: continue

        for nxt, cost, check in graph[now]:
            dist_nxt = dist_now+cost
            new_check = is_checked or check

            if distance[nxt][0] > dist_nxt:
                distance[nxt] = [dist_nxt, new_check]
                heappush(hq, (dist_nxt, nxt, new_check))

            elif distance[nxt][0] == dist_nxt and not distance[nxt][1] and new_check:
                distance[nxt][1] = new_check
                heappush(hq, (dist_nxt, nxt, new_check))    


for _ in range(int(input())):
    N,M,T = map(int,input().split())        # N 노드, M 간선, T 목적지 후보
    S,G,H = map(int,input().split())        # S 출발지, G-H : 필수 도로

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b,d = map(int,input().split())
        check = (a==H and b==G) or (a==G and b==H)

        graph[a].append((b,d,check))
        graph[b].append((a,d,check))

    distance = [[float('inf'), False] for _ in range(N+1)]
    distance[S][0] = 0
    hq = [(0,S,False)]

    dijkstra()

    ans = []
    for _ in range(T):
        num = int(input())
        if distance[num][1]:
            ans.append(num)
    
    print(*sorted(ans))