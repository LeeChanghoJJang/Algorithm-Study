import sys
import heapq
sys.stdin = open('input.txt')

T= int(input())
heap = []
for tc in range(T):
    N, *gifts = map(int,input().split())
    if N == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(-1)
    else:
        for i in gifts:
            heapq.heappush(heap,(-i,i))
