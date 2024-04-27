# import sys
# sys.stdin = open('input.txt')

def bfs(s, N):
    visited = [0] * (N + 1)
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        t = q.pop(0)
        for i in graph[t]:
            if not visited[i]:
                q.append(i)
                visited[i] += 1 + visited[t]

    if not visited[b]:
        print(-1)
    else:
        print(visited[b]-1)

n = int(input())
a, b = map(int, input().split())
m = int(input())

# 그래프 그리기
graph = [[] for _ in range(n+1)]

for i in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

bfs(a, n)

