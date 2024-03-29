import sys
from heapq import *
sys.stdin = open('input.txt')

N = int(input())
heap =[]
for i in range(N):
    number = int(input())
    if number==0:
        if heap:print(heappop(heap)[1])
        else: print(0)
    elif number < 0:
        heappush(heap,(-number,number))
    elif number > 0 :
        heappush(heap,(number,number))