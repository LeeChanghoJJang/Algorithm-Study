import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

link = {i:[] for i in range(N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

que = deque([1])
visited = [0] * (N+1)
visited[1] = 1
result = 0
while que:
    now = que.popleft()
    dist = visited[now]
    if dist > 2:
        continue

    for to in link[now]:
        if not visited[to]:
            que.append(to)
            visited[to] = dist + 1
            result += 1
print(result)
# print(visited)