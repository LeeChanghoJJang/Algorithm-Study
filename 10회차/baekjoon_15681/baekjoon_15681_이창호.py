import sys
sys.stdin = open('input.txt')  # input.txt 파일을 표준 입력으로 사용

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 설정합니다.

def dfs(node, parent):
    # 현재 노드의 서브트리 크기를 1로 초기화합니다.
    subtree_size[node] = 1
    # 현재 노드의 자식 노드에 대해 반복합니다.
    for child in graph[node]:
        # 부모 노드가 아닌 경우에 대해서만 재귀적으로 DFS를 수행합니다.
        if child != parent:
            dfs(child, node)
            # 자식 노드의 서브트리 크기를 현재 노드에 더합니다.
            subtree_size[node] += subtree_size[child]

# 입력값을 받습니다.
N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]  # 그래프를 나타내는 리스트를 초기화합니다.
subtree_size = [0] * (N+1)  # 각 노드의 서브트리 크기를 저장할 리스트를 초기화합니다.

# 그래프 정보를 입력받습니다.
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(R, -1)  # 루트 노드 R을 시작으로 DFS를 수행하여 각 노드의 서브트리 크기를 계산합니다.

# 각 쿼리에 대해 서브트리 크기를 출력합니다.
for _ in range(Q):
    query = int(input())
    print(subtree_size[query])
