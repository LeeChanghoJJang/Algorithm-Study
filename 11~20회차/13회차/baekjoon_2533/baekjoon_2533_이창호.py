import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**7)

# dp를 dfs로 채우기
def dfs(node):
    for next in graph[node]:
        # 방문안한 노드인 경우에만
        if not visited[next]:
            visited[next] = 1
            # 자식 노드로 간다.
            dfs(next)
            # 현재 얼리어답터가 아닐경우에는 자식노드가 얼리어답터여야 함
            dp[node][0] += dp[next][1]
            # 전에 얼라어답터든 아니든 노상관이기 때문에 둘중 작은 갯수를 저장
            dp[node][1] += min(dp[next])

N = int(input())
graph = [[] for _  in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# 노드가 얼리어답터가 아니면 0번노드, 얼리어답터면 1번노드에 누적 얼리어답더 저장
dp = [[0,1] for _ in range(N+1)]
visited = [0] * (N+1)
visited[1]=1
dfs(1)
print(min(dp[1]))

