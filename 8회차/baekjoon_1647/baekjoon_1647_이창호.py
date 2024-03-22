import sys
from heapq import *
sys.stdin = open('input.txt')

def spanning(visited):
    spanning_tree = []
    min_heap = [(0, 1)]
    sum_cost = 0
    while min_heap:
        weight, start = heappop(min_heap)
        if not visited[start]:
            visited[start]=1
            heappush(spanning_tree,(-weight,start))
            sum_cost += weight
            for next, edge_weight in graph[start]:
                if not visited[next]:
                    heappush(min_heap,(edge_weight,next))
    return sum_cost + heappop(spanning_tree)[0]


N,M = map(int,input().split())
graph = {i : [] for i in range(1,N+1)}
for i in range(M):
    start, end, cost = map(int,input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))
print(spanning([0] * (N+1)))
