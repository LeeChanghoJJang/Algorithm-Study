import sys
sys.stdin = open('input.txt')
import heapq
INF = int(1e9)  # 못 가는 길 weight = 무한

V, e = map(int, input().split())    # 노드 수, 엣지 수
k = int(input())    # 시작 노드
graph = [[] for i in range(V+1)]    # 연결 정보
distnace = [INF] * (V+1)    # 다 못간다고 가정해놓고 input 받으면 하나씩 채울거임

for i in range(e):  # edge 채우기
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # q = [(0, 1)], 초기값 설정
    distnace[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distnace[now] < dist:
            continue
        for i in graph[now]:    # i = 갈 수 있는 다른 노드 리스트
            cost = dist + i[1]
            if cost < distnace[i[0]]:
                distnace[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)
for i in range(1, V+1):
    if distnace[i] == INF:
        print('INF')
    else:
        print(distnace[i])