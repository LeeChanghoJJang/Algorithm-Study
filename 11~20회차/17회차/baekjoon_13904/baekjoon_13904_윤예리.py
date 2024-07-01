from heapq import *

n = int(input())
arr = []
max_day = 0

for _ in range(n):
    d, w = map(int, input().split())
    heappush(arr, (-w, d))
    max_day = max(max_day, d)

visited = [False] * (max_day + 1)
score = 0

while arr:
    w, d = heappop(arr)

    for i in range(d, 0, -1):
        if visited[i]:
            continue

        visited[i] = True
        score -= w
        break

print(score)



