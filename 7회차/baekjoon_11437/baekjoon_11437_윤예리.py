import sys
sys.setrecursionlimit(500000)

# depth 계산 함수
def dfs(i, depth):
    d[i] = depth
    visited[i] = 1

    for j in graph[i]:
        if visited[j]:
            continue
        par[j] = i
        dfs(j, depth+1)

# 공통 조상 찾기
def lca(a, b):
    # depth 맞춰주고
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = par[a]
        else:
            b = par[b]
    
    # 공통 조상 찾을 때 까지 부모 타고 가기
    while a!= b:
        a = par[a]
        b = par[b]

    return a

n = int(input())
par = [0] * (n+1)
d = [0] * (n+1)     # depth
visited = [0] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))