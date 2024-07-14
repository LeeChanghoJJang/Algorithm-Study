import sys
from heapq import *
sys.stdin = open('input.txt')

n = int(input())
heap =[]
for _ in range(n):
    a,b = map(int,input().split())
    heappush(heap,(a,b))
result = 0
start, end = float('-inf'),float('-inf')
while heap:
    a,b = heappop(heap)
    if start == end == float('-inf'):
        start = a; end = b
    elif start <= a <= end:
        end = max(end,b)
    elif end < a:
        result += end- start
        start = a; end = b

result += end - start
print(result)