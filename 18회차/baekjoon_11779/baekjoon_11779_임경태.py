# 11779 최소비용 구하기 2
from heapq import heappop, heappush

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
costs = [float('inf')] * (N+1)
prev = [0] * (N+1)

# 그래프 제작
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

S, E = map(int, input().split())

# 초기 설정
Q = [(0, S)]
costs[S] = 0

# 다익스트라
while Q:
    now_cost, now = heappop(Q)

    # 현재 비용 비교
    if costs[now] < now_cost: continue

    # 그래프 순회
    for next, next_cost in graph[now]:
        cost = now_cost + next_cost

        # 다음 비용 비교
        if costs[next] <= cost: continue

        # 비용 및 경로 업데이트
        costs[next] = cost
        prev[next] = now
        heappush(Q, (cost, next))

# 경로 역추적
path = []
now = E
while now:
    path.append(now)
    now = prev[now]

# 출력
print(costs[E])
print(len(path))
print(*reversed(path))