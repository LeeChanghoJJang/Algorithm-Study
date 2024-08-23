# 1707 이분 그래프

def DFS(start, visited, graph, group):
    # 현재 노드를 방문하면서 그 노드를 group(1 또는 -1)으로 표시
    visited[start] = group

    # 현재 노드와 연결된 모든 노드들 확인
    for v in graph[start]:
        # 만약 연결된 노드가 아직 방문되지 않았다면
        if visited[v] == 0:
            if not DFS(v, visited, graph, -group):
                return False
        # 이미 방문된 노드가 현재 노드와 같은 그룹이라면 이분 그래프가 아님
        elif visited[v] == group:
            return False

    return True

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    # 간선 정보를 입력받아 그래프 구축
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 그래프의 모든 정점을 순회하면서 방문하지 않은 노드에서 DFS 시작 (끊어져있는 경우 포함)
    for i in range(1, V+1):
        if visited[i] == 0:
            result = DFS(i, visited, graph, 1)
            if not result:
                break

    # DFS 결과에 따라 해당 그래프가 이분 그래프인지 판단하여 출력
    print("YES" if result else "NO")
