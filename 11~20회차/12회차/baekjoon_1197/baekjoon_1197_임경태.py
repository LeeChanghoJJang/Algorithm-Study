# 1197 최소 스패닝 트리

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if x >= y:
        parent[y] = x
    else:
        parent[x] = y

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
parent = [i for i in range(V+1)]

# 가중치 크기별 오름차순 정렬
edges.sort(key=lambda x: x[2])
weight = 0

for edge in edges:
    # 루트 노드 찾기
    x, y, w = edge
    rx = find(x)
    ry = find(y)

    # 경로에 추가되지 않았으면 병합 및 가중치 카운트
    if rx == ry: continue
    union(rx, ry)
    weight += w

print(weight)