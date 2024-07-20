# 20040 사이클 게임
N, M = map(int, input().split())
parent = [x for x in range(N)]

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    if parent_x < parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y

ans = 0
for i in range(1, M+1):
    x, y = map(int, input().split())
    if find(x) == find(y):
        ans = i
        break
    union(x, y)

print(ans)