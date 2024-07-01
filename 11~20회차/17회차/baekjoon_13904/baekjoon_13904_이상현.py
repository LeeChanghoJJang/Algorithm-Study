from heapq import *

N = int(input())

hq = []
for i in range(N):
    d,w = map(int,input().split())
    heappush(hq,(-w,d))
result = {}

while hq:
    now, day = heappop(hq)
    for i in range(min(day,N),0,-1):
        if i not in result:
            result[i] = -now
            break
print(sum(result.values()))