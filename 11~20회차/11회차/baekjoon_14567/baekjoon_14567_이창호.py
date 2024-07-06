import sys
sys.stdin = open('input.txt')

from collections import defaultdict,deque

def topological_sort(graph):
    # 모든 노드의 진입차수를 계산
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    # 진입차수가 0인 노드를 큐에 추가
    queue = deque([(node,1) for node in graph if indegree[node] == 0])

    # 결과를 담을 리스트
    result = {i:0 for i in range(1,N+1)}

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드를 꺼내 결과에 추가
        node, cnt = queue.popleft()
        result[node] = cnt

        # 현재 노드에 연결된 모든 노드의 진입차수를 감소시키고, 0이 되면 큐에 추가
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append((neighbor,cnt+1))

    return result

N,M = map(int,input().split())
graph = {i:[] for i in range(1,N+1)}
for i in range(M):
    first,end = map(int,input().split())
    graph[first].append(end)

# 위상 정렬 실행
print(*topological_sort(graph).values())


