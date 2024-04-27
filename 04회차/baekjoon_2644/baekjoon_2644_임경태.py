# 2644 / 촌수계산 / 실버2

from collections import deque

N = int(input())  # 사람 수
p1, p2 = map(int, input().split())  # 목표 관계
M = int(input())  # 관계 수
rel = [[] for _ in range(N+1)]  # 관계
dist = [0] * (N+1)  # 촌수

# 무방향 그래프 제작
for _ in range(M):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

# BFS
Q = deque([p1])
while Q:
    now = Q.popleft()
    if now == p2:
        break
    for next in rel[now]:
        if not dist[next]:
            dist[next] = dist[now] + 1
            Q.append(next)
else:
    dist[p2] = -1

print(dist[p2])

'''
34068KB / 60ms
'''