import sys

# 표준 입력을 'input.txt'에서 읽도록 재지정
sys.stdin = open('input.txt')

# 부모 노드를 찾는 함수
def find(x):
    if parent[x] != x:  # 루트 노드가 아니면
        parent[x] = find(parent[x])  # 루트 노드를 찾을 때까지 재귀적으로 호출하고 경로 압축
    return parent[x]

# 두 집합을 합치는 함수
def union(x, y):
    root_x = find(x)  # x의 루트 노드를 찾음
    root_y = find(y)  # y의 루트 노드를 찾음
    if root_x < root_y:  # x의 루트 노드가 y의 루트 노드보다 작으면
        parent[root_y] = root_x  # y가 속한 집합을 x가 속한 집합에 포함시킴
    else:  # 그렇지 않으면
        parent[root_x] = root_y  # x가 속한 집합을 y가 속한 집합에 포함시킴

# 입력 받기
input = sys.stdin.readline
V, E = map(int, input().split())  # 정점의 개수와 간선의 개수 입력
parent = list(range(V + 1))  # 각 정점의 부모 노드를 자기 자신으로 초기화
graph = [list(map(int, input().split()))[::-1] for i in range(E)]  # 간선 정보 입력 후 역순으로 저장 (가중치, 정점1, 정점2)
graph.sort()  # 가중치 순으로 정렬

result = 0  # 결과값 초기화
for wei, now, next in graph:  # 가중치 순서대로 간선을 확인
    if find(now) != find(next):  # 현재 간선의 양 끝 정점이 같은 집합에 속하지 않으면 (사이클이 생성되지 않으면)
        result += wei  # 결과값에 현재 간선의 가중치 추가
        union(now, next)  # 현재 간선의 양 끝 정점을 하나의 집합으로 합침

print(result)  # 최소 신장 트리의 가중치 합 출력
