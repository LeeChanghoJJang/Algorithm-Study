import sys
input = sys.stdin.readline

def find(x):
    if point[x] != x:
        point[x] = find(point[x])
    return point[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        point[y] = x
    else:
        point[x] = y

n, m = map(int, input().split())
point = [i for i in range(n)]

result = 0
for i in range(m):
    x, y = map(int, input().split())
    if result:
        continue
    if find(x) == find(y):
        result = i+1
    union(x, y)

print(result)
