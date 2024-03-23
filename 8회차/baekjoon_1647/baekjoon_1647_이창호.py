import sys
sys.stdin = open('input.txt')
from heapq import *

def spanning(visited):
    spanning_tree = []
    min_heap = [(0, 1)]
    result = []
    while min_heap:
        weight, start = heappop(min_heap)
        if not visited[start]:
            visited[start]=1
            spanning_tree.append((weight,start))
            result.append(weight)
            for next, edge_weight in graph[start]:
                if not visited[next]:
                    heappush(min_heap,(edge_weight,next))
    return sum(result) - max(result)


N,M = map(int,sys.stdin.readline().split())
graph = {i : [] for i in range(1,N+1)}
for i in range(M):
    start, end, cost = map(int,sys.stdin.readline().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))
print(spanning([0] * (N+1)))
