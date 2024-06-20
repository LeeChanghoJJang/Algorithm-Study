# 1865 웜홀

import sys 
sys.stdin = open('input.txt') 

# 풀이1 : 정석 벨만-포드

def bellman_ford(start):
    global is_cycle
    dist[start] = 0
    # 전체 N번의 라운드 반복
    # N-1번까지 모든 정보가 업데이트됨 N번째부터는 음수순환이 아니라면 불변해야함
    for i in range(N):  
        for s, e, t in graph:  # 매 반복마다 모든 간선 확인
            if dist[s] != float('inf') and dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                # N번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == N - 1: is_cycle = True; return

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    graph, dist = [], [float('inf')] * (N+1)
    is_cycle = False

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph.append([S, E, T])
        graph.append([E, S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        graph.append([S, E, -T])
    
    for i in range(1, N + 1):
        if dist[i] == float('inf'):
            bellman_ford(i)

    print('YES' if is_cycle else 'NO')

'''
    <벨만-포드(Bellman-Ford) 알고리즘>
    - 음수값이 포함된 가중 유향 그래프에서 최단 경로 문제를 푸는 알고리즘
    - 다익스트라(Dijkstra) 알고리즘은 빠르지만 음수인 경우는 처리 불가
    - 시간 복잡도 : V(노드), E(간선)
        - 벨만-포드 : O(VE)
        - 다익스트라 : O(ElogV)
    - 알고리즘
        1. 출발 노드 설정
        2. 최단 거리 테이블 초기화
        3. 다음의 과정 N-1번 반복
          (1) 전체 간선 E개를 하나씩 확인
          (2) 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
        만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번 과정 한번 더 수행
        최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것
'''

# 풀이2 : 플로이드-워셜 (보류)

def floyd_warshall():
    # 플로이드-워셜 알고리즘 수행
    for k in range(N):  # 중간 노드
        for i in range(N):  # 시작 노드
            if k == i:
                continue
            for j in range(N):  # 마지막 노드
                # 중간을 거쳐가는게 더 빠르면 갱신
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                if dist[i][i] < 0: return "YES"
    return "NO"

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    dist = [[float('inf')] * N for _ in range(N)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        dist[S-1][E-1] = min(dist[S-1][E-1], T)
        dist[E-1][S-1] = min(dist[E-1][S-1], T)

    for _ in range(W):
        S, E, T = map(int, input().split())
        dist[S-1][E-1] = min(dist[S-1][E-1], -T)

    print(floyd_warshall())

'''
    <플로이드-워셜(Floyd-Warshall) 알고리즘>
    - 변의 가중치가 음이거나 양인 가중 그래프에서 최단 경로들을 찾는 알고리즘
    - 각각의 꼭짓점 쌍을 지나는 그래프의 모든 경로를 비교함

'''