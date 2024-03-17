import sys
from collections import deque

input = sys.stdin.readline

N,M,K,X = map(int,input().split())  
tree = [[] for _ in range(N+1)]
visit = [0] * (N+1)
for _ in range(M):
    i,j = map(int,input().split())
    tree[i].append(j)

q = deque([X])

visit[X] =1

while q:                                # bfs를 통해 모든 거리 계산
    s = q.popleft()
    for item in tree[s]:
        if visit[item] == 0 :
            visit[item] = visit[s]+1
            q.append(item)
ans = []

for i in range(N+1):
    if visit[i]-1 == K:
        ans.append(i)
if not ans :
    print(-1)
else :
    for i in ans:                       # 출력
        print(i)