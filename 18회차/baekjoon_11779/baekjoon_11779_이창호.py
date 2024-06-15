import sys
sys.stdin = open('input.txt')
from collections import defaultdict
from heapq import heappush,heappop
input=sys.stdin.readline
def dijkstra(start):
    dist[start] = 0
    heap = []
    heappush(heap,(0,start))
    while heap:
        wei,now = heappop(heap)
        if dist[now] < wei:
            continue
        for next_node, next_wei in graph[now]:
            next_cost = wei + next_wei
            if next_cost < dist[next_node]:
                dist[next_node] = next_cost
                prev_node[next_node] = now
                heappush(heap,(next_cost,next_node))

N = int(input())
M = int(input())
graph = defaultdict(list)
dist = [float('inf')] * (N + 1)
prev_node = [0] * (N+1)
for i in range(M):
    start,end,wei = map(int,input().split())
    graph[start].append((end,wei))

start, end = map(int,input().split())
dijkstra(start)
print(dist[end])
path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))