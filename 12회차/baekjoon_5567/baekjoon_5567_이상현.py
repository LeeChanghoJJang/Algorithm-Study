from collections import deque

def bfs(start):
    q = deque()
    q.append((0, start))
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        depth, vertex = q.popleft()

        for v in graph[vertex]:
            if visited[v] or depth > 1:
                continue
            visited[v] = True
            q.append((depth + 1, v))

    return sum(visited) - 1

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))