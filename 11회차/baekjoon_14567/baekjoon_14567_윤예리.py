import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)   # 진입 차수

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = deque([])
# 진입 차수가 0인 것들 q에 삽입
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append([i, 1])

result = [0] * (n+1)
while q:
    node, cnt = q.popleft()
    result[node] = cnt

    for next_ in graph[node]:
        # 진입 차수 1씩 빼주고
        in_degree[next_] -= 1
        # 0이 된 노드가 있으면 q에 삽입
        if in_degree[next_] == 0:
            q.append([next_, cnt+1])
print(*result[1:])