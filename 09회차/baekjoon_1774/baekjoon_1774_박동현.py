import sys
from math import sqrt
from heapq import heappop,heappush

input = sys.stdin.readline
N,M = map(int,input().split())


god = [(0,0)]+[tuple(map(int,input().split())) for _ in range(N)]           # 좌표 보정을 위해 앞에 (0,0) 설정

graph = [set() for _ in range(N+1)]                                         # 그래프를 set로 받아서, 뒤에 양방향으로 더할 때 중복 제거

already = [tuple(map(int,input().split())) for _ in range(M)]               # 이미 이어져 있는 길의 경우 아래에서 0 으로 길의 거리를 수정


for i in range(1,N+1):
    for j in range(1,N+1):

        if (i,j) in already :
            dist = 0
        else :
            dist = round(sqrt((god[i][0] - god[j][0])**2 + (god[i][1] - god[j][1])**2),5)   # 2차원 좌표 거리 (일단 넉넉하게 5자리까지)

        graph[i].add((j,dist))
        graph[j].add((i,dist))

# prim 알고리즘
start = 1
hq = [(0,start)]
visit = [False] * (N+1)

ans = 0
while hq :
    dist_now, now = heappop(hq)

    if not visit[now] :
        visit[now] = True
        ans += dist_now
        for next,cost in graph[now]:
            heappush(hq,(cost,next))

# 소수점 2자리까지 계산
print(f"{ans:.02f}")