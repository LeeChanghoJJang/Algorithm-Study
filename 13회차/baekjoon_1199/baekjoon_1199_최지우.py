import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
link = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]
for i in range(N):
    if sum(link[i])%2 == 1: exit(print(-1))
    for j in range(i):
        if link[i][j]:
            graph[i].append(j)
            graph[j].append(i)

route = [0]
while route:
    cur = route[-1]
    while graph[cur]:
        to = graph[cur][-1]
        if link[cur][to]: break

        graph[cur].pop()

    if graph[cur]:
        route.append(to)
        link[cur][to] -= 1
        link[to][cur] -= 1
    else:
        route.pop()
        print(cur +1, end=' ')