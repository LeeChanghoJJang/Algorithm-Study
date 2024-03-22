import sys
sys.stdin = open("input.txt")
from heapq import *

# KRUSKAL
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])
edges.sort(key=lambda x: x[2])
parents = [i for i in range(n+1)]

cnt = 0
sum_weight = 0

for s, e, w in edges:
    if find_set(s) == find_set(e):
        continue

    cnt += 1
    union(s, e)


    if cnt == n-1:
        break

    sum_weight += w

print(sum_weight)


# 메모리 초과
# prim algorithm
#
# def prim(start):
#     pq = [(0, start)]
#     MST = [0] * (n+1)
#
#     sum_weight = 0
#
#     while pq:
#         weight, now = heappop(pq)
#
#         if MST[now]:
#             continue
#
#         MST[now] = 1
#         sum_weight += weight
#
#         for to in range(n):
#             if graph[now][to] == 0 or MST[to]:
#                 continue
#
#             heappush(pq, (graph[now][to], to))
#     return sum_weight
#
# n, m = map(int, input().split())
# graph = [[0] * (n+1) for _ in range(n+1)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#     graph[b][a] = c
#
# print(prim(1))

