import sys
input = sys.stdin.readline
from heapq import *

n = int(input())
office = []

for _ in range(n):
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start
    heappush(office, (end, start))

d = int(input())

tmp = []
cnt = 0
result = 0
while office:
    end, start = heappop(office)
    if start >= end-d:
        heappush(tmp, (start, end))
        cnt += 1
    while tmp:
        s, e = heappop(tmp)
        if s < end-d:
            cnt -= 1
        else:
            heappush(tmp, (s, e))
            break
    result = max(result, cnt)
print(result)