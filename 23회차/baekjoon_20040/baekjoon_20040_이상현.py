import sys
sys.stdin = open('input.txt')

def find(p):
    if p == parent[p]:
        return p

    parent[p] = find(parent[p])
    return parent[p]

def union(p1, p2):
    p1, p2 = find(p1), find(p2)

    if p1 > p2:
        parent[p1] = p2
    else :
        parent[p2] = p1

n, m = map(int, input().split())
parent = [i for i in range(n)]

for i in range(m):
    p1, p2 = map(int, input().split())

    if find(p1) == find(p2):
        print(i + 1)
        break

    union(p1, p2)
else :
    print(0)