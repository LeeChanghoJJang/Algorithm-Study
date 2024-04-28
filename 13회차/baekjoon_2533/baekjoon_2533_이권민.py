# 깊이로 계산. h//2. 분기 될때마다 중복 제거를 위해 따로 처리 필요. 자식 노드에 저장된 값으로
# 계산하면 될듯. 자식 개수. 분기 될때 
# 1 2, 1 3/ 1개. 2 4 2개, 3 5 3 6 2개, 4 7 4 8 4 9 3개 
# 부모 자식중 하나만 얼리 어답터면 ㄱㅊ
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(node):
    for next in graph[node]:
        # 양방향. 부모가 아니면. 자식노드면 해당 노드의 dp값은 다 [0,1]
        # 넣거나 안넣거나.
        if not visited[next]:
            visited[next] = 1
            dfs(next)
            dp[node][0] += dp[next][1]
            # 지금 node가 아니면 자식노드가 얼어 일때의 값
            dp[node][1] += min(dp[next])
            # 지금 node가 얼어, 자식노드가 뭐든 상관 없.
        
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
# 지금 노드가 얼어일때랑 아닐때. 
dp = [[0,1] for _ in range(n+1)]
visited = [0]*(n+1)
visited[1] = 1
dfs(1)
print(min(dp[1]))

# import sys
# input = sys.stdin.readline

# N = int(input())

# link = {i: [] for i in range(1, N+1)}

# for _ in range(N-1):
#     a, b = map(int, input().split())
#     link[a].append(b)
#     link[b].append(a)

# visited = [0] * (N+1)
# start = []
# for i in link:
#     if len(link[i]) == 1:
#         start.append(i)
## 자식 노드 일 때.

# while start:
#     v = start.pop()
#     for x in link[v]:
#         for y in link[x]:
#             link[y].remove(x)
#             if len(link[y]) == 1:
#                 start.append(y)
## 중복제거인듯.
#         visited[x] = 1
#         link[x] = []
# print(visited.count(1))