import sys
from heapq import heappush,heappop
input = sys.stdin.readline
N = int(input())
hq = []
max_day = 0
for i in range(N):
    d, w = map(int, input().split())
    heappush(hq, (-w, d))
    if max_day < d:
        max_day = d

assigned = [0] * (max_day + 1)

score = 0
while hq:
    # 가장 스코어 높은 순으로 가져와서
    w, d = heappop(hq)
    w = -w

    # d일부터 1일 까지 거꾸로 돌면서 비어있는 날 중에 최대한 늦게 배정
    for i in range(d, 0, -1):
        if assigned[i]:
            continue

        assigned[i] = 1
        score += w
        break

print(score)
    