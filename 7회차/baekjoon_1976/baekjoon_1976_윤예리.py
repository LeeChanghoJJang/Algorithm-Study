# Union-Find Algorithm ?

from collections import deque

def bfs(start):
    q = deque()

    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()

        for idx, value in enumerate(graph[now]):        # idx랑 값을 같이 받아와서 idx라는 노드까지 도달할 수 있으면 visited = 1
            if value and visited[idx] == 0:
                q.append(idx)
                visited[idx] = 1

n, m = int(input()), int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
trip = list(map(int, input().split()))
visited = [0] * n

bfs(trip[0]-1)
for city in trip:
    if visited[city-1] == 0:
        print('NO')
        break
else:
    print('YES')
