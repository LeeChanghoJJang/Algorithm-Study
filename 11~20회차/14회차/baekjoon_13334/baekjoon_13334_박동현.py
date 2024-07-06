import sys
from heapq import heappop, heappush
input = sys.stdin.readline


N = int(input())
arr = sorted([ sorted([*map(int,input().split())]) for _ in range(N) ], key=lambda x: (x[1],x[0]))
dist = int(input())

hq = []
ans = 0 

for i in arr :
    start, end = i
    heappush(hq, start)
    # 끝에서 선분의 최대 거리를 계산
    start_point = end-dist
    # 그 최대 거리 보다 짧다면
    while hq and hq[0] < start_point:
        # 팝
        heappop(hq)
    # 길이 계산
    ans = max(ans, len(hq))

print(ans)