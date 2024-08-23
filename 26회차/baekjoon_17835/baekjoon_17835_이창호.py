import sys
sys.stdin = open('input.txt')
from heapq import *
input =sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[] for i in range(n+1)]

# 역방향 그래프
for _ in range(m):
    a,b,w = map(int,input().split())
    graph[b].append((a,w))

# 면접장
data = [*map(int,input().split())]
check = [0]*(n+1); hq = []

# 프림의 원리를 이용
# 면접장 다음 도시부터 힙에 저장
for a in data:
    check[a] = 1
    for b,w in graph[a]:
        heappush(hq,(w,-b))

# 변수의 초기값 설정
now,w = -1,0
for _ in range(n-k):
    while 1:
        w,now = heappop(hq)
        if check[-now]:
            continue
        break
    check[-now] = 1
    for next,w1 in graph[-now]:
        heappush(hq,(w+w1,-next))
print(-now);print(w)