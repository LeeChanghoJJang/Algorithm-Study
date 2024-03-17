from collections import deque

def bfs(start):
    q = deque()
    q.append((0, start))
    visited = [False] * (N + 1)
    visited[start] = True

    while q:
        depth, vertex = q.popleft()
        depth_list[vertex] = depth

        for v in graph[vertex]:
            if not visited[v]:
                visited[v] = True
                parent[v] = vertex
                q.append((depth + 1, v))

def find(v1, v2):
    while depth_list[v1] != depth_list[v2]:
        if depth_list[v1] > depth_list[v2]:
            v1 = parent[v1]
        else:
            v2 = parent[v2]

    while v1 != v2:
        v1 = parent[v1]
        v2 = parent[v2]

    return v1

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
depth_list = [0] * (N + 1)

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

bfs(1)

M = int(input())
pair_list = []

for _ in range(M):
    pair_list.append(tuple(map(int, input().split())))

for v1, v2 in pair_list:
    print(find(v1, v2))