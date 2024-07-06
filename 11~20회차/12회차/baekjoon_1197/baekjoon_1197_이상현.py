from heapq import *

def prim(start):
    # 시작 정점을 포함한 연결된 정점들
    connected = {start}
    # 아직 연결되지 않은 간선들을 저장할 힙
    unconnected = [(w, e) for e, w in graph[start]]
    heapify(unconnected)  # 힙 속성 유지
    sum_ = 0  # MST의 가중치 합

    while unconnected:
        weight, vertex = heappop(unconnected)  # 최소 가중치 간선 선택

        if vertex in connected:  # 이미 연결된 정점이면 패스
            continue

        connected.add(vertex)  # 연결된 정점으로 추가
        sum_ += weight  # 가중치 합 갱신

        # 새로 연결된 정점에 대해 연결된 간선들을 힙에 추가
        for v, w in graph[vertex]:
            if v in connected:  # 이미 연결된 정점이면 패스
                continue
            heappush(unconnected, (w, v))  # 연결되지 않은 간선 추가

    return sum_  # MST의 가중치 합 반환

# 정점의 개수 V와 간선의 개수 E 입력
V, E = map(int, input().split())
# 그래프 초기화
graph = [[] for _ in range(V + 1)]

# 간선 정보 입력받아 그래프에 추가
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))  # 양방향 그래프이므로 양쪽 정점에 간선 추가
    graph[B].append((A, C))

# 프림 알고리즘 수행하여 MST의 가중치 합 출력
print(prim(1))
