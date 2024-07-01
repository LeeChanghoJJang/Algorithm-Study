import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())

# 그래프를 인접 리스트로 생성
roads = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, fee = map(int, input().split())
    roads[start].append((end, fee))

start_city, end_city = map(int, input().split())

# 다익스트라 알고리즘을 사용한 최단 경로 탐색
def dijkstra(start, end):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    priority_queue = [(0, start)]
    parents = [-1] * (n + 1)
    # 이건뭐지
    
    while priority_queue:
        current_dist, current_city = heapq.heappop(priority_queue)
        
        if current_dist > distances[current_city]:
            continue
        
        for neighbor, weight in roads[current_city]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_city
                # 어디서 왔는지.
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # 최단 경로 복원
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parents[current]
    path.reverse()
    
    return distances[end], path

# 시작 도시에서 도착 도시까지의 최단 거리 및 경로를 계산
shortest_distance, shortest_path = dijkstra(start_city, end_city)

# 결과 출력
print(shortest_distance)
print(len(shortest_path))
print(' '.join(map(str, shortest_path)))
