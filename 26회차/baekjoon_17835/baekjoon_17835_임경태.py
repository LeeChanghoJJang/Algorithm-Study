# 17835 면접보는 승범이네
import heapq

N, M, K = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    a, b, cost = map(int, input().split())
    arr[b].append([a, cost])

targets = list(map(int, input().split()))


def dijkstra():
    Q = []

    for t in targets:
        heapq.heappush(Q, [0, t])
        result[t] = 0

    while Q:
        now_cost, city = heapq.heappop(Q)

        if result[city] < now_cost:
            continue

        for next_city, next_cost in arr[city]:
            cost = now_cost + next_cost

            if cost < result[next_city]:
                result[next_city] = cost
                heapq.heappush(Q, [cost, next_city])


max_start, max_cost = 0, 0
result = [int(1e11)] * (N+1)

dijkstra()

for i, r in enumerate(result):
    if r > max_cost and r != int(1e11):
        max_start, max_cost = i, r

print(max_start)
print(max_cost)