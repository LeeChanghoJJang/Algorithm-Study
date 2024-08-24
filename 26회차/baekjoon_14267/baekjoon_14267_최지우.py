import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
line = list(map(int, input().split()))
link = {i: [] for i in range(1, N+1)}

# 1번이 사장, 0번 안씀
for i, n in enumerate(line):
    if n == -1:
        continue
    link[n].append(i+1)

cc = [0] * (N+1)
for _ in range(M):
    i, w = map(int, input().split())
    cc[i] += w

res = [0] * (N)

def bfs(start):
    q = deque([start])
    while q:
        now = q.popleft()
        
        for to in link[now]:
            res[to-1] = res[now-1] + cc[to]
            q.append(to)

bfs(1)
print(*res)
