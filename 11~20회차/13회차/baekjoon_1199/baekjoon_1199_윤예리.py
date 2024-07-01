# 오일러 회로
# DFS를 돌면서 가장 먼저 완료되는 정점부터 기록
# 모든 정점의 간선 개수가 짝수개여야지만 성립 가능
# 이미 방문이 끝난 간선은 제거 >> Hash로 저장

def dfs(x):
    for y in graph[x]:
        if arr[x][y]:
            arr[x][y] -= 1
            arr[y][x] -= 1
            dfs(y)
    print(x + 1, end=' ')


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

graph = {}
for i in range(n):
    graph[i] = []
    total = 0
    for j in range(n):
        for k in range(arr[i][j]):
            total += 1
            graph[i].append(j)

    # 간선이 홀수개면 성립 불가
    if total % 2:
        exit(print(-1))

dfs(0)
print(graph)

#
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
# from collections import defaultdict
# # defaultdict : key가 있으면 반환, 없으면 생성
#
# n = int(input())
# graph = []
# degree = [0] * n
# visit = [[0] * n for _ in range(n)]
# for i in range(n):
#     lst = {}
#     for j, v in enumerate(list(map(int, input().split()))):
#         if v:
#             lst[j] = 1
#             visit[i][j] = v
#             degree[i] += v
#     graph.append(lst)
#
# for i in range(n):
#     if degree[i] % 2:
#         exit(print(-1))
#
# answer = []
# stack = [0]
# while stack:
#     current = stack[-1]
#     if graph[current]:
#         # next(): 이터레이터 안에 있는 객체를 차례로 반환 (for문 하듯이)
#         # iter(): 이터레이터 객체를 반환
#         next_ = next(iter(graph[current]))
#         visit[next_][current] -= 1
#         visit[current][next_] -= 1
#         degree[current] -= 1
#         degree[next_] -= 1
#
#         if not visit[current][next_]:
#             del graph[current][next_]
#             del graph[next_][current]
#         stack.append(next_)
#
# for i in range(n):
#     if degree[i]:
#         exit(print(-1))
# print(' '.join(map(str, answer)))
