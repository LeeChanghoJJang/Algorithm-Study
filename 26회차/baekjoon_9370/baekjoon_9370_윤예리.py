import heapq
import sys
input = sys.stdin.readline

def solution(start):
    distance = [10e10] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    end = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for i in range(t):
        end.append(int(input()))

    S = solution(s)
    G = solution(g)
    H = solution(h)

    result = []
    for e in end:
        if S[g] + G[h] + H[e] == S[e] or S[h] + H[g] + G[e] == S[e]:
            result.append(e)

    result.sort()
    for r in result:
        print(r, end=' ')