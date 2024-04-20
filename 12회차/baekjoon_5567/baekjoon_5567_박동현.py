import sys
from collections import deque

input = sys.stdin.readline

N, M = int(input()), int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

start = 1

q = deque([start])
visit = [0] * (N+1)
visit[start] = 1
# 그냥 bfs
while q :
    now = q.popleft()

    for item in graph[now]:
        if not visit[item]:
            visit[item] = visit[now]+1
            q.append(item)

cnt = 0
for friend in visit:
    if 1 < friend <= 3:
        cnt += 1
print(cnt)