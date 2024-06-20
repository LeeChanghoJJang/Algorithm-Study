import sys
from heapq import *

n = int(input())
arr = []

for _ in range(n):
    # sys.stdin.readline()이 아니면 시간초과임 
    x = int(sys.stdin.readline())
    
    if not x:
        try:
            print(heappop(arr)[1])
        except:
            print(0)
    else:
        heappush(arr, (abs(x), x))

