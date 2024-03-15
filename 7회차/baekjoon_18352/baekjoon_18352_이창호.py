import sys
sys.stdin = open('input.txt')
from collections import deque
import heapq

def BFS(start):
    queue = deque([start])
    visited[start]=1
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = visited[now]+1
                queue.append(next)
    temp= []
    for i,j in enumerate(visited):
        if j-1==K:
            temp.append(i)
    if temp:
        for i in sorted(temp):
            print(i)
    else:
        print(-1)
    return

N, M, K, X = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
visited = [0] * (N+1)
for i in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
BFS(X)
# import sys
# from collections import deque
#
# def BFS(start):
#     queue = deque([(start, 0)])  # Use tuples to store node and distance
#     visited[start] = 1
#     while queue:
#         now, distance = queue.popleft()
#         for next_node in graph[now]:
#             if not visited[next_node]:
#                 visited[next_node] = visited[now] + 1
#                 queue.append((next_node, distance + 1))
#     result = [i for i, j in enumerate(visited) if j - 1 == K]
#     if result:
#         print(*sorted(result))
#     else:
#         print(-1)
#
# N, M, K, X = map(int, input().split())
# graph = [[] for _ in range(N + 1)]
# visited = [0] * (N + 1)
#
# for _ in range(M):
#     start, end = map(int, input().split())
#     graph[start].append(end)
#
# BFS(X)

