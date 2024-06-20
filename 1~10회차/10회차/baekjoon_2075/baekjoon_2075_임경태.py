# 2075 N번째 큰 수
from heapq import heappop, heapify

N = int(input())
Q = []

for _ in range(N):
    Q += list(map(int, input().split()))
    heapify(Q)
    while len(Q) > N: heappop(Q)

print(Q[0])