import sys
sys.setrecursionlimit(10 ** 5)

def dfs(vertex):
    dp[vertex] = 1

    for v in graph[vertex]:
        if not dp[v]:
            dfs(v)
            dp[vertex] += dp[v]

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dp = [0] * (N + 1)

for _ in range(N - 1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

dfs(R)

for _ in range(Q):
    U = int(input())
    print(dp[U])