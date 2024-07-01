import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x):
    visited[x] = 1
    dp[x][1] = 1
    dp[x][0] = 0

    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)
            dp[x][1] += min(dp[i][0], dp[i][1])     # 자기가 얼리어답터인 경우
            # 자식이 얼리어답터인 경우와 아닌 경우를 나눠서 작은 값 더하기
            dp[x][0] += dp[i][1]    # 자기가 얼리어답터가 아닌 경우
            # 자식이 무조건 얼리어답터야 하므로 그냥 더해주기

n = int(input())
graph = [[] for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
dfs(1)
print(min(dp[1][0], dp[1][1]))