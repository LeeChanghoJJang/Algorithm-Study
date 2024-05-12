import sys
from heapq import *
sys.stdin = open('input.txt')

# N : 도시 개수 / M : 도로 개수 /  K :  k번째 최단경로
N, M, K = map(int, input().split())
graph = [[] for i in range(N+1)]

# 간선과 가중치를 그래프에 추가합니다.
for _ in range(M):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))

# 초기값 : 가중치 0, 1번 도시부터 시작
heap = [(0, 1)]

# 시작 노드로부터 다른 모든 노드까지의 거리를 저장하기 위한 리스트의 리스트를 초기화합니다.
distance = [[] for i in range(N+1)]

# 다익스트라 알고리즘을 사용하여 노드 1에서 다른 모든 노드로의 K번째 최단 경로를 찾습니다.
while heap:
    # 우선순위 큐에서 거리가 가장 짧은 도시를 탐색합니다. (처음은 시작점)
    w, now = heappop(heap)
    # 현재 노드까지 찾은 경로가 K개일 경우
    if len(distance[now]) == K:
        # 현재 거리가 K번째 최장 거리보다 크거나 같다면
        if w >= -distance[now][0]:
            continue  # 반복문의 다음 단계로 넘어갑니다.
        heappop(distance[now])  # 현재 노드의 K번째 최장 거리를 리스트에서 제거합니다.
    # 현재 노드까지의 거리의 음수 값을 현재 노드의 거리 리스트에 추가합니다.
    heappush(distance[now], -w)
    # 현재 노드의 이웃을 탐색하고 거리를 업데이트합니다.
    for next, w1 in graph[now]:
        heappush(heap, (w + w1, next))  # 새로운 거리와 이웃 노드를 우선순위 큐에 추가합니다.

# 노드 1로부터 각 노드까지의 K번째 최단 거리를 출력합니다.
for i in range(1, N+1):
    print(-1 if len(distance[i]) < K else -distance[i][0])
