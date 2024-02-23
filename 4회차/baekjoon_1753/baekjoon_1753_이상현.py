import sys
input = sys.stdin.readline

import heapq

# 백준 1753번 최단경로

# 시작점으로부터 각 점까지의 최소 경로값을 구하는 문제
# 최소 경로값을 pop하기 위해서 heapq 라이브러리 사용
def dijkstra(start, graph):
    dist_[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        # current_dist는 현재까지의 거리(경로값), current_vertex는
        # 현재 정점을 나타냄
        current_dist, current_vertex = heapq.heappop(q)

        # 만약 현재까지 경로값이 원래 저장돼 있는 최소 경로값보다
        # 크다면 다음 반복문으로 넘어감
        if current_dist > dist_[current_vertex]:
            continue

        # 인근 정점 중에서 원래 저장돼 있는 최소 경로값보다
        # 지금 정점을 거쳐 가는게 경로값이 더 작다면 새로 갱신 후
        # 탐색을 위해 q에 추가
        for weight, nbd in graph[current_vertex]:
            distance = current_dist + weight

            if distance < dist_[nbd]:
                dist_[nbd] = distance
                heapq.heappush(q, (distance, nbd))

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
inf = 10 ** 6
dist_ = [inf] * (V + 1)

# 단방향 간선
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dijkstra(K, graph)

# 만약 연결되어 있다면 최단 경로의 경로값을 출력,
# 아니라면 INF를 출력
for x in range(1, V + 1):
    if dist_[x] != inf:
        print(dist_[x])
    else:
        print('INF')