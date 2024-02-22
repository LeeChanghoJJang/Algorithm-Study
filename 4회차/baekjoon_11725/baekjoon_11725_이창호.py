import sys
sys.stdin = open('input.txt')
# 첫번째 방법
# N = int(input())
# connection = [[] for _ in range(N+1)]
# trees = [list(map(int,input().split())) for i in range(N-1)]
# visited = [0] *(N+1)
# stack = [1]
# while stack:
#     now = stack.pop()
#     visited[now] = 1
#     for i,j in trees:
#         if i == now and not visited[j]:
#             connection[j].append(i)
#             stack.append(j)
#         elif j ==now and not visited[i]:
#             connection[i].append(j)
#             stack.append(i)
# for i in range(2,N+1):
#     print(*connection[i])
import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent, connection, visited):
    visited[node] = 1
    for child in connection[node]:
        if not visited[child]:
            parent[child] = node
            dfs(child, parent, connection, visited)

N = int(input())
connection = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

dfs(1, parent, connection, visited)
print(parent)
for i in range(2, N + 1):
    print(parent[i])
