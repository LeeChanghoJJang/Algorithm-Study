from heapq import *

N = int(input())
q = []

for _ in range(N):
    num_list = list(map(int, input().split()))
    len_ = len(q)

    for num in num_list:
        if len_ < N:
            heappush(q, num)
        else:
            heappush(q, num)
            heappop(q)

print(heappop(q))