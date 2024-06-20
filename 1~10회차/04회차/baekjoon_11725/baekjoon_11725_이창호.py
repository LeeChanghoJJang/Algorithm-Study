import sys
sys.stdin = open('input.txt')
# 첫번째 방법 : 트리 이용(시간초과)
N = int(input())
# 인덱스를 기준으로 연결정보 저장하기 위해 connection 정의
connection = [[] for _ in range(N+1)]
# 문제에서 주어진 두 연결정점 정보 저장
trees = [list(map(int,input().split())) for i in range(N-1)]
visited = [0] *(N+1)
stack = [1]
# 정점 노드 1번부터 연결된 정보 저장
while stack:
    now = stack.pop()
    visited[now] = 1
    # 인덱스를 자식으로, 값을 부모로 저장
    for i,j in trees:
        if i == now and not visited[j]:
            connection[j].append(i)
            stack.append(j)
        elif j ==now and not visited[i]:
            connection[i].append(j)
            stack.append(i)
for i in range(2,N+1):
    print(*connection[i])

# 두번째 방법 :재귀 이용 (70428KB 372ms)
import sys
sys.setrecursionlimit(10**6)
# 주어진 node에서 각 자식노드를 찾고, 부모 리스트에 자식을 인덱스로 부모를 저장
def dfs(node, parent, connection, visited):
    visited[node] = 1
    for child in connection[node]:
        if not visited[child]:
            parent[child] = node
            dfs(child, parent, connection, visited)

N = int(input())
connection = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
parent = [0] * (N + 1)
# 입력된 정보를 connection에 저장해서 부모 리스트를 축출하기 위함
for _ in range(N - 1):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)

dfs(1, parent, connection, visited)
print(parent)
for i in range(2, N + 1):
    print(parent[i])
