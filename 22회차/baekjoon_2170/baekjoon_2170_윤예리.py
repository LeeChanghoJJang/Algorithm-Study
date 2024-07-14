from heapq import *

import sys
input = sys.stdin.readline

n = int(input())

hq = []
for _ in range(n):
    x, y = map(int, input().split())
    heappush(hq, (x, y))

start, end = heappop(hq)
result = 0
while hq:
    new_start, new_end = heappop(hq)

    if end < new_start:
        result += end-start
        start = new_start
        end = new_end
    elif start < new_start and end <= new_end:
        end = new_end

result += end-start
print(result)
# print(start, end)