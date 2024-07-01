import sys
from heapq import *

sys.stdin = open('input.txt')
N = int(input())

heap = []
for i in range(N):
    d,w = map(int,input().split())
    heappush(heap,(-w,d))
result = [0] * (N+1)

while heap:
    now, day = heappop(heap)
    for i in range(min(day,N),0,-1):
        if result[i] == 0:
            result[i] = -now
            break
print(sum(result))