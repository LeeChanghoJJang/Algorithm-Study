import sys
input = sys.stdin.readline
from heapq import *

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

# 가장 가까운 노드
nearest_node = [start] * (n+1)
distance = [10e10] * (n+1)

q = [(0, start)]
while q:
    dist, node = heappop(q)
    if dist > distance[node]:
        continue

    for next_node, next_dist in graph[node]:
        cost = next_dist + dist
        if cost < distance[next_node]:
            distance[next_node], nearest_node[next_node] = cost, node
            heappush(q, (cost, next_node))

answer = []
tmp = end
while tmp != start:
    answer.append(str(tmp))
    tmp = nearest_node[tmp]

answer.append(str(start))
answer.reverse()

print(distance[end])
print(len(answer))
print(" ".join(answer))