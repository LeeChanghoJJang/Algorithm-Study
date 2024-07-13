import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

points.sort()

start, end = points[0]
result = 0
for i in range(1, N):
    x, y = points[i]
    if end <= x:
        result += end - start
        start, end = x, y
    else:
        if end < y:
            end = y

result += end - start
print(result)