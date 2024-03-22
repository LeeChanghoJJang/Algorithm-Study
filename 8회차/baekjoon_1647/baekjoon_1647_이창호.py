import sys
from heapq import *

# 입력을 파일에서 받아오도록 설정
sys.stdin = open('input.txt')

# 프림 알고리즘을 사용하여 최소 신장 트리의 가중치 합을 계산하는 함수
def spanning(visited):
    spanning_tree = []  # 최소 신장 트리의 간선 정보를 저장할 리스트
    min_heap = [(0, 1)]  # (가중치, 정점) 정보를 담을 최소 힙
    sum_cost = 0  # 최소 신장 트리의 가중치 합
    while min_heap:
        weight, start = heappop(min_heap)  # 최소 힙에서 가장 작은 가중치의 간선 추출
        if not visited[start]:  # 해당 정점이 아직 방문되지 않았다면
            visited[start] = 1  # 방문 표시
            heappush(spanning_tree, (-weight, start))  # 최소 신장 트리에 간선 정보 추가
            sum_cost += weight  # 가중치 누적
            for next, edge_weight in graph[start]:  # 현재 정점과 연결된 간선을 확인
                if not visited[next]:  # 연결된 정점이 방문되지 않았다면
                    heappush(min_heap, (edge_weight, next))  # 최소 힙에 간선 정보 추가
    return sum_cost + heappop(spanning_tree)[0]  # 최소 신장 트리의 가중치 합 반환

# 입력 받기
N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}  # 그래프 초기화
for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))  # 간선 정보 추가
    graph[end].append((start, cost))  # 양방향 그래프이므로 반대 방향으로도 추가

# 최소 신장 트리의 가중치 합 출력
print(spanning([0] * (N + 1)))
