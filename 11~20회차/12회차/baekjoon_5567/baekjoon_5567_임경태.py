# 5567 결혼식

from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
dist = [1, 1] + [0] * (n-1)
Q = deque([1])
cnt = 0

# 그래프 제작
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 너비우선탐색
while Q:
    now = Q.popleft()

    # 친구의 친구까지만 허용
    if dist[now] == 3:
        continue

    # 그래프 순회
    for next in graph[now]:
        if not dist[next]:
            dist[next] = dist[now] + 1
            Q.append(next)
            cnt += 1

print(cnt)