from heapq import *
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = M
q = []

for _ in range(N):
    s, e = map(int, input().split())

    if s > e:
        heappush(q, [e, s])

if not q:
    exit(print(M))

scope = q[0]

while q:
    l, r = scope
    cur_l, cur_r = heappop(q)

    if l <= cur_l <= r:
        scope[1] = max(r, cur_r)
    else:
        result += 2 * (scope[1] - scope[0])
        scope = [cur_l, cur_r]

result += 2 * (scope[1] - scope[0])
print(result)