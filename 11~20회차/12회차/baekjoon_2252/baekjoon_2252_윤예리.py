import sys
input = sys.stdin.readline
from collections import deque

def sort_():
    q = deque()

    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for j in graph[now]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                q.append(j)

n, m = map(int, input().split())
in_degree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

result = []
sort_()
print(*result)