import heapq

n, m, r = map(int, input().split()) # 지역 개수, 수색 범위, 길 개수
t = list(map(int, input().split())) # 구역 템 개수
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

result = 0
for i in range(1, n+1):     # 지역을 순회하면서
    distance = [float('INF')] * (n+1)
    q = []

    heapq.heappush(q, (0, i))
    distance[i] = 0

    while q:
        current_dist, current_node = heapq.heappop(q)

        if current_dist > distance[current_node]:   # 앞 순서 노드는 이미 봤으므로 패스
            continue

        for neighbor in graph[current_node]:
            new_distance = current_dist + neighbor[1]

            if new_distance < distance[neighbor[0]]:
                distance[neighbor[0]] = new_distance
                heapq.heappush(q, (new_distance, neighbor[0]))

    tmp = 0
    for i, d in enumerate(distance):  
        if d <= m:          # 갈 수 있으면
            tmp += t[i-1]
    if tmp > result:
        result = tmp
print(result)