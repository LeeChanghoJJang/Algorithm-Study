import sys
sys.stdin = open('input.txt')
from collections import deque
import heapq
# 다익스트라 써볼랬는데, 인접한 거리가 항상 1이라 안써도 풀 수 있을거 같아서 BFS로 함
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
        # 최단거리가 K인 경우에는 temp에 저장
        if j-1==K:
            temp.append(i)
    # temp에 있으면 sort해서 출력
    if temp:
        for i in sorted(temp):
            print(i)
    # 없으면 -1
    else:
        print(-1)
    return

N, M, K, X = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
visited = [0] * (N+1)
# 인접한 거리는 항상 1이기
for i in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
# X부터 출발
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

