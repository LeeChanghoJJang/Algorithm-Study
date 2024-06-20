import heapq

def dijkstra(graph, start):
    distance = [float('INF')] * (n+1)
    distance[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distance[current_node]:
            continue

        for neighbor in graph[current_node]:
            new_distance = current_dist + 1

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distance

n, m, k, x = map(int, input(). split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = dijkstra(graph, x)
if k not in result:
    exit(print(-1))

for i in range(n+1):
    if result[i] == k:
        print(i)

