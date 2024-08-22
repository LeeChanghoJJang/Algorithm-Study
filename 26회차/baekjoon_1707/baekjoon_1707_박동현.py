import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 이분 그래프 구성을 위해 group을 -1/1로 나눔
def DFS(now, group=1):
    visit[now] = group

    for nxt in graph[now]:
        if not visit[nxt]:
            res = DFS(nxt, -group)
            if not res:
                return False
        else:
            if visit[nxt] == group:
                return False
    return True


for _ in range(int(input())):
    N,M = map(int,input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = [0] * (N+1)
    for i in range(1, N+1):
        if not visit[i]:
            res = DFS(i)
            if not res:
                break
    print("YES" if res else "NO")
