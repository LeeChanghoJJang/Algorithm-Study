import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, g):
    q = deque([start])
    visited[start] = g

    while q:
        x = q.popleft()

        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]:
                return False
    return True

tc = int(input())
for _ in range(tc):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, v+1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')