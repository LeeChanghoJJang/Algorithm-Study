import sys
sys.stdin = open('input.txt')
INF = int(1e9)
# 벨만포드 함수 정의
def bellman_ford(start,n):
    # 다익스트라와 같이 비용들을 저장한 배열 정의
    dist = [INF for i in range(n+1)]
    # 시작점은 비용이 없음
    dist[start] = 0
    # 모든 점을 순회함 
    for i in range(n):
        # 시작점, 도착점, 비용을 그래프에서 계속 순회한다.
        for s,e,t in graph:
            # 도착점의 비용이 시작점의 기존 비용 + 가는데 드는 비용보다 큰 경우에만 갱신
            if dist[e] > dist[s] + t:
                # n-1로 끊는 이유는 무한루프를 방지하기 위함
                # 끝까지 가도 계속 순환되고 있다는 것 자체로 출발 위치로 오는게 가능하다는 소리임
                if i==n-1:
                    return True
                dist[e] = dist[s] + t
    # 만약 저기서 끊기지 않고 반복문을 모조리 순회했다면 False 반환 
    return False

for _ in range(int(input())):
    n,m,w = map(int,input().split())
    graph = []
    for i in range(m):
        s,e,t = map(int,input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))
    for i in range(w):
        s, e, t = map(int, input().split())
        graph.append((s,e,-t))
    print(graph)
    tf = bellman_ford(1,n)
    if tf: print("YES")
    else: print("NO")
