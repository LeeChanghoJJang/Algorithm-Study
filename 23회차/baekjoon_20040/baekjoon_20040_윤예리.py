import sys
input = sys.stdin.readline

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parentX = find(x)
    parentY = find(y)

    if parentX < parentY:
        parent[parentY] = parentX
    else:
        parent[parentX] = parentY

n, m = map(int, input().split())
parent = [i for i in range(n)]

for i in range(1, m+1):
    x, y = map(int, input().split())
    if find(x) == find(y): exit(print(i))
    union(x, y)

print(0)