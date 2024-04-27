# 14938 서강그라운드 (골드4)

from heapq import heappush, heappop

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

# 양방향 그래프 제작
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

ans, Q = 0, []
INF = float('inf')

# 시작 지점을 바꾸어가며 탐색
for i in range(1, n+1):
    heappush(Q, [i, 0]); dist = [INF] * (n+1); dist[i] = 0

    # 다익스트라
    while Q:
        now, w = heappop(Q)
        if dist[now] < w: continue
        for next, next_w in graph[now]:
            cost = w + next_w
            if dist[next] > cost:
                dist[next] = cost; heappush(Q, [next, cost])

    # 갈 수 있는 곳의 점수 합산
    ans = max(ans, sum(item[i-1] for i in range(n+1) if dist[i] <= m))

print(ans)

'''
33188KB / 52ms
'''