import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(q):
    while q:
        now = q.popleft()
        for next in graph[now]:
            orders[next] -= 1
            if orders[next] == 0:
                print(next, end=' ')
                q.append(next)

for tc in range(1, 11):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))
    graph = [[] for _ in range(V+1)]
    orders = [0] * (V+1)

    for i in range(0, E*2, 2):
        graph[edge[i]].append(edge[i+1])
        orders[edge[i+1]] += 1

    q = deque()
    print(f'#{tc}', end=' ')
    for i in range(1, V+1):
        if orders[i] == 0:
            print(i, end=' ')
            q.append(i)
    BFS(q)
    print()
