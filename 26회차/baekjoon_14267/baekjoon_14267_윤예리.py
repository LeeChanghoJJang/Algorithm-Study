import sys
input = sys.stdin.readline

n, m = map(int, input().split())
par = [0] + list(map(int, input().split()))
point = [0] * (n+1)

for i in range(m):
    u, cnt = map(int, input().split())
    point[u] += cnt

for i in range(2, n+1):
    point[i] += point[par[i]]

for i in range(1, len(point)):
    print(point[i], end=' ')