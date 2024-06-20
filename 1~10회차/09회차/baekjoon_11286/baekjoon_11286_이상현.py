import sys
input = sys.stdin.readline

from heapq import *

N = int(input())
q = []

for _ in range(N):
    x = int(input())

    if x:
        heappush(q, (abs(x), x))
    else:
        if q:
            print(heappop(q)[1])
        else:
            print(0)