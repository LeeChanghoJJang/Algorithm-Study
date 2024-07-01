import sys
sys.stdin = open('input.txt')  # 입력을 파일에서 읽도록 설정

# 부모 노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:  # 현재 노드의 부모 노드가 자기 자신이 아니면
        parent[x] = find_parent(parent, parent[x])  # 부모 노드를 재귀적으로 찾아서 경로 압축
    return parent[x]  # 부모 노드 반환

# 두 집합을 합치는 함수
def union(parent, a, b):
    a = find_parent(parent, a)  # 노드 a의 부모 노드를 찾음
    b = find_parent(parent, b)  # 노드 b의 부모 노드를 찾음
    if a < b:  # 두 노드의 부모가 다르면
        parent[b] = a  # b의 부모를 a로 설정
    else:
        parent[a] = b  # a의 부모를 b로 설정

# 입력값 받음: N은 친구의 수, M은 친구 관계의 수, k는 친구들이 모이는데 드는 돈
N, M, k = map(int, input().split())

# 친구들의 가격 정보를 받음
friends_cost = list(map(int, input().split()))

# 각 노드의 부모 노드를 저장하는 배열 초기화(처음은 자기가 자기 무리의 대표노드)
parent = [i for i in range(N + 1)]

# 친구 관계를 입력받고 두 친구를 같은 무리로 합침
# 향후 가장 낮은 비용이 드는 친구에게만 비용지불 예정
for _ in range(M):
    v, w = map(int, input().split())
    union(parent, v, w)

# 부모 노드별로 친구들의 가격을 저장하는 사전 초기화
sep_dict = {i: set() for i in range(1, max(parent) + 1)}

# 친한 친구끼리 묶어 sep_dict에 저장
for i in range(1, N + 1):
    sep_dict[find_parent(parent, i)].add(friends_cost[i - 1])

# 각 친구무리별 최소 비용을 구하고 결과에 더함
result = sum(map(lambda x:min(x) if x else 0, sep_dict.values()))

# 소요비용이 내가 가진 돈 k를 초과하는지 확인하고 출력
print(result if result <= k else 'Oh no')
