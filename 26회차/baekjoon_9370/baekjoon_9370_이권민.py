import sys
import heapq

def dijkstra(start, n, graph):
    dist = [int(1e9)] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > dist[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    end = [int(input()) for _ in range(t)]
    # g로 가는 최단경로 이후 h에서 end지점으로 가는 최단경로, h로 가는 최단경로 이후 g에서 end지점으로 가는 최단경로 
    # s에서 end까지의 최단경로 중 이것들보다 작은 애들은 end 후보지 제외
    
    dist_s = dijkstra(s, n, graph)
    dist_g = dijkstra(g, n, graph)
    dist_h = dijkstra(h, n, graph)
    
    results = []
    
    for x in end:
        # s -> g -> h -> x 또는 s -> h -> g -> x 의 경로가 최단 경로와 같은지 확인
        IsRight = 0
        if (dist_s[g] + dist_g[h] + dist_h[x]) >= (dist_s[h] + dist_h[g] + dist_g[x]):
            IsRight = dist_s[h] +dist_h[g] + dist_g[x]
        else:
            IsRight = dist_s[g] + dist_g[h] + dist_h[x]
        if (IsRight == dist_s[x]):
            results.append(x)
    
    results.sort()
    print(*results)