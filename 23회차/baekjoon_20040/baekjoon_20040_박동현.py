import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


# 유니온 파인드로 사이클 있는지 확인
def union(x, y):
    fx = find(x)
    fy = find(y)

    if rank[fx] > rank[fy]:
        root[fy] = fx
    elif rank[fx] < rank[fy]:
        root[fx] = fy
    else:
        root[fy] = fx
        rank[fx] += 1


def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]


N, M = map(int, input().split())

root = list(range(N))
rank = [0]*N

for i in range(M):
    a, b = map(int, input().split())
    if find(a) == find(b):
        exit(print(i+1))
    union(a, b)
print(0)
