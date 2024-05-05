import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
arr = [list(sorted(map(int, input().split()))) for _ in range(N)]
d = int(input())

arr.sort(key=lambda x:(x[1], x[0]))
heap = []
result = 0
for h, o in arr:
    heappush(heap, h)
    start = o - d
    while heap and heap[0] < start:
        heappop(heap)
    result = max(result, len(heap))
print(result)