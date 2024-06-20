from sys import stdin
input = stdin.readline

def bf():                                                 # 벨만-포드
    for i in range(n):                                    # 전체를 순회하면서
            for j in range(len(edges)):                     
                  cur, next, cost = edges[j]              # 각 간선에서
                  if dist[next] > dist[cur] + cost:       # 도착지가 출발지 + 비용보다 낮다면
                        dist[next] = dist[cur] + cost     # 도착지의 값을 그 비용으로 돌림
                        if i == n - 1:                    # 모든 n에 대해 가능하다면 (음수로 무한 루프가 가능하다면)
                              return True                 # True 반환
    return False
                        
TC = int(input())


for _ in range(TC):
      n, m, w = map(int, input().split())
      edges = []
      dist = [1e9] * (n + 1)
      for i in range(m + w):
            s, e, t = map(int, input().split())
            if i >= m:
                  t = -t
            else:
                  edges.append((e, s, t))
            edges.append((s, e, t))
      if bf():
            print("YES")
      else:
            print("NO")