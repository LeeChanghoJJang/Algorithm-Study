import sys
input = sys.stdin.readline

# kruskal

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


v, e = map(int, input().split())
graph = []
parent = [i for i in range(v+1)]
weight = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

graph.sort(key=lambda x:x[2])
for i in range(e):
    a, b, c = graph[i]
    if find(a) != find(b):
        union(a, b)
        weight += c

print(weight)
