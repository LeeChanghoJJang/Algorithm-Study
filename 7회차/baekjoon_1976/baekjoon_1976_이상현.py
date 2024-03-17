from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        vertex = q.popleft()

        for v in graph[vertex]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(1, N + 1):
    temp = list(map(int, input().split()))

    for j in range(1, N + 1):
        if temp[j - 1]:
            graph[i].append(j)
            graph[j].append(i)

list_ = list(map(int, input().split()))
bfs(list_[0])

if any(not visited[i] for i in list_):
    print('NO')
else:
    print('YES')