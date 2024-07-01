from collections import deque

def bfs(start):
    q = deque()  # 큐 생성
    q.append((0, start))  # 시작 노드와 깊이(거리) 0을 큐에 삽입
    visited = [False] * (n + 1)  # 방문 여부를 저장할 리스트 초기화
    visited[start] = True  # 시작 노드 방문 표시

    while q:  # 큐가 빌 때까지 반복
        depth, vertex = q.popleft()  # 큐에서 노드와 깊이 추출

        for v in graph[vertex]:  # 현재 노드와 연결된 모든 노드에 대해 탐색
            if visited[v] or depth > 1:  # 이미 방문한 노드거나, 깊이가 1 이상인 경우 건너뜀
                continue
            visited[v] = True  # 방문 표시
            q.append((depth + 1, v))  # 다음 노드와 깊이(거리)를 큐에 추가

    # 방문한 노드의 개수를 세고, 시작 노드는 제외함
    return sum(visited) - 1

n = int(input())  # 노드의 개수 입력
m = int(input())  # 간선의 개수 입력
graph = [[] for _ in range(n + 1)]  # 그래프 초기화

# 간선 정보 입력받아 그래프 구성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 양방향 그래프이므로 양쪽 노드에 간선 추가
    graph[b].append(a)

# BFS 수행 결과 출력
print(bfs(1))
