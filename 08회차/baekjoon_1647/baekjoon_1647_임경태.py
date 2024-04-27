# 1647 도시 분할 계획

# 특정 값의 루트 찾는 함수
def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

# 하나의 트리로 합치는 함수
def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

# N: 집의 개수, M: 길의 개수
N, M = map(int, input().split())
# 간선 비용 기준 오름차순 정렬
edges = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[2])
# 각각의 트리 생성 (부모가 자기 자신)
parent = [i for i in range(N+1)]
# 비용 배열
costs = []
# 간선 순회
for s, e, cost in edges:
    if find(s) != find(e):
        union(s, e)
        costs.append(cost)

print(sum(costs[:len(costs)-1]))

'''
- 신장 부분 그래프 (Spanning Graph)
    - 모든 노드를 포함하는 부분 그래프

- 최소 비용 신장 그래프 (Minumum Spanning Graph; MST)
    - 연결 유한 그래프의 연결 신장 부분 그래프 가운데, 변들의 비용의 합을 최소화한 그래프

- 크루스칼 알고리즘
    - 최소 비용 신장 트리를 찾는 알고리즘

    - 시간 복잡도 : O(ElogV) (E: 간선 개수, V: 노드 개수)

    - 알고리즘
        1. 그래프의 각 노드가 각각 하나의 트리가 되도록 하는 트리 생성
        2. 모든 간선을 원소로 갖는 집합 S를 제작
        3. S가 비어있지 않는 동안
            (1) 가장 작은 가중치의 간선을 하나 뺀다
            (2) 그 변이 어떤 2개의 트리를 연결한다면 두 트리를 하나로 통합한다
            (3) 그렇지 않는다면 그 간선은 버린다
'''