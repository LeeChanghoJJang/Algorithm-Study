import sys
input = sys.stdin.readline

# 두 점 사이의 거리를 계산하는 함수
def get_dist(loc1, loc2):
    x1, y1, x2, y2 = loc1[0], loc1[1], loc2[0], loc2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# 두 노드의 부모를 찾는 함수 (Union-Find)
def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])

    return parent[x]

# 두 노드를 합치는 함수 (Union-Find)
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 받기
n, m = map(int, input().split())
parent = [0] * (n+1)
edges = [0] * (n+1)
for i in range(1, n+1):
    edges[i] = list(map(int, input().split()))

# 간선 연결
for _ in range(m):
    a, b = map(int, input().split())
    union(parent, a, b)

# 가능한 모든 간선들의 거리 계산 및 정렬
possible = []
for i in range(1, len(edges)-1):
    for j in range(i+1, len(edges)):
        possible.append([get_dist(edges[i], edges[j]), i, j])
possible.sort()

# 최소 스패닝 트리의 비용 계산
ans = 0
for p in possible:
    cost, x, y = p[0], p[1], p[2]

    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        ans += cost

# 결과 출력
print("{:.2f}".format(ans))
