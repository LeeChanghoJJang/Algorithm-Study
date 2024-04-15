from heapq import *

n, m = map(int, input().split())
q = list(map(int, input().split()))
heapify(q)

for _ in range(m):
    n1, n2 = heappop(q), heappop(q)
    sum_ = n1 + n2
    heappush(q, sum_)
    heappush(q, sum_)

print(sum(q))