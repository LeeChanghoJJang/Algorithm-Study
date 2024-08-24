import sys
from collections import deque
input = sys.stdin.readline


def dfs(i, now):
    que = deque([i])
    visited[i] = now
    while que:
        v = que.pop()
        now = visited[v]
        for to in edge[v]:
            if not visited[to]:
                que.append(to)
                visited[to] = now*(-1)
            else:
                if visited[to] == now:
                    return True
    


for tc in range(int(input())):
    V, E = map(int, input().split())

    edge = {i: [] for i in range(1, V+1)}

    for _ in range(E):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    visited = [0] * (V+1)

    result = 'YES'

    for i in range(1, V+1):
        if not visited[i]:
            if dfs(i, 1):
                result = 'NO'

    print(result)