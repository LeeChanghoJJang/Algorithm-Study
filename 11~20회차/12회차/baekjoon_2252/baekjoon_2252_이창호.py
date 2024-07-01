import sys
sys.stdin = open('input.txt')
from collections import defaultdict, deque

def topological_sort(graph):
    # 진입 차수 계산
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    # 진입 차수가 0인 노드를 큐에 삽입
    queue = deque([node for node in graph if in_degree[node] == 0])

    # 결과를 담을 리스트
    result = []

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드를 꺼내 결과에 추가
        node = queue.popleft()
        result.append(node)

        # 해당 노드와 연결된 모든 노드의 진입 차수를 감소시키고, 0이 되면 큐에 추가
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 사이클이 있는 경우에는 모든 노드를 방문하지 못하므로 None 반환
    if len(result) != len(graph):
        return None
    return result


# 그래프 정의 (인접 리스트 형태)
N,M = map(int,input().split())
graph = {i: [] for i in range(1,N+1)}
for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)

# 위상 정렬 수행
result = topological_sort(graph)
print(*result)
