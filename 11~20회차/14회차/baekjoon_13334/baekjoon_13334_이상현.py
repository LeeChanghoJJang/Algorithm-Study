from heapq import *

n = int(input())
list_ = []
max_ = 0

for _ in range(n):
    h, o = map(int, input().split())
    list_.append((max(h, o), min(h, o)))

list_.sort()
d = int(input())
q = []

for i in range(n):
    if list_[i][0] - list_[i][1] <= d:
        heappush(q, list_[i][1])
        while q and q[0] < list_[i][0] - d:
            heappop(q)
        max_ = max(max_, len(q))

print(max_)