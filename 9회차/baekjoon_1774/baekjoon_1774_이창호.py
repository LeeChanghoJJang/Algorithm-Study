import sys
sys.stdin = open('input.txt')
# 두 점 사이의 거리 계산 함수
def cal_distance(loc1, loc2):
    x1, y1, x2, y2 = loc1[0], loc1[1], loc2[0], loc2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# 루트 노드를 찾는 함수 (경로 압축)
def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 집합을 합치는 함수 (작은 집합을 큰 집합에 합침)
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 받기
N, M = map(int, input().split())
parent = list(range(N + 1))  # 각 정점의 부모를 저장할 리스트
edges = [0] * (N + 1)  # 각 정점의 좌표를 저장할 리스트

# 정점의 좌표 입력 받기
for i in range(1, N + 1):
    edges[i] = list(map(int, input().split()))

# 이미 연결된 정점들을 합치기
for _ in range(M):
    a, b = map(int, input().split())
    union(parent, a, b)

# 가능한 모든 간선 구하기
possible = []
for i in range(1, len(edges) - 1):
    for j in range(i + 1, len(edges)):
        possible.append([cal_distance(edges[i], edges[j]), i, j])

# 거리 순으로 간선 정렬
possible.sort()

result = 0
# Kruskal 알고리즘을 통해 최소 신장 트리 구하기
for p in possible:
    cost, x, y = p[0], p[1], p[2]
    if find(parent, x) != find(parent, y):  # 사이클을 형성하지 않으면 연결
        union(parent, x, y)
        result += cost

# 결과 출력
print(f'{result:.2f}')
