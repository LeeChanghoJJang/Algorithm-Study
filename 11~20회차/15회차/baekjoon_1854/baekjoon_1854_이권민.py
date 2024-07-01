import sys
import heapq

input = sys.stdin.readline
INF = int(1e12)

# 1 ≤ n ≤ 1000, 0 ≤ m ≤ 2000000, 1 ≤ k ≤ 100
N, M, K = map(int, input().split())

# 거리, 위치
q = []
# a번 도시에서 b번 도시로 갈 때는 c의 시간이 걸린다. (1 ≤ a, b ≤ n. 1 ≤ c ≤ 1000)

distance = [[] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

heapq.heappush(distance[1], 0)  # 비용
heapq.heappush(q, (0, 1))       # 비용, 장소

while q:
    dist, now = heapq.heappop(q)
    for i in graph[now]:
        # i[0]: 비용, i[1]: 장소
        cost = dist + i[0]
        # 저장된 거리가 K보다 작을 때
        if len(distance[i[1]]) < K:
            # 그냥 넣기
            heapq.heappush(distance[i[1]], -cost)
            heapq.heappush(q, (cost, i[1]))
        # 저장된 거리가 K보다 크고
        # heapq의 가장 작은 값에 -1을 곱한 값보다 cost가 작을 때
        elif cost < -distance[i[1]][0]:
            # heapq에서 데이터 하나를 뺀다
            heapq.heappop(distance[i[1]])
            heapq.heappush(distance[i[1]], -cost)
            heapq.heappush(q, (cost, i[1]))

for i in range(1, N+1):
    if len(distance[i]) == K:
        print(-distance[i][0])
    else:
        print(-1)