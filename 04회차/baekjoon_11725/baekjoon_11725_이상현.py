from collections import deque

# 백준 11752번 트리의 부모 찾기

# 트리의 루트가 1일 때, 각 노드의 부모를 구하는 문제
# bfs를 이용하여 접근
def bfs(vertex, graph):
    q = deque()
    q.append(vertex)

    # 인덱싱을 편하게 해주기 위해 (N + 1) 개의 요소
    # 방문여보 + 부모 노드의 번호를 저장하는 리스트
    result = [1, 1] + [0] * (N - 1)
    
    while q:
        # temp는 현재 정점의 위치
        temp = q.popleft()
        
        # 만약 인근 정점 중에 방문하지 않은 곳이 있다면
        # 그 정점은 현재 정점의 자식 노드이므로 result에 반영
        for v in graph[temp]:
            if not result[v]:
                result[v] = temp
                q.append(v)
            
    # 문제의 조건에 따라 1번 노드는 제외하고 반환
    return result[2:]
    
N = int(input())
graph = [[] for _ in range(N + 1)]

# 양 방향 간선
for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
[print(i) for i in bfs(1, graph)]