import sys

input = sys.stdin.readline
import heapq

N,M = map(int,input().split())  # N : 정점, M : 간선

graph = [[] for _ in range(N+1)] 

for _ in range(M):
    a,b,l = map(int,input().split()) # a : 출발 b : 도착 l : 비용
    graph[a].append((b,l))
    graph[b].append((a,l))


start = 1
hq = [(0,start)]
visit = [False for _ in range(N+1)]

ans = 0
max_cost = 0
while hq :
    dist_now, now = heapq.heappop(hq)

    if not visit[now] :
        visit[now] = True
        ans += dist_now
        max_cost = max(dist_now, max_cost)
        for next,cost in graph[now]:
            heapq.heappush(hq,(cost,next))

print(ans-max_cost)

## prim 알고리즘 : python 시간초과, pypy 335544kb / 6536ms

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

N,M = map(int,input().split())

parent = list(range(N+1))


graphs = []
for _ in range(M):
    a,b,cost = map(int,input().split())
    graphs.append((cost,a,b))

graphs.sort()

ans = 0
max_cost = 0
for graph in graphs :
    cost, a, b = graph
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        ans += cost
        max_cost = max(max_cost, cost)

print(ans-max_cost)

## kruskal 알고리즘 python 198636kb / 3820ms, pypy 268928kb / 4104ms (?)