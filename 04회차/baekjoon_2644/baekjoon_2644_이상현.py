from collections import deque

# 백준 2644번 촌수계산

# 입력으로 주어지는 두 사람의 촌수를 구하는 문제
def bfs(start, end, graph):
    q = deque()
    q.append((start, 0))

    # 인덱싱을 편하게 하기 위해 (n + 1)개의 요소를 가지는
    # visited 리스트 생성
    visited = [0] * (n + 1)
    visited[start] = 1

    while q:
        # vertex는 현재 사람, cnt는 start와 vertex 간의 촌수
        vertex, cnt = q.popleft()

        # 만약 vertex가 우리가 찾는 사람이라면 반복문 종료
        if vertex == end:
            break

        # 현재 사람의 친척 관계를 탐색
        for v in graph[vertex]:
            # 만약 조사하지 않은 사람이 있다면
            # cnt(촌수)를 1 증가시키고 큐에 추가
            if not visited[v]:
                q.append((v, cnt + 1))
                visited[v] = 1

    # 만약 우리가 찾는 사람을 방문했다면 촌수를, 아니라면 -1을 반환
    return cnt if visited[end] else -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

# 양방향 간선
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(start, end, graph))