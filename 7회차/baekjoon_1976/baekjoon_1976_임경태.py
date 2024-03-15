# 1976 여행 가자 (골드4)

from collections import deque

N = int(input()); input()
graph = [[] for _ in range(N)] 
for i in range(N):
    for j, v in enumerate(input().split()):
        if v == '1': graph[i].append(j)

seq = list(map(int, input().split()))
visit = [0] * N

Q = deque([seq[0] - 1])
while Q:
    now = Q.popleft()
    for next in graph[now]:
        if not visit[next]: Q.append(next)
    visit[now] = 1

if all(visit[city - 1] for city in seq): print('YES')
else: print('NO')

'''
34036KB / 68ms
'''